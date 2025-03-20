from crewai import Agent
from config import OPENAI_API_KEY

def backend_spec_agent():
    return Agent(
        name="Backend Specification Agent",
        role="Backend Engineer",
        goal="Design backend architecture for user registration.",
        backstory="An expert in databases (MySQL) and scalability, with no bcrypt encryption of passwords.",
        model="gpt-4",  # Fixed the typo (was 'lmodel')
        api_key=OPENAI_API_KEY
    )
