from crewai import Task

def collect_requirements_task(agent, problem_statement: str):
    return Task(
        description=(
            f"Based on the following problem statement, identify and list the essential user input fields required to fulfill the goal:\n\n"
            f"\"\"\"\n{problem_statement}\n\"\"\"\n\n"
            "- Field Name\n"
            "- Type (Alphanumeric, Numeric, Date, etc.)\n"
            "- Mandatory (Yes/No)\n"
            "- Purpose (Clear and concise definition of the field’s use)"
        ),
        expected_output=(
            "A clean markdown table listing **only the necessary fields** with their attributes. "
            "Do not include explanations, headers, or any extra content. Only the table in the specified format."
        ),
        agent=agent
    )
