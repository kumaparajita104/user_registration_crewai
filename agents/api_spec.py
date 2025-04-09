from crewai import Agent
from config import OPENAI_API_KEY

def api_spec_agent():
    return Agent(
        name="API Specification Agent",
        role="API Architect",
        goal="Map UI fields to API attributes for user registration and login. Do not add any kind of token-based authentication (JWT, OAuth, etc.). Keep it simple.",
        backstory="Specialist in defining API specs for forms like registration and login. The focus is on sending and receiving data, not on validating security or tokens.",
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=200
    )
