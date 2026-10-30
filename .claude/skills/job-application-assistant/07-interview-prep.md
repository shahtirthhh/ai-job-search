---
framework_version: 1.0.0
---

# Interview Preparation Guide

<!-- SETUP: STAR examples are personalized by running /setup based on your actual experience -->

## STAR Format

Structure answers as: **Situation** (context), **Task** (your responsibility), **Action** (what you did), **Result** (outcome).

Keep answers to 1-2 minutes. Be specific. End with what you learned or would do differently.

## Ready-Made STAR Examples

<!-- Populated by /setup on 2026-10-04 from the CV. Situation/Task lines only restate what
the CV says; items marked [ADD: ...] need Tirth's own detail before use in an interview. -->

### 1. Omni-channel Communication Platform: RAG accuracy (measurement-driven AI engineering)
**S:** A multi-tenant WhatsApp/SMS/voice platform needed an assistant that answered from each client's own knowledge base; answer accuracy was about 65% on a 60-question test set.
**T:** Raise answer quality per tenant without leaking data across tenants.
**A:** Built a per-tenant knowledge base with LangChain, RAG and vector search; tuned chunk size, top-k, similarity threshold and temperature against the 60-question test set. [ADD: how the test set was built and which change moved accuracy most]
**R:** Accuracy rose from about 65% to 80%; no cross-tenant data issues.
**Use for:** "Tell me about an LLM/RAG system you built", "How do you evaluate LLM output?", "Describe a time you improved something with data"

### 2. WhatsApp onboarding with Meta Embedded Signup (complex third-party integration)
**S:** Onboarding a new client onto WhatsApp took about 2 days of manual setup.
**T:** Let each client admin connect their own WhatsApp number self-serve.
**A:** Implemented Meta's Solution Partner onboarding flow: Embedded Signup, token exchange and webhook subscriptions. [ADD: the hardest part of the Meta flow and how it was debugged]
**R:** Onboarding dropped to under 15 minutes; 4 client admins connected their own numbers.
**Use for:** "Tell me about a difficult integration", "A time you removed a manual process", "Working with poorly documented APIs"

### 3. AI Debt Recovery Platform (agent design with human in the loop)
**S:** Staff reviewed roughly 500 debt accounts per month by hand against account history and recovery policies.
**T:** Speed up case review while keeping a person in control of every action.
**A:** Built a LangGraph agent with OpenAI function calling and RAG over account history and policies in ChromaDB (FastAPI, GCP); staff approve suggested actions in a React dashboard. [ADD: why human approval was chosen and how failures are handled]
**R:** Case review time cut by about 40%.
**Use for:** "Design an AI agent", "How do you make AI safe in a sensitive domain?", "A product you owned end to end"

### 4. Promotion and team delivery at Digipine (ownership, leadership)
**S:** Joined Digipine Infotech as Associate Software Engineer in Sep 2023.
**T:** Deliver 2 telephony products (Twilio, ElevenLabs, Kafka, Redis), then take ownership of larger work.
**A:** Delivered both, was promoted to Software Engineer within 7 months, then ran Agile sprints and weekly design reviews for two product tracks with three developers, and onboarded 2 interns through structured code reviews and pair programming.
**R:** Both tracks delivered on schedule for two quarters; intern onboarding cut from 2 weeks to 1; owned 3 production AI and messaging products from design to deployment.
**Use for:** "Tell me about a time you led", "How do you mentor?", "Why were you promoted?"

### 5. Freelance client delivery (stakeholder management)
**S:** Worked as a freelance full stack engineer (Jul 2023 - Aug 2024) on 2 client projects.
**T:** Deliver on agreed timelines with changing requirements and no team behind him.
**A:** Gathered requirements on weekly client calls, shared a demo every sprint, and confirmed scope changes in writing. [ADD: one concrete scope change and how it was handled]
**R:** Both projects delivered on the agreed timelines; 2 full stack AI products deployed on AWS EC2 with NGINX.
**Use for:** "Handling a difficult stakeholder", "Managing scope creep", "Working independently"

