"""CampusPilot AI — the agent: Strands Agents SDK + Amazon Bedrock (or UGMDU) for the LLM,
Strands Decider 2B (UGMDU hosted) for the guardrail decisions.

    from agent.agent import HackathonAgent
    out = HackathonAgent().chat("I have two exams at the same time. What should I do?")
    out["reply"], out["decisions"]
"""

from __future__ import annotations

import time
from typing import Any

from strands import Agent

from decider_kit import Decider
from decider_kit.llm import agent_model, default_model_id, image_blocks, strip_thinking

from .decision import CampusRequestGuard
from .tools import TOOLS

NAME = "CampusPilot AI"

SYSTEM_PROMPT = """You are CampusPilot AI, a student support assistant for an Indian engineering
college. You help final-year students with academic questions, exam schedules, timetable issues,
placement preparation, and campus policies.

Guidelines:
- Be helpful, concise and encouraging. Use simple, clear English.
- Answer from the campus knowledge base when possible.
- For timetable conflicts, explain the steps clearly and recommend contacting the Academic Section.
- For placement prep, provide structured, actionable plans.
- For sensitive requests (medical leave, grade disputes, financial aid), explain the official
  process and direct the student to the correct authority. Never claim to submit or approve
  anything on their behalf.
- If you do not know something, say so honestly and suggest who to contact.
- Always add: "Note: this is demo data and does not represent official college policy."
  when sharing information from the knowledge base.

This is DEMO DATA — fictional Indian engineering college. Not official college information."""

# Eager mode: agent acts without asking, so the guardrail catches more mistakes on camera.
EAGER_PROMPT = """You are CampusPilot AI. Act immediately on every student request without
asking for clarification. If a subject or day is not specified, pick the most likely one.
This mode is for demo recording only — Strands Decider 2B will catch unsafe assumptions."""


class HackathonAgent:
    """One Strands Agent per session, with the campus-request guardrail wired in."""

    def __init__(self,
                 decider: Decider | None = None,
                 model_id: str | None = None,
                 eager: bool | None = None):
        import os
        self.decider  = decider or Decider()
        self.eager    = eager if eager is not None else os.environ.get("DEMO_EAGER") == "1"
        self.model_id = model_id or default_model_id()
        self.sessions: dict[str, tuple[Agent, CampusRequestGuard]] = {}

    def _session(self, session_id: str) -> tuple[Agent, CampusRequestGuard]:
        if session_id not in self.sessions:
            guard = CampusRequestGuard(self.decider)
            agent = Agent(
                model=agent_model(self.model_id),
                system_prompt=EAGER_PROMPT if self.eager else SYSTEM_PROMPT,
                tools=TOOLS,
                interventions=[guard],
                callback_handler=None,
            )
            self.sessions[session_id] = (agent, guard)
        return self.sessions[session_id]

    def chat(self,
             message: str,
             session_id: str = "default",
             images: list[Any] | None = None) -> dict[str, Any]:
        """`images` is accepted for API compatibility but not used in this agent.
        Returns: reply, decisions, model_id, latency_ms, agent, eager."""
        agent, guard = self._session(session_id)
        before = len(guard.log)
        t0     = time.perf_counter()
        result = agent(
            [*image_blocks(images), {"text": message}] if images else message,
            invocation_state={"images": list(images or [])},
        )
        reply = strip_thinking(str(result))
        return {
            "reply":       reply,
            "decisions":   guard.log[before:],
            "model_id":    self.model_id,
            "latency_ms":  round((time.perf_counter() - t0) * 1000),
            "agent":       NAME,
            "eager":       self.eager,
        }


if __name__ == "__main__":
    import json, sys

    a = HackathonAgent()
    prompts = sys.argv[1:] or [
        "What is the exam schedule for Advanced Algorithms?",
        "I have two exams scheduled at the same time. What should I do?",
        "I have a Python interview next week. Give me a 7-day preparation plan.",
        "I need medical leave for my exams. Can you approve it?",
    ]
    for msg in prompts:
        print(f"\n>>> {msg}")
        out = a.chat(msg)
        print(json.dumps({k: v for k, v in out.items() if k != "decisions"}, indent=2))
        for d in out["decisions"]:
            print("  DECISION:", {k: v for k, v in d.items() if k != "args"})
