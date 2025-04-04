from crewai import Task

def collect_requirements_task(agent):
    return Task(
        description=(
            "List the required fields for user registration, specifying:\n"
            "- Field Name\n"
            "- Type (Numeric, Alphanumeric, etc.)\n"
            "- Mandatory (Yes/No)\n"
            "- One-line purpose definition"
        ),
        expected_output=(
            "A structured table listing only necessary fields with attributes."
        ),
        agent=agent
    )
