from crewai import Agent
from config import OPENAI_API_KEY

def api_spec_agent(problem_statement: str, fields_description: str):
    return Agent(
        name="API Specification Agent",
        role="Product API Analyst",
        goal=(
            "Describe how the information from the user registration form is passed to the system for processing. "
            "Avoid mentioning specific endpoints, HTTP methods, or code. Keep the explanation user-focused and conceptual."
        ),
        backstory=(
            "A specialist in outlining how data flows from the UI to the backend in human-readable terms. "
            "Your job is to describe how the data entered by users is interpreted and handled, without diving into technical implementation details like API routes or protocols."
        ),
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=200,
        inputs={
            "problem_statement": problem_statement,
            "fields_description": fields_description
        }
    )
