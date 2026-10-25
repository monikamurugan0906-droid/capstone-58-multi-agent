"""Single-prompt baseline, used for the before/after comparison."""
from agents import llm

def run_baseline(topic: str) -> str:
    prompt = f"Write a 300-word research summary on '{topic}' for CSE students. Mention sources."
    return llm.call(prompt)
