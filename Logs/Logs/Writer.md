writer output 
AI Agents and Multi-Agent Systems: CrewAI and AutoGen

AI agents and multi-agent systems are important topics in computer science. AI agents use Large Language Models (LLMs) to reason about tasks, plan steps, interact with tools, and perform actions toward a goal. Their capabilities depend on the model, available tools, and system design.

A multi-agent system consists of multiple agents that cooperate to solve tasks. Each agent can have a different role and exchange information with other agents to achieve a shared objective. This approach allows complex tasks to be divided into smaller activities, such as research, analysis, writing, and verification. Depending on the system design, these activities can support parallel work and cross-checking.

CrewAI is an open-source framework for creating teams of AI agents. Developers can assign specific roles, goals, tools, and tasks to individual agents. CrewAI provides two important concepts: Crews and Flows. Crews organize collaborative agents, while Flows control workflow execution. Flows can manage application state, conditional steps, and event-driven execution.

AutoGen is another framework for developing applications involving multiple collaborating AI agents. Its AgentChat API supports different team conversation patterns, including round-robin conversations and model-selected speakers. However, Microsoft's official GitHub repository states that AutoGen is in maintenance mode and recommends that new users consider Microsoft Agent Framework.

Despite their advantages, multi-agent systems face several challenges. Agents may produce inconsistent results, repeat work, propagate errors, or experience coordination difficulties. Adding more agents can also increase processing time and computational costs. Therefore, multi-agent systems do not always outperform single-agent systems. Their performance depends on the task, models, coordination, and evaluation methods.

Evaluating AI agents requires more than checking their final answers. Important evaluation factors include task success, planning, tool use, robustness, safety, and cost-efficiency. Multi-agent systems also require evaluating coordination and communication.

In conclusion, AI agents and multi-agent frameworks provide ways to organize automated tasks. For CSE students, understanding their architecture, collaboration mechanisms, limitations, and evaluation methods is essential when studying these technologies.
