from crewai import Task

def define_api_task(agent, uiux_output):
    return Task(
        description=(
            "Explain how the registration form sends information to the system:\n"
            "\n- What details are collected from the user"
            
        ),
        expected_output="A simple explanation in points of how the system receives and uses user details.Please dont give huge explanation.Make sure highlight the keywords in inverted commas",
        agent=agent
    )
