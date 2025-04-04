from crewai import Agent
from config import OPENAI_API_KEY

def uiux_design_agent():
    return Agent(
        name="UI/UX Design Agent",
        role="UI/UX Strategist",
        goal="Define a structured and concise UI/UX design for the registration form.",
        backstory="Expert in crafting intuitive and visually appealing user interfaces with a focus on clarity and usability.",
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=300  # Adjusted for concise yet complete responses
    )
