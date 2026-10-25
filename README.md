
# Capstone 58: Multi-Agent Research Assistant Demo

**Question:** How can several AI agents with different roles work together on a research task, and where do they go wrong?

**Audience:** CSE students and AI club members

## What I did
- Designed 3 agents: Researcher, Writer, Reviewer
- Ran the 3 roles manually with ChatGPT, Gemini and Claude on the topic "AI agents and multi-agent systems (CrewAI and AutoGen)"
- Compared the result with a single-prompt baseline
- Recorded failures, verified claims against sources, and wrote a reliability checklist
- Made a 6-slide deck and a 10-question quiz with answer key

## Key finding
More agents did not automatically mean more reliability. The Researcher step was strong, but the Writer dropped all sources and the Reviewer added hype instead of catching problems. Core facts stayed correct.

## Repository structure
- `Logs/` run logs (Researcher, Writer, Reviewer, Baseline outputs)
- `docs/` agent design, reliability checklist, failure analysis, verification report, before/after analysis, prompt library, quiz and answer key, ethics
- `slides/` presentation (PDF)
- `src/` demo-level CrewAI code (agents, baseline, automated pipeline). Note: the demo results above come from the manual run; the code is provided for automation and was not used for these logs.

## Setup (for the code)
```
pip install -r requirements.txt
cp .env.example .env
python src/run_pipeline.py "your topic"
```
Add a free Gemini API key in the .env file before running.

## Tools used
ChatGPT, Gemini, Claude, CrewAI (code), Gamma, GitHub

## Ethics
Human review of all outputs, no access to private accounts, agents sandboxed, API keys never committed.
