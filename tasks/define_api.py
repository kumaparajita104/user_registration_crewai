from crewai import Task

class DefineAPITask:
    def create_task(self, agent, uiux_output):  # Accept uiux_output
        return Task(
            description=f"Design API specifications for user registration based on the following UI/UX design:\n\n{uiux_output}",
            expected_output="A RESTful API contract detailing endpoints, request/response formats, and authentication mechanisms.",
            agent=agent
        )
