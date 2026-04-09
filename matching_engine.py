# SYNERGEN Matching Engine (v1.1)
from active_challenges import get_challenges

class MatchingEngine:
    def __init__(self, user_vector):
        self.user_vector = user_vector
        self.challenges = get_challenges()

    def get_top_matches(self):
        """
        Համեմատում է օգտատիրոջ կոգնիտիվ վեկտորը ակտիվ խնդիրների հետ:
        """
        results = []
        for challenge in self.challenges:
            # Հաշվում ենք համընկնող հատկանիշները
            match_score = len(set(self.user_vector) & set(challenge["required_cognitive_traits"]))
            results.append({
                "challenge": challenge["title"],
                "score": match_score,
                "impact": challenge["impact_potential"]
            })
        
        # Սորտավորում ենք ըստ ամենաբարձր համապատասխանության
        return sorted(results, key=lambda x: x["score"], reverse=True)

# Օրինակ. Եթե Դենիսը ունի այս հատկանիշները.
# user_traits = ["logic_integrator", "flow_optimizer"]
