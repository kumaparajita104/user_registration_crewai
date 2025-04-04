from crewai import Task

def define_backend_task(agent, api_output):
    return Task(
        description=(
            "Describe how user registration details are stored and managed but don't give user table structure:\n"
            "\n- What information is saved (e.g., name, age, email)"
            "\n- How the system organizes and retrieves it"
            
        ),
        expected_output="Please give it in points highlighting important key words giving a brief overview of how user data is stored and accessed.Please refrain from giving security insights and lengthy proceses.",
        agent=agent
    )
