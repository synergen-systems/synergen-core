import math

class SynergenEngine:
    def __init__(self, utility_gain, risk_sigma, implementation_cost):
        """
        Initialize the Core Engine with Systemic Variables.
        :param utility_gain: Total projected benefit (Resource savings)
        :param risk_sigma: Systemic risk factor (0 to 1)
        :param implementation_cost: Cost of deploying the solution
        """
        self.utility_gain = utility_gain
        self.risk_sigma = risk_sigma
        self.cost = implementation_cost

    def calculate_synergy_coefficient(self):
        """
        Calculates the S-Coefficient ($S = \Delta U / (\sigma \cdot C)$).
        The core metric of SYNERGEN efficiency.
        """
        if self.risk_sigma <= 0 or self.cost <= 0:
            return float('inf')  # Ideal system state
        
        return self.utility_gain / (self.risk_sigma * self.cost)

def calculate_candidate_score(candidate_traits, weights):
    """
    Calculates the Node's matching score based on specific Challenge weights.
    :param candidate_traits: Dictionary of candidate skills/traits
    :param weights: Dictionary of required traits and their multipliers from weights.json
    """
    score = sum(candidate_traits.get(trait, 0) * weight for trait, weight in weights.items())
    return round(score, 2)

# Test Execution block
if __name__ == "__main__":
    # Example for CHAL-004 (Strategic Systems Design)
    engine = SynergenEngine(utility_gain=5000, risk_sigma=0.1, implementation_cost=500)
    print(f"Systemic S-Value: {engine.calculate_synergy_coefficient()}")

    # Example Candidate Matching
    weights_chal_04 = {"strategic_systems_design": 1.0}
    candidate_traits = {"strategic_systems_design": 9.2}
    
    score = calculate_candidate_score(candidate_traits, weights_chal_04)
    print(f"Candidate Match Score for CHAL-004: {score}")
