from crewai import Agent
from config import OPENAI_API_KEY


def uiux_design_agent():
    return Agent(
        name="UI/UX Design Agent",
        role="UI/UX Designer",
        goal="Define a user-friendly interface for registration.",
        backstory="A specialist in creating intuitive and accessible UI/UX.",
        model="gpt-4",
        api_key=OPENAI_API_KEY
    )

