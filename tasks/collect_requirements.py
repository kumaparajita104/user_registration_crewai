from crewai import Task
from agents.user_requirements import user_requirements_agent  # Import the function

def collect_requirements_task(agent):  # Accepts agent as an argument
    return Task(
        description="Gather user requirements for the user registration flow.",
        expected_output="A document outlining key user requirements.",
        agent=agent  # Correctly assigns the instantiated agent
    )
