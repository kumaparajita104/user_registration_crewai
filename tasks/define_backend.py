from crewai import Task

class DefineBackendTask:
    def create_task(self, agent, api_output):  # Accept api_output
        return Task(
            description=f"Define backend structure for storing and processing user data based on the following API specifications:\n\n{api_output}",
            expected_output="A database schema, backend service details, and API integration strategies.",
            agent=agent
        )
