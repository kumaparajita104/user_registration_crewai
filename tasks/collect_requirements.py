from crewai import Task

class CollectRequirementsTask:
    def create_task(self, agent):
        return Task(
            description="Gather user requirements for registration flow.",
            expected_output="A document outlining key user requirements.",
            agent=agent
        )
