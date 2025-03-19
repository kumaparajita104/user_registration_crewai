from crewai import Crew
from agents.backend_spec import BackendSpecAgent
from tasks.define_backend import DefineBackendTask

class BackendCrew:
    def create_crew(self):
        backend_agent = BackendSpecAgent().create_agent()
        backend_task = DefineBackendTask().create_task(backend_agent)

        return Crew(
            agents=[backend_agent],
            tasks=[backend_task],
            verbose=True
        )
