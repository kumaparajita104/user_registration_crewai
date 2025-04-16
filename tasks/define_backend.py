from crewai import Task

def define_backend_task(agent, api_output, problem_statement):
    return Task(
        description=(
            "Based on the following form interaction and context, explain how the system stores and handles the user's data.\n\n"
            f"Context:\n{problem_statement}\n\n"
            f"Form Interaction Details:\n{api_output}\n\n"
            "Focus Areas:\n"
            "- What kind of data is stored (e.g., 'username', 'email', etc.)\n"
            "- How it is organized, retrieved, and made accessible later\n"
            "- Avoid details like table schemas or security mechanisms"
        ),
        expected_output=(
            "Provide a concise list of bullet points outlining backend storage and data handling. "
            "Highlight key terms using *asterisks* or \"inverted commas\". Keep explanations minimal, no in-depth security or architectural details."
        ),
        agent=agent
    )
