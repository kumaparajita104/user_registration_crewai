from crewai import Agent
from config import OPENAI_API_KEY

def user_requirements_agent(problem_statement: str):
    return Agent(
        name="User Requirements Agent",
        role="Requirement Analyst",
        goal="Identify the essential user input fields based on the problem statement.",
        backstory=(
            "You are an expert in designing forms that collect only the most essential and relevant data from users. "
            "Your task is to streamline the user registration or input process by identifying the core fields necessary to fulfill the goals described in the problem statement. "
            "Avoid collecting redundant information or unnecessary details. Focus on clarity, simplicity, and purpose."
        ),
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
        max_tokens=300,
        context=f"""
You are tasked with helping define a user input form based on the following problem statement:

\"\"\"{problem_statement}\"\"\"

Please provide **only the essential input fields** needed to achieve the goal described. The output should be in the form of a markdown table. For each field, include:

- **Field Name**: A concise name for the input field.
- **Type**: The type of data that should be entered (e.g., String, Date, Numeric, Alphanumeric).
- **Mandatory**: Whether the field is mandatory or optional (Yes/No).
- **Purpose**: A clear and concise one-line definition of why this field is needed.

**Important Instructions:**
- Do **not** include explanations, clarifications, or extra context.
- The table should only include fields that are essential for the user to provide, based on the goal of the problem statement.
- Provide **no additional text** beyond the table.

Your output should look like this:

| Field Name | Type | Mandatory | Purpose |
|------------|------|-----------|---------|
| Username   | Alphanumeric | Yes | Unique identifier for the user. |
| Password   | Alphanumeric | Yes | To authenticate the user securely. |

Do not add headings, intros, or explanations — only the table with necessary fields.
"""
    )
