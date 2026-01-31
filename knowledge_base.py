import json
from utils import clean_text, contains_keywords

def load_knowledge_base():
    """
    Loads the knowledge base from the specified JSON file.
    """
    with open("data/knowledge.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_suggestions(problem_text):
    """
    Returns a list of algorithm suggestions based on keywords present in problem_text.
    Uses efficient whole-word matching and avoids duplicates.
    """
    knowledge = load_knowledge_base()
    suggestions = []
    seen = set()

    # Preprocess problem text for robust matching
    cleaned_problem_text = clean_text(problem_text)
    problem_words = set(cleaned_problem_text.split())

    for keyword, algos in knowledge.items():
        cleaned_keyword = clean_text(keyword)
        # Match keyword as a whole word in the problem statement
        if cleaned_keyword in problem_words:
            for algo in algos:
                # Avoid duplicate algorithm suggestions by name and code
                algo_id = (algo.get('name'), algo.get('code'))
                if algo_id not in seen:
                    suggestions.append(algo)
                    seen.add(algo_id)

    return suggestions