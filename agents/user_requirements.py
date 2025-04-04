from crewai import Agent
from config import OPENAI_API_KEY

def user_requirements_agent():
    return Agent(
        name="User Requirements Agent",
        role="Requirement Analyst",
        goal="Define only the essential input fields for user registration.",
        backstory="Specialist in streamlining form fields to improve user experience.",
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,  # Ensures structured, non-detailed responses
        max_tokens=200  # Limits verbosity
    )
