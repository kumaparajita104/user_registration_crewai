from .llm_wrapper import LLMWrapper
from .stable_confidence import stable_explanation_confidence

llm = LLMWrapper()

def run_with_stability_check(crew):
    print("▶️ Running PRD task with explanation-based stability check...\n")

    result = crew.kickoff()
    output = result.output if hasattr(result, "output") else str(result)

    question = crew.tasks[0].description
    candidate_answer = output.strip()

    if not candidate_answer:
        print("⚠️ Candidate answer is empty. Returning 0 confidence.")
        return "", 0.0

    print(f"\n📥 Candidate Answer:\n{candidate_answer}\n")

    confidence_score = round(
        stable_explanation_confidence(llm, question, candidate_answer, min_samples=3) * 100, 2
    )

    print(f"\n🧠 Explanation-Based Confidence Score: {confidence_score}%")
    return candidate_answer, confidence_score