### 6. Real-time backends under load (performance)
**S:** An AI story and image app backend, and a bulk call forwarding platform, both needed predictable latency.
**T:** Hold response times under load.
**A:** NestJS with Kafka event streaming and Redis caching for the app; FreeSWITCH APIs with Kafka consumers and Redis routing tables for call forwarding; verified with load tests.
**R:** 150 concurrent users at p95 under 300 ms; about 100 simultaneous calls with routing latency under 300 ms.
**Use for:** "How do you design for performance?", "Tell me about Kafka/Redis in production", "How do you test at load?"

## Common Tough Questions

### "Why are you leaving Digipine?" (still employed there)
> [PREPARE YOUR ANSWER - be honest, forward-looking, no negativity about the employer. Likely angle: promoted fast and owned products end to end; now wants larger scale and deeper AI work.]

### "You don't have [specific skill/experience]."
> [PREPARE YOUR ANSWER - acknowledge the gap, bridge to adjacent experience, show willingness to learn. Likely gaps: model training/fine-tuning (bridge: M.Tech in AI in progress, plus production LLM evaluation work), years of experience (about 3), very large scale.]

### "How will you manage the M.Tech alongside this job?"
> [PREPARE YOUR ANSWER - state plainly that it is a part-time programme (IIT Jodhpur, 2026-2028) already running alongside the current full-time job, and what the time commitment is.]

### "Which of these projects were at Digipine and which were freelance?"
> [PREPARE YOUR ANSWER - the CV lists projects without an employer; have the mapping ready.]

### "Where do you see yourself in 5 years?"
> [PREPARE YOUR ANSWER - show ambition aligned with the role's growth path]

### "What's your biggest weakness?"
> [PREPARE YOUR ANSWER - genuine weakness with concrete mitigation strategy]

### "Why this company specifically?"
> Customize per company. Must reference: specific projects, company values, market position, or team structure. Never give a generic answer.

## Questions You Should Ask Interviewers

### About the Role
- "What does a typical week look like in this role?"
- "What would success look like in the first 6 months?"
- "What's the biggest challenge the team is facing right now?"

### About the Team
- "How big is the team, and how do you divide work?"
- "What does the development/project lifecycle look like, from idea to production?"
- "How do you onboard new team members?"

### About Tech & Growth
- "What's your current tech stack for [relevant area]?"
- "Is there room to grow into more architectural or strategic decisions?"
- "How does the team stay current with new tools and methods?"

### About Culture (use these to prevent disappointment)
- "How would you describe the team culture?"
- "What does professional development look like here?"
- "Is there flexibility for remote/hybrid work?"
- "What's the balance between development/new projects and maintenance work?"
- "How would you describe the leadership style in this team?"
- "What do people who thrive here have in common?"

## Phone/Video Interview Tips
- Have STAR examples written out (use this file)
- Keep a glass of water nearby
- Smile when speaking (it changes your tone)
- Ask for clarification if a question is vague
- It's OK to take 5 seconds to think before answering
- End with: "Is there anything else you'd like to know about my background?"

## After the Application (Best Practice)

### Follow-Up Etiquette
- **Don't call to "stand out"** or to learn more about the role post-submission - this risks a negative impression
- If the employer specified a timeline, respect it and wait
- If no timeline was given and significant time has passed (2+ weeks), a brief call to ask about status is acceptable
- If you have genuinely new, relevant information to share, a short follow-up is fine

### Thank-You Notes
- When you receive any update (interview invitation, rejection, or status update), send a brief thank-you message
- Express appreciation for their time and the process
- Keep it short (2-3 sentences)

## Roleplay Guidelines
When the user asks for interview practice:
1. Ask which role/company to simulate
2. Start with easy warm-up questions ("Tell me about yourself")
3. Progress to role-specific technical questions
4. Include 1-2 behavioral questions using the competencies from the job posting
5. End with a tough question or curveball
6. After each answer, give brief feedback: what worked, what to sharpen
7. Suggest which STAR example would work best for each question
