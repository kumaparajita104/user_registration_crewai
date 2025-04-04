from crewai import Agent
from config import OPENAI_API_KEY

def backend_spec_agent():
    return Agent(
        name="Backend Specification Agent",
        role="Backend Engineer",
        goal="Define how user registration data is stored and processed.",
        backstory="An expert in database structures, ensuring efficient storage of form inputs.",
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=200
    )
