# Failure Analysis

Topic: AI Agents and Multi-Agent Systems (CrewAI and AutoGen)
Method: Manual simulation of 3 roles (Researcher, Writer, Reviewer) plus a single-prompt baseline.

| # | Agent | Failure type | What happened | Suggested fix |
|---|---|---|---|---|
| 1 | Researcher | Formatting / tool noise | Output contained stray citation fragments (broken characters, repeated names such as "IBM Research", "CrewAI Documentation"). | Ask for plain text with sources as a clean list. |
| 2 | Researcher | Weak source mapping | One survey (Yehudai et al., "A Survey on Evaluation of LLM-based Agents") was cited for claims 1, 7 and 8. Its attribution (IBM Research, ACL 2026) is correct, but it is an evaluation survey, so it may not directly support claim 7 about multi-agent challenges. | Cite a multi-agent source for claim 7 and verify manually. |
| 3 | Writer | Omission (lost sources) | All source names from the Researcher were dropped, so readers cannot verify any claim. | Add rule: "Keep source names in brackets after each claim." |
| 4 | Writer | Minor scope creep | Added unsupported opinions: "important topics in computer science", "understanding ... is essential". | Rule: "Add no opinions or importance claims." |
| 5 | Writer | Lost caveats | The Researcher's UNVERIFIED flags and research date were not carried forward. | Carry UNVERIFIED flags into the draft. |
| 6 | Reviewer | Rubber-stamping / over-polishing | Did not catch the missing sources. Instead it strengthened wording: "important" became "critical", "abstractions" became "powerful abstractions", "can increase" became "often increases", "depends" became "depends heavily", "attention needed" became "equally vital". | Reviewer prompt must forbid style changes and require an issue list with evidence. |
| 7 | Reviewer | New unsupported claim | Added "essential for navigating modern software engineering and artificial intelligence", which is not in any source. | Reviewer may only delete or flag, never add claims. |
| 8 | Reviewer | Weaker attribution | "Microsoft's official GitHub repository" became "official repository guidelines". | Keep the original attributions. |
| 9 | Baseline | Vague sources | Gave only generic sources ("CrewAI Documentation", "Microsoft Research & GitHub"), with no paper titles or links. | Ask for specific URLs. |
| 10 | Baseline | Hype and unverified specifics | "Foundational shift", "maintain contextual memory", "AutoGen v0.4 asynchronous actor architecture" and "token usage, latency" are not supported by any cited source in the output. | Verify each manually. |
| 11 | Baseline | Formatting glitch | Two sections ran together ("refinement.Key Frameworks"). | Minor. |

Not observed in this run: infinite loops, or unsafe advice. (Loops are less likely in a manual simulation, where the human controls each step.)
Note: No major hallucination was found in the core facts. The main weakness was the pipeline degrading quality, not inventing facts.
