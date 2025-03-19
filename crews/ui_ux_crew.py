from crewai import Crew
from agents.ui_ux_design import UIUXDesignAgent
from tasks.define_ui_ux import DefineUIUXTask

class UIUXCrew:
    def create_crew(self):
        uiux_agent = UIUXDesignAgent().create_agent()
        uiux_task = DefineUIUXTask().create_task(uiux_agent)

        return Crew(
            agents=[uiux_agent],
            tasks=[uiux_task],
            verbose=True
        )
