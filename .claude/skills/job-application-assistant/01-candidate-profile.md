---
framework_version: 1.1.1
---

# Candidate Profile

<!-- Populated by /setup on 2026-10-04 from cv/shahtirthhh.tex plus follow-up answers. -->

## Identity
- **Name:** Tirth Shah
- **Location:** India (home city not recorded - add it here if a posting needs a commute check)
- **Phone:** +91-9377461119
- **Email:** shahtirth0212@gmail.com
- **LinkedIn:** https://linkedin.com/in/shahtirthhh
- **GitHub:** https://github.com/shahtirthhh
- **Website:** https://tirthcodes.dev
- **LeetCode:** https://leetcode.com/u/shahtirthhh
- **Status:** Employed full-time as Software Engineer at Digipine Infotech LLP; pursuing a part-time M.Tech in AI (IIT Jodhpur, 2026-2028) alongside work. Looking for full-time roles.
- **Constraints:** Open to relocation within India and abroad, and to remote roles. Roles outside India need visa sponsorship (citizenship / work authorization not recorded - assumed Indian citizen, confirm). A new role must be compatible with continuing the part-time M.Tech.

### Languages
<!-- Used by the Language Gate in 04-job-evaluation.md and by job-scraper/search-queries.md. -->

| Language | Level | Notes |
|----------|-------|-------|
| English | Fluent / professional | Working language; CVs and client communication |
| Hindi | Fluent | |
| Gujarati | Native | |

## Education

| Degree | Period | Institution | Key Topics |
|--------|--------|-------------|------------|
| M.Tech in Artificial Intelligence | 2026-2028 (in progress, part-time alongside work, expected 2028) | Indian Institute of Technology Jodhpur | Artificial Intelligence |
| B.E. in Computer Engineering, First Class with Distinction | Graduated 2024 (start year not recorded) | LDRP Institute of Technology and Research | Computer Engineering |

## Professional Experience

Total: about 3 years including freelance (Jul 2023 - present).

### Software Engineer - Digipine Infotech LLP (Sep 2023 - Present)
<!-- Start date corrected from Sep 2024 to Sep 2023 on 2026-10-30: Tirth confirmed he joined in Sep 2023. The freelance entry below (Jul 2023 - Aug 2024) now overlaps it; Tirth to confirm those dates before it is used on a CV. -->
India (office city not recorded)
- Joined as Associate Software Engineer; promoted to Software Engineer within 7 months after delivering 2 telephony products with Twilio, ElevenLabs, Kafka, and Redis.
- Went on to own design and delivery of 3 production AI and messaging products, from first design to cloud deployment on AWS and GCP.
- Delivered two product tracks on schedule for two quarters with three developers, by running Agile sprints and weekly design reviews.
- Cut onboarding time for 2 interns from 2 weeks to 1 through structured code reviews and pair programming.

### Full Stack Engineer (Contract) - Freelance, Self-Employed (Jul 2023 - Aug 2024)
- Delivered 2 client projects on the agreed timelines by gathering requirements directly from clients on weekly calls, sharing a demo every sprint, and confirming scope changes in writing.
- Built and deployed 2 full stack AI products end to end, using React, Node.js, NestJS, Docker, and AWS EC2 with NGINX.

## Projects
<!-- The source CV lists these in one Projects section without saying which were built at
Digipine and which were freelance. Do NOT attribute a project to an employer in a CV or
cover letter until Tirth confirms the mapping. -->

- **Omni-channel Communication Platform (WhatsApp, SMS, Voice)** - React, Node.js, MongoDB, Kafka, LangChain, RAG, Vector Search, WhatsApp Cloud API, Twilio, Docker, AWS ECS
  - Cut client onboarding from about 2 days of manual setup to under 15 minutes by implementing Meta's Solution Partner onboarding flow (Embedded Signup, token exchange, webhook subscriptions) so each of 4 client admins connects their own WhatsApp number.
  - Raised answer accuracy from about 65% to 80% on a 60-question test set by building a per-tenant knowledge base with LangChain, RAG, and vector search, and tuning chunk size, top-k, similarity threshold, and temperature.
  - Delivered messages in under 1 second at about 10K events per day with no cross-tenant data issues, via a Kafka routing layer with per-tenant topics, containerized with Docker on AWS ECS.
- **AI Debt Recovery Platform** - React, FastAPI, LangGraph, ChromaDB, OpenAI, Docker, GCP
  - Cut case review time by about 40% across roughly 500 debt accounts per month with a human-in-the-loop AI agent (LangGraph, OpenAI function calling, RAG over account history and recovery policies in ChromaDB); staff approve suggested actions in a React dashboard.
