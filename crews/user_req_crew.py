from crewai import Crew
from agents.user_requirements import UserRequirementsAgent
from tasks.collect_requirements import CollectRequirementsTask

class UserRequirementsCrew:
    def create_crew(self):
        user_req_agent = UserRequirementsAgent().create_agent()
        user_req_task = CollectRequirementsTask().create_task(user_req_agent)

        return Crew(
            agents=[user_req_agent],
            tasks=[user_req_task],
            verbose=True
        )
