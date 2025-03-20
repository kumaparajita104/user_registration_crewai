from crewai import Agent
from config import OPENAI_API_KEY

def api_spec_agent():
    return Agent(
        name="API Specification Agent",
        role="API Architect",
        goal="Define robust API contracts for user registration.",
        backstory="An expert in RESTful APIs and backend integrations.",
        model="gpt-4",
        api_key=OPENAI_API_KEY
    )
