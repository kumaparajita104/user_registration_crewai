from crewai import Agent
from config import OPENAI_API_KEY

def api_spec_agent():
    return Agent(
        name="API Specification Agent",
        role="API Architect",
        goal="Map UI fields to API attributes with correct field types.",
        backstory="Specialist in structuring form data for smooth backend integration in simple english nothing technical.",
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=200
    )
