from crewai import Task

def define_backend_task(agent, api_output):  # Accept agent and API output
    return Task(
        description=f"Define backend structure for storing and processing user data based on the following API specifications:\n\n{api_output}",
        expected_output="A database schema, backend service details, and API integration strategies.",
        agent=agent
    )
