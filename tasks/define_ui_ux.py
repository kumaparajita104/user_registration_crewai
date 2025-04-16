from crewai import Task

def define_uiux_task(agent, user_req_output, problem_statement):
    # Ensure that the problem_statement is a valid string
    if not isinstance(problem_statement, str):
        raise ValueError("problem_statement must be a string")

    return Task(
        description=(
            "Using the provided user requirements and problem statement, define a clean and intuitive structure for the user interface (UI) "
            "and user experience (UX) in bullet points.\n"
            "Focus on the following key aspects:\n"
            "- Layout and Grouping of Elements\n- Label and Input Styling\n- Button and Interaction Design\n- Feedback and Error Messages\n- Navigation and Flow\n\n"
            f"User Requirements:\n{user_req_output}\n"
            f"Problem Statement:\n{problem_statement}"
        ),
        expected_output=(
            "A concise bullet-point list outlining the structure, visual styling, and user flow. "
            "No code, detailed explanations, or design tokens included."
        ),
        agent=agent
    )
