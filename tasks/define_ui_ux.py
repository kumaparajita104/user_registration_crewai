from crewai import Task

def define_uiux_task(agent, user_req_output):
    return Task(
        description=(
            "Define the **UI/UX structure** for the registration form in a **concise, bullet-point format**. "
            "Keep it **simple, clear, and non-technical**.\n\n"
            "- **Field Arrangement**: How fields are grouped and aligned.\n"
            "- **Label & Input Styling**: Font size, label position, and input appearance.\n"
            "- **Button Design**: Shape, color, and placement.\n"
            "- **Feedback & Validation**: How errors and confirmations appear.\n"
            "- **Cursor & Navigation**: Tab order and hover effects.\n\n"
            "**Avoid exact pixel values and hex codes. Focus on general design choices.**"
        ),
        expected_output=(
            "A structured **non-technical** UI/UX specification using simple terms (e.g., 'Medium font size, Light color')."
        ),
        agent=agent
    )
