"""3 agents (Researcher, Writer, Reviewer) using CrewAI."""
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(model="gemini/gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY"))

def build_crew(topic: str) -> Crew:
    researcher = Agent(
        role="Researcher",
        goal=f"Collect accurate key facts about: {topic}",
        backstory="Careful analyst. Never invents facts. Marks anything uncertain as 'UNVERIFIED'.",
        llm=llm, allow_delegation=False, verbose=True,
    )
    writer = Agent(
        role="Writer",
        goal="Write a clear 300-word summary for CSE students using ONLY the researcher's notes.",
        backstory="Technical writer who explains simply and does not add new claims.",
        llm=llm, allow_delegation=False, verbose=True,
    )
    reviewer = Agent(
        role="Reviewer",
        goal="Find wrong, unsupported or outdated claims and unsafe advice in the draft.",
        backstory="Strict fact-checker. Lists each issue, then gives a corrected final version.",
        llm=llm, allow_delegation=False, verbose=True,
    )

    t1 = Task(description=f"Research '{topic}'. Give 8 bullet facts with source names.",
              expected_output="8 bullet facts + sources", agent=researcher)
    t2 = Task(description="Write a 300-word summary from the notes.",
              expected_output="300-word summary", agent=writer, context=[t1])
    t3 = Task(description="Review the draft. List issues, then give the corrected final text.",
              expected_output="Issue list + corrected final text", agent=reviewer, context=[t2])

    return Crew(agents=[researcher, writer, reviewer], tasks=[t1, t2, t3],
                process=Process.sequential, verbose=True)
