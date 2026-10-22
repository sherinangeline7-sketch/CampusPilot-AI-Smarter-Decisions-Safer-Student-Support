# Use case

CampusPilot AI — Smarter Decisions. Safer Student Support.

- **Pitch:** an AI-powered student support agent for Indian engineering colleges that answers
  academic and placement questions, guides students through timetable conflicts, and routes
  sensitive requests (medical leave, grade disputes, financial aid) to the right human authority
  — never making official decisions itself.
- **Who it is for:** final-year engineering students at an Indian college who need fast,
  reliable guidance on exams, placements, timetables and campus administration.
- **Features:**
  - answer academic and placement questions from a synthetic campus knowledge base;
  - provide a personalised placement / interview preparation plan on request;
  - guide students through timetable conflicts with clear next steps;
  - detect sensitive requests (medical leave, grade disputes, financial aid) and route them to
    the correct college authority with human confirmation;
  - block prompt-injection attempts and out-of-scope requests at the input stage;
  - show a live decision panel in the demo UI explaining every guardrail verdict;
  - deployed on Amazon Bedrock AgentCore Runtime.
- **The decision handed to Strands Decider 2B:** before every student message and every tool
  call, is this safe to process autonomously? Five typed questions in two stages:
  - **Input stage** (before the LLM acts): is it a prompt-injection attempt? is it within the
    agent's scope? is it a sensitive request requiring human authority?
  - **Tool stage** (before each tool call): are the tool arguments grounded in what the student
    said? is it premature to call this tool now?
  Pattern: `#guardrails`
- **Why a decision model:** the safety check runs on every single message and every tool call.
  It must be fast, cheap and produce a calibrated confidence the code can branch on — exactly
  what Strands Decider 2B is built for.
- **Amazon Bedrock:** Amazon Nova Pro by default; the conversation and all tool use go through
  the Strands Agents SDK.
- **Author:** Sherin Angeline A
- **Team:** CampusPilot Team
- **Data:** synthetic demo data — fictional Indian engineering college. Not official college
  policy. Replace with a real college API for production use.
