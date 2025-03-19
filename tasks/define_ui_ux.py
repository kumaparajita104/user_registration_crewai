from crewai import Task

class DefineUIUXTask:
    def create_task(self, agent, user_req_output):  # Accept user_req_output
        return Task(
            description=f"Design a simple and intuitive UI/UX for registration based on the following user requirements:\n\n{user_req_output}",
            expected_output="Wireframes, user flow diagrams, and UX principles document.",
            agent=agent
        )
