from crewai import Task

def define_api_task(agent, fields_description: str, problem_statement: str):
    return Task(
        description=(
            f"Using the following problem statement and description of form fields, explain how the user-submitted data is passed from the form to the system for processing:\n"
            f"\nProblem Statement:\n{problem_statement}\n"
            f"\nFields Description:\n{fields_description}"
        ),
        expected_output=(
            "A clear, bullet-point explanation of how data entered in the form is received and interpreted by the system. "
            "Keep it simple, avoid technical details such as API endpoints or HTTP methods. Highlight important keywords in inverted commas (e.g., 'email', 'password')."
        ),
        agent=agent
    )
