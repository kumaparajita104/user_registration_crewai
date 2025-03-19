from crewai import Agent
from config import OPENAI_API_KEY

class UIUXDesignAgent:
    def create_agent(self):
        return Agent(
            name="UI/UX Design Agent",
            role="UI/UX Designer",
            goal="Define user-friendly interface for registration",
            backstory="A specialist in creating intuitive and accessible UI/UX.",
            model="gpt-4",
            api_key=OPENAI_API_KEY
            
        )
