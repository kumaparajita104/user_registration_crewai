from fuzzywuzzy import fuzz
from collections import Counter

def extract_keywords(text):
    # Split into lines and filter out only meaningful content
    lines = [line.strip().lower() for line in text.splitlines() if len(line.strip()) > 3]
    return set(lines)

def compare_keywords(set1, set2):
    if not set1 or not set2:
        return 0

    matches = 0
    for keyword1 in set1:
        for keyword2 in set2:
            if fuzz.token_set_ratio(keyword1, keyword2) > 80:
                matches += 1
                break  # One match per keyword

    max_len = max(len(set1), len(set2))
    return matches / max_len if max_len > 0 else 1

def run_with_stability_check(crew, runs=3):
    outputs = []

    for i in range(runs):
        print(f"🔁 Executing run {i + 1}...")
        result = crew.kickoff()
        output = result.output if hasattr(result, "output") else str(result)
        outputs.append(output.strip())

    if len(outputs) < 2:
        return outputs[0], 100.0  # Only one run, so 100% confidence

    similarities = []
    for i in range(runs):
        for j in range(i + 1, runs):
            keywords_i = extract_keywords(outputs[i])
            keywords_j = extract_keywords(outputs[j])
            sim = compare_keywords(keywords_i, keywords_j)
            similarities.append(sim)

    stability_score = sum(similarities) / len(similarities)
    confidence = round(stability_score * 100, 2)

    print(f"📊 Stability Score: {stability_score:.2f}")
    print(f"✅ Confidence (based on key concept match): {confidence}%")

    return outputs[0], confidence
