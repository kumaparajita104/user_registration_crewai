#!/usr/bin/env python
from crewai import Crew
from crewai.flow import Flow, start, listen
from pydantic import BaseModel
from typing import Optional
import os
from datetime import datetime

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
    problem_statement: Optional[str] = None

    user_req_confidence: Optional[float] = None
    uiux_confidence: Optional[float] = None
    api_confidence: Optional[float] = None
    backend_confidence: Optional[float] = None


class PRDFlow(Flow[PRDState]):

    @start()
    def initialize(self):
        self.state.problem_statement = (
            "Design a user registration portal with a simple form where a user enters only the necessary details to create an account. "
            "The form should be intuitive, minimal, and focused on collecting only essential information for account creation."
        )
        print("🚀 Starting PRD Generation Process...")
        PRDWriter.clear_document()

    @listen(initialize)
    def gather_user_requirements(self):
        print("\n📌 Gathering User Requirements...")
        agent = user_requirements_agent(self.state.problem_statement)
        task = collect_requirements_task(agent, self.state.problem_statement)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result, confidence = run_with_stability_check(crew)
        self.state.user_req_output = result
        self.state.user_req_confidence = confidence
        output_file = write_agent_output("User_Requirements", result, confidence)
        print(f"📝 Output saved to: {output_file}")
        PRDWriter.write_section("User Requirements", result)
        print(f"🧪 Confidence Score: {confidence}%")

    @listen(gather_user_requirements)
    def define_uiux(self):
        print("\n🎨 Defining UI/UX Design...")
        agent = uiux_design_agent(self.state.problem_statement)
        task = define_uiux_task(agent, self.state.user_req_output, self.state.problem_statement)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result, confidence = run_with_stability_check(crew)
        self.state.uiux_output = result
        self.state.uiux_confidence = confidence
        output_file = write_agent_output("UI_UX_Design", result, confidence)
        print(f"📝 Output saved to: {output_file}")
        PRDWriter.write_section("UI/UX Design", result)
        print(f"🧪 Confidence Score: {confidence}%")

    @listen(define_uiux)
    def define_api_spec(self):
        print("\n🔗 Defining API Specification...")
        agent = api_spec_agent(self.state.problem_statement, self.state.uiux_output)
        task = define_api_task(agent, self.state.uiux_output, self.state.problem_statement)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result, confidence = run_with_stability_check(crew)
        self.state.api_output = result
        self.state.api_confidence = confidence
        output_file = write_agent_output("API_Specification", result, confidence)
        print(f"📝 Output saved to: {output_file}")
        PRDWriter.write_section("API Specification", result)
        print(f"🧪 Confidence Score: {confidence}%")

    @listen(define_api_spec)
    def define_backend(self):
        print("\n🛠️ Defining Backend Architecture...")
        agent = backend_spec_agent(self.state.problem_statement)
        task = define_backend_task(agent, self.state.api_output, self.state.problem_statement)
        crew = Crew(agents=[agent], tasks=[task], verbose=True)
        result, confidence = run_with_stability_check(crew)
        self.state.backend_output = result
        self.state.backend_confidence = confidence
        output_file = write_agent_output("Backend_Architecture", result, confidence)
        print(f"📝 Output saved to: {output_file}")
        PRDWriter.write_section("Backend Architecture", result)
        print(f"🧪 Confidence Score: {confidence}%")

    @listen(define_backend)
    def complete(self):
        print("\n✅ PRD Generation Completed Successfully! Check prd_document.md")

        # Print detailed confidence report
        print("\n📊 PRD Stability Report:")
        print(f"- User Requirements Confidence: {self.state.user_req_confidence}%")
        print(f"- UI/UX Design Confidence: {self.state.uiux_confidence}%")
        print(f"- API Specification Confidence: {self.state.api_confidence}%")
        print(f"- Backend Architecture Confidence: {self.state.backend_confidence}%")

        confidences = [
            self.state.user_req_confidence,
            self.state.uiux_confidence,
            self.state.api_confidence,
            self.state.backend_confidence,
        ]
        avg_confidence = round(sum(confidences) / len(confidences), 2)
        print(f"\n🧠 Overall PRD Stability Score: {avg_confidence}%")

        # Log confidence scores to PRD document
        PRDWriter.write_section("Confidence Scores", f"""
        - User Requirements: {self.state.user_req_confidence}%
        - UI/UX Design: {self.state.uiux_confidence}%
        - API Specification: {self.state.api_confidence}%
        - Backend Architecture: {self.state.backend_confidence}%
        - Overall Stability: {avg_confidence}%
        """)


def write_agent_output(agent_name: str, output: str, confidence: float):
    """Write agent output to a separate file with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/{agent_name}_{timestamp}.md"
    
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)
    
    with open(filename, "w") as f:
        f.write(f"# {agent_name} Output\n\n")
        f.write(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Confidence Score: {confidence}%\n\n")
        f.write("## Output\n\n")
        f.write(output)
    
    return filename


def kickoff():
    flow = PRDFlow()
    flow.kickoff()


def plot():
    flow = PRDFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
