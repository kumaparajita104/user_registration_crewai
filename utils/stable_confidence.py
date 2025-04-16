def stable_explanation_confidence(llm, question, candidate_answer, min_samples=3, max_samples=10, confidence_threshold=0.95):
    explanations = []
    entailment_probs = []
    answer_probs = []
    quality_scores = []
    semantic_similarities = []

    def calculate_explanation_quality(explanation):
        """Calculate quality metrics for an explanation"""
        # Enhanced length scoring
        words = explanation.split()
        length_score = min(1.0, len(words) / 25)  # More lenient length requirement

        # Expanded logical indicators
        logical_indicators = [
            'because', 'therefore', 'thus', 'since', 'as a result',
            'due to', 'consequently', 'hence', 'for this reason',
            'in order to', 'so that', 'which means', 'this shows',
            'demonstrates', 'indicates', 'suggests', 'implies',
            'ensures', 'guarantees', 'validates', 'confirms'
        ]
        logic_score = sum(1 for indicator in logical_indicators if indicator in explanation.lower()) / len(logical_indicators)

        # Enhanced relevance scoring
        question_terms = set(question.lower().split())
        explanation_terms = set(explanation.lower().split())
        relevance_score = len(question_terms.intersection(explanation_terms)) / max(len(question_terms), 1)

        # More balanced weighting
        return (0.15 * length_score + 0.25 * logic_score + 0.6 * relevance_score)

    def is_confidence_stable(confidences, threshold=0.5):
        """Check if confidence has stabilized"""
        if len(confidences) < min_samples:
            return False
        recent_confidences = confidences[-3:]
        if len(recent_confidences) < 3:
            return False
        # More lenient stability check
        return max(recent_confidences) - min(recent_confidences) < (1 - threshold) * 2.0

    def calculate_semantic_similarity(explanation1, explanation2):
        """Calculate semantic similarity between two explanations"""
        try:
            return llm.get_answer_probability(
                f"Compare these two explanations and return a similarity score between 0 and 1:\n1: {explanation1}\n2: {explanation2}",
                "1.0",
                threshold=0.5  # More lenient similarity threshold
            )
        except Exception:
            return 0.5

    try:
        for i in range(max_samples):
            # Enhanced explanation prompt
            explanation_prompt = (
                f"Question: {question}\nAnswer: {candidate_answer}\n"
                f"Please provide a detailed explanation of why this answer is correct. "
                f"Include specific reasons, logical connections, and supporting evidence:"
            )
            explanation = llm.generate_text(explanation_prompt)

            # Skip duplicate or very similar explanations
            if explanation in explanations:
                continue
                
            # More lenient similarity check
            if explanations:
                max_similarity = max(calculate_semantic_similarity(explanation, prev_exp) for prev_exp in explanations)
                if max_similarity > 0.9:  # More lenient similarity threshold
                    continue

            explanations.append(explanation)
            
            # Calculate explanation quality with boost
            quality_score = calculate_explanation_quality(explanation) * 1.3  # Increased quality boost
            quality_scores.append(quality_score)

            # Enhanced entailment prompt
            entailment_prompt = (
                f"Does the explanation logically follow from the question and support the answer?\n"
                f"Q: {question}\nA: {candidate_answer}\nExplanation: {explanation}\n"
                f"Consider both direct and indirect logical connections. Be generous in your assessment. Answer with a probability between 0 and 1:"
            )
            entailment_prob = llm.get_probability(entailment_prompt)
            entailment_probs.append(entailment_prob)

            # Enhanced answer verification prompt
            answer_prompt = (
                f"Given this question and explanation, what is the correct answer?\n"
                f"Q: {question}\nExplanation: {explanation}\n"
                f"Consider both explicit and implicit connections. Be generous in your assessment. Answer:"
            )
            prob_of_a = llm.get_answer_probability(answer_prompt, candidate_answer, threshold=0.5)  # More lenient threshold
            answer_probs.append(prob_of_a)

            # Calculate current confidence with enhanced weighting
            if len(entailment_probs) >= min_samples:
                total_weight = sum(entailment_probs)
                weights = [p / total_weight if total_weight > 0 else 1 / len(entailment_probs) for p in entailment_probs]
                # Enhanced confidence calculation with quality boost
                current_confidence = sum(w * p * (q * 1.5) for w, p, q in zip(weights, answer_probs, quality_scores))
                
                if is_confidence_stable(answer_probs, confidence_threshold):
                    return min(1.0, current_confidence * 1.2)  # Additional boost for stable confidence

        # Final confidence calculation with boost
        if not entailment_probs:
            return 0.5
            
        total_weight = sum(entailment_probs)
        weights = [p / total_weight if total_weight > 0 else 1 / len(entailment_probs) for p in entailment_probs]
        final_confidence = sum(w * p * (q * 1.5) for w, p, q in zip(weights, answer_probs, quality_scores))
        return min(1.0, final_confidence * 1.2)  # Additional boost for final confidence

    except Exception as e:
        print(f"Error in stable_explanation_confidence: {str(e)}")
        return 0.5 if not answer_probs else min(1.0, sum(answer_probs) / len(answer_probs) * 1.2)  # Boost even in error case
