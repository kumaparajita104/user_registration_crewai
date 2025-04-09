#!/usr/bin/env python
from crewai import Crew
from crewai.flow import Flow, start, listen
from pydantic import BaseModel
from typing import Optional

from agents.user_requirements import user_requirements_agent
from agents.ui_ux_design import uiux_design_agent
from agents.api_spec import api_spec_agent
from agents.backend_spec import backend_spec_agent

from tasks.collect_requirements import collect_requirements_task
from tasks.define_ui_ux import define_uiux_task
from tasks.define_api import define_api_task
from tasks.define_backend import define_backend_task

from prd_writer import PRDWriter
from utils.stability_checker import run_with_stability_check


class PRDState(BaseModel):
    user_req_output: Optional[str] = None
    uiux_output: Optional[str] = None
    api_output: Optional[str] = None
    backend_output: Optional[str] = None


class PRDFlow(Flow[PRDState]):

    @start()
    def initialize(self):
        print("🚀 Starting PRD Generation Process...")
        PRDWriter.clear_document()

    @listen(initialize)
    def gather_user_requirements(self):
        print("\n📌 Gathering User Requirements...")
        agent = user_requirements_agent()
        task = collect_requirements_task(agent)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result, confidence = run_with_stability_check(crew)
        self.state.user_req_output = result
        PRDWriter.write_section("User Requirements", result)
        print(f"🧪 Confidence Score: {confidence}%")

    @listen(gather_user_requirements)
    def define_uiux(self):
        print("\n🎨 Defining UI/UX Design...")
        agent = uiux_design_agent()
        task = define_uiux_task(agent, self.state.user_req_output)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result, confidence = run_with_stability_check(crew)
        self.state.uiux_output = result
        PRDWriter.write_section("UI/UX Design", result)
        print(f"🧪 Confidence Score: {confidence}%")

    @listen(define_uiux)
    def define_api_spec(self):
        print("\n🔗 Defining API Specification...")
        agent = api_spec_agent()
        task = define_api_task(agent, self.state.uiux_output)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result, confidence = run_with_stability_check(crew)
        self.state.api_output = result
        PRDWriter.write_section("API Specification", result)
        print(f"🧪 Confidence Score: {confidence}%")

    @listen(define_api_spec)
    def define_backend(self):
        print("\n🛠️ Defining Backend Architecture...")
        agent = backend_spec_agent()
        task = define_backend_task(agent, self.state.api_output)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result, confidence = run_with_stability_check(crew)
        self.state.backend_output = result
        PRDWriter.write_section("Backend Architecture", result)
        print(f"🧪 Confidence Score: {confidence}%")

    @listen(define_backend)
    def complete(self):
        print("\n✅ PRD Generation Completed Successfully! Check prd_document.md")


def kickoff():
    flow = PRDFlow()
    flow.kickoff()


def plot():
    flow = PRDFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
