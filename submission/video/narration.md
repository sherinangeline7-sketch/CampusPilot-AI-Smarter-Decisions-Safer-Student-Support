0. CampusPilot AI runs on Amazon Bedrock AgentCore Runtime. Every student message and tool call is checked by Strands Decider before the agent acts, using typed questions across multiple stages.

1. An AI student support agent that answers campus questions, guides timetable conflicts, and routes sensitive requests to the right human authority â€�  never making official decisions itself. What it does: Answer exam schedules, timetable and policy questions from a campus knowledge base. Generate structured placement and interview preparation plans. Detect timetable conflicts and recommend clear next steps. Route sensitive requests (medical leave, grade disputes) to the correct authority with human confirmation.

2. A timetable conflict â€�  a common, stressful problem. The decider checks: in scope? not sensitive? Then the agent explains the steps and recommends contacting the Academic Section. The decider scored injection 0.07, in scope 0.98, sensitive 0.10, so the verdict was proceed, in 5.3 seconds. The decider scored args grounded 0.55, premature 0.50, so the verdict was guide, in 3.2 seconds.

3. A placement preparation request. The decider confirms it is in scope and not sensitive. The agent builds a structured day-by-day plan using the campus placement knowledge base. The decider scored injection 0.08, in scope 0.96, sensitive 0.06, so the verdict was proceed, in 4.4 seconds.

4. A sensitive request â€�  this needs a human authority. The decider flags sensitive=high confidence. The agent explains the official process and directs the student to the HOD, without claiming to approve anything. The decider scored injection 0.19, in scope 0.92, sensitive 0.68, so the verdict was confirm, in 5.2 seconds.

5. On 44 labelled decisions, with the decider on the AWS User Group Madurai hosted API, Strands Decider was 73% accurate at a median of 5074 milliseconds, against 95% and 20773 milliseconds for a hosted open LLM asked the same questions.

6. One forward pass per guardrail check. Five typed questions, calibrated confidence the code branches on, and Amazon Bedrock for the conversation. Built with the AWS User Group Madurai Strands Decider hackathon kit.