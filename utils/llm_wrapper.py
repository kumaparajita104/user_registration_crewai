import openai
import re
from config import OPENAI_API_KEY
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

client = openai.OpenAI(api_key=OPENAI_API_KEY)

class LLMWrapper:
    def __init__(self, model="gpt-4"):
        self.model = model

    def generate_text(self, prompt, temperature=0.5, max_tokens=300):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()

    def get_probability(self, prompt):
        full_prompt = (
            prompt +
            "\n\nRespond ONLY with a number between 0 and 1. Do not explain your reasoning."
        )
        response = self.generate_text(full_prompt)
        try:
            return float(response)
        except ValueError:
            match = re.search(r"\b(0(?:\.\d+)?|1(?:\.0)?)\b", response)
            if match:
                return float(match.group(0))
            print(f"⚠️ Could not parse a float from response: '{response}'")
            return 0.0

    def get_answer_probability(self, prompt, expected_answer, threshold=0.5):
        """
        Returns a similarity-based probability score (0 to 1)
        between the model's generated answer and the expected answer.
        """
        response = self.generate_text(prompt)

        # Compute TF-IDF cosine similarity
        vectorizer = TfidfVectorizer().fit_transform([expected_answer, response])
        similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]

        # Compare to threshold and return 1.0 or 0.0
        return 1.0 if similarity >= threshold else 0.0
