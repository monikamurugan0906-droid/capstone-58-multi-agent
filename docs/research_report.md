# Research Report: Multi-Agent Research Assistant Demo

**Project question:** How can several AI agents with different roles work together on a research task, and where do they go wrong?
**Audience:** CSE students and AI club members
**Date:** 25 October 2026

## 1. Background
AI agents use large language models (LLMs) to reason about tasks, plan steps, use tools and act toward a goal. A multi-agent system uses several agents with different roles that exchange information to reach a shared objective. Two well-known open-source frameworks are CrewAI and AutoGen.

- **CrewAI:** agents get roles, goals, tools and tasks. It organises collaborating agents as Crews and controls workflows (state, conditional steps, event-driven execution) with Flows.
- **AutoGen:** its AgentChat API supports multi-agent conversation patterns such as round-robin and model-selected speakers. According to the official GitHub README, AutoGen is now in maintenance mode and new users are directed to Microsoft Agent Framework.

## 2. Method
1. Designed 3 agents: **Researcher** (collects facts with sources), **Writer** (300-word summary using only the notes), **Reviewer** (fact-checks and corrects).
2. Ran the three roles manually with ChatGPT, Gemini and Claude on the topic "AI agents and multi-agent systems (CrewAI and AutoGen)".
3. Ran the same task as a single prompt (baseline) for comparison.
4. Recorded failures, and checked key claims against official documentation and the papers cited.
5. Demo-level CrewAI code is included in `src/` for automation but was not used for the logs above.

## 3. Findings
**What worked**
- The Researcher produced specific facts with named sources and flagged uncertain items as UNVERIFIED.
- The core facts stayed correct through all three steps.
- The key caution survived: multi-agent systems do not always outperform single agents.

**Where the pipeline went wrong**
- The Writer dropped every source name, so readers could not verify claims.
- The Reviewer did not catch this. It polished wording and added emphasis ("critical", "powerful", "often", "heavily"), plus one new unsupported claim, and weakened an attribution.
- One survey was cited for several claims, and one of them (multi-agent challenges) may not be directly supported by an evaluation survey.
- Researcher output contained stray citation fragments (formatting noise).

**Comparison with a single prompt**
The baseline was faster and had useful structure, but its sources were vague and some specifics (such as AutoGen's actor architecture) were not backed by a cited source. The multi-agent pipeline did not clearly beat it. Its research step was stronger, but quality dropped at the Writer and Reviewer steps.

## 4. Verification summary
Verified manually: AutoGen maintenance-mode status (official README), CrewAI Crews and Flows, AutoGen AgentChat team patterns, existence of both cited surveys. The evaluation survey is by Yehudai et al. (IBM Research and others), arXiv 2025, Findings of ACL 2026. Details are in `docs/verification_report.md`.

## 5. Conclusion
More agents do not automatically mean more reliability. Reliability comes from controls: each agent needs strict rules (keep sources, never add claims, a Reviewer that flags rather than rewrites), and a human must review the final output.

## 6. Sources
- AutoGen repository README: github.com/microsoft/autogen
- CrewAI documentation: docs.crewai.com
- AutoGen AgentChat guide: microsoft.github.io/autogen
- Yehudai et al., "Survey on Evaluation of LLM-based Agents": arxiv.org/abs/2503.16416
- "Large Language Model Based Multi-agents: A Survey of Progress and Challenges", IJCAI 2024

## 7. Ethics
Human review of all outputs, no access to private accounts, agents sandboxed, API keys never committed. AI tools were used to produce and review drafts, and all claims in this report were checked by the author.
