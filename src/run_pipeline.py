"""Automation step: runs the multi-agent crew + baseline and saves timestamped logs."""
import sys, datetime, pathlib
from agents import build_crew
from baseline import run_baseline

topic = " ".join(sys.argv[1:]) or "Multi-agent AI systems: CrewAI and AutoGen"
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logs = pathlib.Path(__file__).parent.parent / "logs"
logs.mkdir(exist_ok=True)

print("== Baseline (single prompt) ==")
base = run_baseline(topic)
(logs / f"{stamp}_baseline.md").write_text(f"# Baseline\nTopic: {topic}\n\n{base}", encoding="utf-8")

print("== Multi-agent run ==")
result = build_crew(topic).kickoff()
(logs / f"{stamp}_multiagent.md").write_text(f"# Multi-agent\nTopic: {topic}\n\n{result}", encoding="utf-8")

print(f"Done. Logs saved in logs/ ({stamp}). Now record failures in docs/failure_analysis.md")
