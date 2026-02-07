# agents.py
import os
from crewai import Agent
from crewai.llm import LLM

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


work_agent = Agent(
    role="Work Analyzer",
    goal="Analyze today's technical work",
    backstory="Expert software activity analyzer",
    llm=llm
)

planner_agent = Agent(
    role="Task Planner",
    goal="Plan realistic tasks for tomorrow",
    backstory="Agile productivity planner",
    llm=llm
)


