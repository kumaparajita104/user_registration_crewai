from crewai import Task

def define_uiux_task(agent, user_req_output):
    return Task(
        description=(
            "Based on the fields below, define a clean and non-technical UI/UX structure in bullet points.\n"
            "Use simple terms for:\n"
            "- Field Grouping\n- Label & Input Styling\n- Button Design\n- Feedback Messages\n- Navigation Order\n\n"
            f"User Fields:\n{user_req_output}"
        ),
        expected_output=(
            "A concise bullet-point list describing layout, styling and flow. No UI code, no explanations, no design tokens."
        ),
        agent=agent
    )
