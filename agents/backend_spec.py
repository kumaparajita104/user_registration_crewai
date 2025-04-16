from crewai import Agent
from config import OPENAI_API_KEY

def backend_spec_agent(problem_statement: str):
    return Agent(
        name="Backend Specification Agent",
        role="Backend Engineer",
        goal=(
            "Define how the user registration data is stored and processed in the backend system. "
            "Focus on how the data is structured, saved in a database, and how it is used later for user access and management."
        ),
        backstory=(
            "An expert in database design and backend systems. Specializes in defining storage solutions for form data and ensuring "
            "that data is processed efficiently and securely in backend systems."
        ),
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=200,
        inputs={
            "problem_statement": problem_statement  # Pass the problem statement dynamically
        }
    )
