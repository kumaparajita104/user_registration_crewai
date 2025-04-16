from crewai import Agent
from config import OPENAI_API_KEY

def uiux_design_agent(problem_statement: str):
    return Agent(
        name="UI/UX Design Agent",
        role="UI/UX Strategist",
        goal=(
            f"Design a structured, clean, and user-friendly interface for the following product:\n\n"
            f"{problem_statement}\n\n"
            "Focus on layout, field arrangement, labeling, button design, and feedback messages in a concise and readable format. "
            "Avoid exact pixel values or technical design jargon. Output should help developers visualize the form layout easily."
        ),
        backstory=(
            "An expert in crafting simple, elegant user interfaces focused on clarity, user accessibility, and intuitive workflows. "
            "You specialize in turning requirements into user-friendly UI design specs that are easy for frontend teams to follow."
        ),
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=300
    )
