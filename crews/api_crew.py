from crewai import Crew
from agents.api_spec import APISpecAgent
from tasks.define_api import DefineAPITask

class APICrew:
    def create_crew(self):
        api_agent = APISpecAgent().create_agent()
        api_task = DefineAPITask().create_task(api_agent)

        return Crew(
            agents=[api_agent],
            tasks=[api_task],
            verbose=True
        )
