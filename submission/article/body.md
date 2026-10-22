# CampusPilot AI: Smarter Decisions, Safer Student Support

## The problem

Students often need quick answers about campus policies, examination schedules, timetable conflicts, and placement preparation. Sensitive requests, such as medical leave and grade disputes, also require the right human authority rather than an automated decision.

## Our solution

CampusPilot AI is an AI-powered student support agent designed to help students find information and understand their next steps.

The project focuses on four main capabilities:

- Answering campus questions using a campus knowledge base.
- Creating structured placement and interview preparation plans.
- Identifying timetable conflicts and recommending practical next steps.
- Directing sensitive requests to the appropriate human authority.

## Safety through guardrails

An important part of CampusPilot AI is its use of Strands Decider to check requests before the agent acts. The system is designed to identify requests that are outside its scope or involve sensitive decisions.

For example, when a student asks for medical leave approval, the agent explains the official process and directs the student to the appropriate authority instead of claiming to approve the request.

This approach aims to make student support more useful while keeping important decisions under human control.

## Technology

The project uses Amazon Bedrock AgentCore Runtime as its intended deployment environment, Amazon Bedrock for conversational AI, and Strands Decider for request guardrails. The hackathon kit supports the project workflow, demonstration, and submission preparation.

## What I learned and what is next

Building CampusPilot AI helped me understand how an AI agent can combine useful responses with safety checks and human oversight. I also learned the importance of handling sensitive requests carefully and providing clear next steps instead of making decisions that require human approval.

The next steps are to complete deployment, test the guardrails against more real-world student questions, improve the campus knowledge base, and collect feedback from students and staff. Further testing will help identify gaps and make the system more reliable.

## Project links

Code: Add the public repository URL before publishing this article.

Video: Add the public demo video URL after uploading demo.mp4 to YouTube or Vimeo.

Tags: #strands-decider-2b #guardrails #amazon-bedrock #strands-agents #agentcore

Built with the AWS User Group Madurai Strands Decider hackathon kit.
