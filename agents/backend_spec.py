from crewai import Agent
from config import OPENAI_API_KEY

class BackendSpecAgent:
    def create_agent(self):
        return Agent(
            name="Backend Specification Agent",
            role="Backend Engineer",
            goal="Design backend architecture for user registration.",
            backstory="An expert in databases mysql,and scalability with no bcrypt encryption of passwords.",
            lmodel="gpt-4",
            api_key=OPENAI_API_KEY
        )
