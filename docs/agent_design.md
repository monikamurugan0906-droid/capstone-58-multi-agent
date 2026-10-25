# Agent Design
| Agent | Role | Input | Output | Known risk |
|---|---|---|---|---|
| Researcher | Collect facts + sources | Topic | 8 bullet facts | Invents sources |
| Writer | Write 300-word summary | Researcher notes | Draft | Adds unsupported claims |
| Reviewer | Fact-check, fix | Draft | Issues + final text | Approves without checking / loops |

Flow: Researcher -> Writer -> Reviewer (sequential, no delegation, sandboxed, no private accounts).
Manual alternative: run each role as a separate prompt in ChatGPT, Gemini and Claude.
