# Candidate Modes

This workspace serves two candidates. Every request runs in exactly one mode, and the
mode decides which profile, CV, search queries and state files are read and written.

| Mode | Candidate | Say | Profile source |
|------|-----------|-----|----------------|
| **wind** | Tirth Shah | "wind mode", or `/scrape wind`, `/apply wind ...` | The repo defaults: `CLAUDE.md` profile summary and `.claude/skills/job-application-assistant/0*-*.md` |
| **nish** | Nishchal Namdeo | "nish mode", or `/scrape nish`, `/apply nish ...` | `profiles/nish/` (overrides the defaults listed below) |

The mode stays active for the rest of the conversation until the user switches. If no mode
has been named yet and the request is candidate-specific (scrape, evaluate, CV, cover
letter, interview prep), ask which mode before doing anything. Never mix the two: a fit
assessment, CV or cover letter must only use facts from the active candidate's profile.

## Path map

Shared, mode-independent files (portal CLIs, `04-job-evaluation.md` framework, `03-writing-style.md`,
`07`/`08`/`09` guides, `tools/`) are used by both modes.

| What | wind (Tirth) | nish (Nishchal) |
|------|--------------|-----------------|
| Candidate profile | `.claude/skills/job-application-assistant/01-candidate-profile.md` | `profiles/nish/01-candidate-profile.md` |
| Behavioral profile | `.claude/skills/job-application-assistant/02-behavioral-profile.md` | `profiles/nish/02-behavioral-profile.md` |
| Search queries | `.claude/skills/job-scraper/search-queries.md` | `profiles/nish/search-queries.md` |
| Base CV | `cv/shahtirthhh.tex` | `cv/nish/nishchal_namdeo.tex` |
| Tailored CVs | `cv/main_<company>_<role>.tex` | `cv/nish/main_<company>_<role>.tex` |
| Cover letters | `cover_letters/cover_<company>_<role>.tex` | `cover_letters/nish/cover_<company>_<role>.tex` |
| Seen jobs (dedup) | `job_scraper/seen_jobs.json` | `job_scraper/nish/seen_jobs.json` |
| Application tracker | `job_search_tracker.csv` | `job_search_tracker_nish.csv` |
| Application archive | `documents/applications/<company>_<role>/` | `documents/applications/nish/<company>_<role>/` |

Seen-jobs files are per candidate on purpose: a job skipped as a poor fit for one
candidate may be a strong fit for the other.

## CV template and compile command

Both base CVs use the same single-column, ATS-safe `article` template (no moderncv, no
icons). Compile with **pdflatex** (the template uses `glyphtounicode` / `\pdfgentounicode`).
The CLAUDE.md "exactly 2 pages" rule applies to wind; **nish CVs are exactly 1 page**
(her base CV is a 1-page resume). All other Verification Checklist items apply to both.
