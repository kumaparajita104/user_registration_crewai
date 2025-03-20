from crewai import Task

def define_api_task(agent, uiux_output):  # Function instead of class method
    return Task(
        description=f"Design API specifications for user registration based on the following UI/UX design:\n\n{uiux_output}",
        expected_output="A RESTful API contract detailing endpoints, request/response formats, and authentication mechanisms.",
        agent=agent
    )