- **A2P/10DLC Compliance Bot** - React, NestJS, LangChain, RAG, Vector Search, Google AI Studio APIs, Twilio, AWS EC2, NGINX
  - Raised first-attempt registration approval from about 60% to 75% across 20 pilot accounts; users connect their Twilio account, have their website analyzed, and get a compliance report with fixes.
  - Cut compliance review from about 2 hours to 10 minutes per account by combining LangChain RAG over carrier and messaging guidelines with Google AI Studio APIs.
- **Voice AI Agent for Lead Follow-up** - Twilio, ElevenLabs, NestJS, Redis, Docker, AWS EC2
  - Reached about 15% more previously missed leads and cut pre-qualification time by about 25%; the agent calls back leads, collects details, keeps call state in Redis, and hands qualified leads to a human agent.
- **Bulk Call Forwarding Platform** - FreeSWITCH APIs, Kafka, Redis, Angular, Docker, Kubernetes, AWS ECS, NGINX
  - Handled about 100 simultaneous calls with routing latency under 300 ms in load tests (FreeSWITCH APIs, Kafka consumers for call events, Redis routing tables, Angular operator dashboard).
- **Real-time Football Coaching Platform (SaaS)** - React, Node.js, Claude API, LangChain, Socket.IO, Docker, AWS EC2, NGINX
  - Cut coach session planning time from about 1 hour to 10 minutes; coaches and clubs create training sessions with AI-generated animated drills from the Claude API and LangChain.
  - Kept session boards in sync for about 50 concurrent users with updates under 500 ms using Socket.IO on Node.js.
- **AI Story and Image Sharing Mobile App (Backend)** - NestJS, Kafka, Redis, OpenAI, Ideogram, RevenueCat, Docker, GitHub Actions
  - Sustained 150 concurrent users at p95 response time under 300 ms in load tests (NestJS, Kafka event streaming, Redis caching, Docker deployments through GitHub Actions).
  - Generated about 500 personalized stories and images per day by integrating OpenAI and Ideogram with dynamic prompts; cut payment integration from 2 weeks to 4 days with reusable RevenueCat webhook handlers.

## Independent Projects
<!-- Projects outside of employment: freelance, open source, personal -->
- **void-snippets (Creator & Maintainer)**: open-source NPM package, a pnpm monorepo of typed HTTP, TanStack Query, and Socket.IO helpers (TypeScript, React). About 200 weekly NPM downloads in 3 months; saved about 1 hour of setup per feature across 3 internal codebases.

## Technical Skills

### Programming & AI
- **Languages:** TypeScript, JavaScript, Java, Python, SQL
<!-- Vue 3 (Composition API), Java and Spring Boot added 2026-10-30 on Tirth's word that he has used them. No project or employer is recorded for them, so do not write a project bullet or metric for them until Tirth supplies one. Pinia, Vitest and JUnit were NOT confirmed. -->
- **Frontend:** React, Vue 3 (Composition API), Angular, TanStack Query, Socket.IO, REST APIs
- **Backend:** Spring Boot, NestJS, Node.js, FastAPI, WebSocket, Apache Kafka, Redis
- **AI & LLM:** LangChain, LangGraph, RAG, Vector Search (ChromaDB), Embeddings, OpenAI API (Function Calling), Claude API, Google AI Studio (Gemini), Prompt Engineering, LLM Evaluation, ElevenLabs, Vapi, Retell AI
- **Databases:** PostgreSQL, MongoDB, Redis, Firebase

### Domain Expertise
- LLM applications: RAG pipelines, human-in-the-loop agents, multi-tenant knowledge bases, retrieval tuning and evaluation
- Voice AI and telephony: Twilio, Telnyx, FreeSWITCH, ElevenLabs, Vapi, Retell AI
- Business messaging: Meta Business APIs (WhatsApp Cloud API, Embedded Signup, Webhooks), SMS, A2P/10DLC compliance
- Event-driven microservices: Kafka, Redis, real-time systems (WebSocket, Socket.IO)
- Small-team delivery: Agile sprints, design reviews, code review, mentoring interns, direct client requirement gathering

### Software & Tools
- **Cloud & DevOps:** AWS (EC2, ECS, S3, Lambda), GCP, Docker, Kubernetes, NGINX, GitHub Actions CI/CD, Git, Agile/Scrum
- **APIs & Integrations:** Meta Business APIs, Twilio, Telnyx, FreeSWITCH APIs, RevenueCat, Jobber, Make, Zapier

## Publications
None.

## Awards
- Solved 70+ data structures and algorithms problems on LeetCode (https://leetcode.com/u/shahtirthhh)

## References
None recorded. Use "Available upon request."
