# Search Queries for Job Scraper

<!-- Populated by /setup on 2026-10-04. Re-run `/setup --section search` to change. -->

## Installed portal CLIs (primary for `/scrape`)

`/scrape` discovers every portal skill under `.agents/skills/*/SKILL.md` and runs its CLI first. Shipped country-agnostic CLIs include `linkedin-search` and `freehire-search`; Danish demos and any skill you add with `/add-portal` are included the same way. You do **not** need a matching `site:` line below for those CLIs to run.

The `site:` query templates in this file are the **WebSearch fallback** — for portals without a CLI, company career pages, or when a CLI fails.

**Language scope:** write every query category in every language listed in your CLAUDE.md Languages table (typically 1-2, sometimes more). A posting requiring a language you have *not* declared, as a job condition, is excluded before scoring; a posting requiring a *higher level* than you declared in a language you *do* work in is flagged for your own judgment, not excluded — see `04-job-evaluation.md`'s Language Gate, the single source of truth for this rule. Translate each category's keywords rather than machine-translating word-for-word (e.g. "Frontend Developer" -> "Desarrollador Frontend", not a literal word-for-word translation) if you work in more than one language.

## Search Sites

Primary:
- **linkedin.com/jobs** - LinkedIn job listings (filter: India, plus Remote / Worldwide); covered by the `linkedin-search` CLI
- **freehire** - covered by the `freehire-search` CLI
- **naukri.com** - India's largest general job board (no CLI yet - scaffold one with `/add-portal`)
- **wellfound.com** - startup roles, India and remote
- **instahyre.com**, **cutshort.io**, **hirist.tech** - Indian tech-focused boards

Secondary (company career pages via Google):
- Direct Google searches with `site:` filters for known target companies
- ATS-hosted pages: `site:boards.greenhouse.io`, `site:jobs.lever.co`, `site:jobs.ashbyhq.com`

The Danish demo portals (Jobindex, Jobbank, Jobdanmark, Jobnet) stay disabled - not Tirth's market.

## Query Categories

Queries are grouped by priority. All queries are in **English**: it is the working language of the Indian and international tech market, and Hindi/Gujarati postings for these roles are not a meaningful source. Location terms: `India`, `Remote`, and the hubs `Bengaluru`, `Hyderabad`, `Pune`, `Mumbai`, `Gurugram`, `Noida`, `Ahmedabad`.

**Organize by function, not job title.** The same underlying work carries different titles across companies, so each category lists several title variants.

**Seniority:** about 3 years of experience. Prefer postings asking for 1-5 years; skip Senior Staff / Principal / 8+ years and unpaid internships.

### Priority 1: AI / LLM application engineering

Building production GenAI products: RAG, agents, voice AI.

```
site:linkedin.com/jobs "AI Engineer" LangChain India
site:linkedin.com/jobs "Generative AI Engineer" India
site:linkedin.com/jobs "LLM Engineer" OR "Applied AI Engineer" India OR Remote
site:naukri.com "Generative AI Engineer" RAG LangChain
site:naukri.com "AI Engineer" LangGraph OR "AI agents"
site:wellfound.com "AI Engineer" RAG remote
site:instahyre.com "AI Engineer" LLM
site:jobs.ashbyhq.com OR site:boards.greenhouse.io "AI Engineer" LangChain remote India
"Voice AI Engineer" Twilio OR ElevenLabs OR Vapi OR "Retell" remote
"Full Stack AI Engineer" React "LLM" India OR Remote
```

### Priority 2: Full stack and backend product engineering

React + Node.js/NestJS products, event-driven backends.

```
site:linkedin.com/jobs "Full Stack Engineer" React NestJS India
site:linkedin.com/jobs "Software Engineer" TypeScript Node.js India
site:linkedin.com/jobs "Backend Engineer" Node.js Kafka India
site:naukri.com "Full Stack Developer" React Node.js NestJS
site:naukri.com "Backend Developer" NestJS Kafka Redis
site:naukri.com "Software Engineer" TypeScript React "Node.js"
site:wellfound.com "Full Stack Engineer" TypeScript remote
site:cutshort.io "Backend Developer" Node.js Kafka
site:hirist.tech "Full Stack Developer" React NestJS
"Backend Engineer" FastAPI OR NestJS Kafka remote India
```

### Priority 3: Solutions / Forward Deployed / integrations

Client-facing engineering, using the freelance and integrations background (WhatsApp Cloud API, Twilio, telephony).

```
site:linkedin.com/jobs "Forward Deployed Engineer" India OR Remote
site:linkedin.com/jobs "Solutions Engineer" AI OR LLM India
site:linkedin.com/jobs "AI Solutions Engineer" OR "AI Integration Engineer" India OR Remote
site:wellfound.com "Forward Deployed Engineer" AI
"Solutions Engineer" "WhatsApp" OR "Twilio" OR "conversational AI" India
"Integration Engineer" "WhatsApp Business API" OR "CPaaS" India
site:naukri.com "Solutions Engineer" "Generative AI"
```

### Priority 4: Broader software and frontend roles

Wider net.

```
site:linkedin.com/jobs "Frontend Developer" React TypeScript India
site:naukri.com "Frontend Developer" React "TanStack" OR "TypeScript"
site:naukri.com "React Developer" TypeScript
site:linkedin.com/jobs "Software Engineer" "visa sponsorship" OR "relocation" TypeScript
site:linkedin.com/jobs "Software Engineer" Node.js React Remote
"Software Development Engineer" SDE-2 OR "SDE 2" Node.js India
"Founding Engineer" TypeScript AI remote
```

## Location Filter

Tirth is open to relocation within India and abroad, so location is rarely a veto:
- **Ideal:** fully remote (India or international), or major Indian tech hubs (Bengaluru, Hyderabad, Pune, Mumbai, Gurugram/Noida, Ahmedabad/Gandhinagar)
- **Acceptable:** any other city in India
- **Acceptable with sponsorship:** outside India where the posting offers visa sponsorship or relocation support
- **Borderline:** outside India where sponsorship is not mentioned - include but flag "sponsorship unverified"
- **Exclude:** outside India where the posting requires existing work authorization, citizenship, permanent residency or a security clearance (see `04-job-evaluation.md`'s Eligibility Gate)
- **Flag:** any role whose hours or location would conflict with the part-time M.Tech at IIT Jodhpur (2026-2028)

## Language Filter

Your working languages and levels are in CLAUDE.md's Languages table. When filtering scraped results, apply `04-job-evaluation.md`'s Language Gate: a posting requiring a language you haven't declared at all is excluded; a posting requiring a higher level than you declared in a language you do work in is not excluded, flag it clearly instead (see `job-scraper/SKILL.md`'s Step 3 "Quick Fit Assessment" for how the flag surfaces in `/scrape` output). Postings simply *written* in a language you don't work in, that don't require it on the job, are fine.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- "/scrape [focus_area]" -> relevant category queries + custom focus-specific queries
