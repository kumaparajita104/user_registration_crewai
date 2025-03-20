from crewai import Crew
from agents.user_requirements import user_requirements_agent
from agents.ui_ux_design import uiux_design_agent
from agents.api_spec import api_spec_agent
from agents.backend_spec import backend_spec_agent

from tasks.collect_requirements import collect_requirements_task
from tasks.define_ui_ux import define_uiux_task
from tasks.define_api import define_api_task
from tasks.define_backend import define_backend_task

from prd_writer import PRDWriter


class PRDGeneration:
    def __init__(self):
        self.state = {
            "user_req_output": None,
            "uiux_output": None,
            "api_output": None,
            "backend_output": None
        }

    def collect_user_requirements(self):  # sourcery skip: class-extract-method
        print("\n📌 Gathering User Requirements...")
        agent = user_requirements_agent()
        task = collect_requirements_task(agent)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result = crew.kickoff()

        self.state["user_req_output"] = result
        PRDWriter.write_section("User Requirements", result)

    def define_uiux(self):
        print("\n🎨 Defining UI/UX Design...")
        agent = uiux_design_agent()
        task = define_uiux_task(agent, self.state["user_req_output"])
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result = crew.kickoff()

        self.state["uiux_output"] = result
        PRDWriter.write_section("UI/UX Design", result)

    def define_api_spec(self):
        print("\n🔗 Defining API Specification...")
        agent = api_spec_agent()
        task = define_api_task(agent, self.state["uiux_output"])
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result = crew.kickoff()

        self.state["api_output"] = result
        PRDWriter.write_section("API Specification", result)

    def define_backend_architecture(self):
        print("\n🛠️ Defining Backend Architecture...")
        agent = backend_spec_agent()
        task = define_backend_task(agent, self.state["api_output"])
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result = crew.kickoff()

        self.state["backend_output"] = result
        PRDWriter.write_section("Backend Architecture", result)

    def generate_prd(self):
        print("🚀 Starting PRD Generation Process...")
        PRDWriter.clear_document()

        self.collect_user_requirements()
        self.define_uiux()
        self.define_api_spec()
        self.define_backend_architecture()

        print("\n✅ PRD Generation Completed Successfully! Check prd_document.md")


if __name__ == "__main__":
    prd_generator = PRDGeneration()
    prd_generator.generate_prd()
