baseline output 
Research Summary: AI Agents and Multi-Agent Systems
AI agents and multi-agent systems represent a foundational shift in computer science, moving software engineering from single-prompt interactions toward autonomous, collaborative workflows. AI agents use Large Language Models (LLMs) to reason through tasks, maintain contextual memory, execute tool calls, and complete goal-driven operations.  
When complex tasks exceed single-agent capabilities, multi-agent frameworks distribute responsibilities across specialized roles, enabling parallel task execution and iterative refinement.Key Frameworks
​CrewAI: A Python framework centered on role-based team collaboration. It structures operations around Crews (collaborative agent clusters) and Flows (event-driven execution, state tracking, and conditional branching).
​AutoGen: Developed by Microsoft Research, AutoGen utilizes an asynchronous, event-driven actor architecture. Its AgentChat API supports multi-agent conversation patterns like round-robin and model-selected routing. Official repositories note that AutoGen is in maintenance mode, guiding developers toward the Microsoft Agent Framework.
​Engineering Trade-offs & Evaluation
​For Computer Science and Engineering (CSE) students, multi-agent systems involve key trade-offs:
​Coordination Overhead: Additional agents increase token usage, execution latency, and error propagation.
​Evaluation Metrics: Evaluation requires auditing task completion, tool call accuracy, planning correctness, safety guardrails, and cost efficiency.
​Key Sources
​CrewAI Documentation & Framework Guides: Overview of role-based designs, tasks, and flow control mechanisms.
​Microsoft Research & GitHub Repository (microsoft/autogen): Specifications for AutoGen v0.4, event-driven architecture, and repository maintenance notices.
