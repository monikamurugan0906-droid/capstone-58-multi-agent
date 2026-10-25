# Before / After Analysis

Before = single prompt (Baseline). After = Researcher, Writer, Reviewer pipeline.

| Criteria | Single prompt (Baseline) | Multi-agent (Final Reviewer output) |
|---|---|---|
| Specific sources | Generic ("CrewAI docs", "Microsoft Research & GitHub") | Researcher step gave specific papers and docs, but they were lost in the final text |
| Sources in final text | Yes (Key Sources section, but vague) | No |
| Core facts correct | Mostly yes | Yes |
| Hype / unsupported wording | "Foundational shift", "maintain contextual memory" | "Critical area", "powerful abstractions", "often increases", "essential for navigating modern software engineering and AI" |
| Caveats (multi-agent not always better) | Not mentioned | Included |
| Attribution detail | Better (Microsoft Research, v0.4 mentioned, unverified) | Weaker ("official repository guidelines") |
| Extra effort | 1 prompt | 3 prompts plus copy-paste |
| Format | Short, structured with headings | Plain paragraphs |

## Conclusion
- The multi-agent pipeline did not clearly beat the single prompt in this run.
- Its strongest part was the Researcher step: specific sources, UNVERIFIED flags and the caveat that multi-agent is not always better.
- It then degraded: the Writer dropped the sources and the Reviewer added hype instead of catching problems.
- The baseline was faster and had useful structure, but its sources were vague and some claims are unsupported.
- Lesson: more agents do not automatically mean more reliability. Each agent needs strict rules, for example "keep sources", "never add claims", and a human must verify the final output.
