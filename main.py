from crewai import Crew
from agents.user_requirements import UserRequirementsAgent
from agents.ui_ux_design import UIUXDesignAgent
from agents.api_spec import APISpecAgent
from agents.backend_spec import BackendSpecAgent

from tasks.collect_requirements import CollectRequirementsTask
from tasks.define_ui_ux import DefineUIUXTask
from tasks.define_api import DefineAPITask
from tasks.define_backend import DefineBackendTask

from prd_writer import PRDWriter

if __name__ == "__main__":
    print("🚀 Starting PRD Generation Process...")

    # Clear PRD File
    PRDWriter.clear_document()

    ## 1️⃣ USER REQUIREMENTS CREW
    print("\n📌 Gathering User Requirements...")
    user_req_agent = UserRequirementsAgent().create_agent()
    user_req_task = CollectRequirementsTask().create_task(user_req_agent)

    user_req_crew = Crew(agents=[user_req_agent], tasks=[user_req_task], verbose=True)
    user_req_output = user_req_crew.kickoff()

    PRDWriter.write_section("User Requirements", user_req_output)

    ## 2️⃣ UI/UX DESIGN CREW (Uses User Requirements Output)
    print("\n🎨 Defining UI/UX Design...")
    uiux_agent = UIUXDesignAgent().create_agent()
    uiux_task = DefineUIUXTask().create_task(uiux_agent, user_req_output)  # Pass output

    uiux_crew = Crew(agents=[uiux_agent], tasks=[uiux_task], verbose=True)
    uiux_output = uiux_crew.kickoff()

    PRDWriter.write_section("UI/UX Design", uiux_output)

    ## 3️⃣ API SPECIFICATION CREW (Uses UI/UX Output)
    print("\n🔗 Defining API Specification...")
    api_agent = APISpecAgent().create_agent()
    api_task = DefineAPITask().create_task(api_agent, uiux_output)  # Pass output

    api_crew = Crew(agents=[api_agent], tasks=[api_task], verbose=True)
    api_output = api_crew.kickoff()

    PRDWriter.write_section("API Specification", api_output)

    ## 4️⃣ BACKEND ARCHITECTURE CREW (Uses API Output)
    print("\n🛠️ Defining Backend Architecture...")
    backend_agent = BackendSpecAgent().create_agent()
    backend_task = DefineBackendTask().create_task(backend_agent, api_output)  # Pass output

    backend_crew = Crew(agents=[backend_agent], tasks=[backend_task], verbose=True)
    backend_output = backend_crew.kickoff()

    PRDWriter.write_section("Backend Architecture", backend_output)

    print("\n✅ PRD Generation Completed Successfully! Check prd_document.md")
