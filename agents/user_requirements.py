from crewai import Agent
from config import OPENAI_API_KEY

def user_requirements_agent():  # ✅ Added parentheses
    return Agent(
        name="User Requirements Agent",
        role="Requirement Analyst",
        goal="Gather and define user registration requirements, focusing only on essential fields.",
        backstory="An expert in requirement gathering, ensuring a streamlined and efficient registration process.",
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        task_description=(
            "Identify the necessary fields for a simple user registration form, ensuring ease of use. "
            "The form should include fields such as name, age, and address, without login, password recovery, or captcha recovery."
        )
    )
