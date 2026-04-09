import math

class SynergenEngine:
    def __init__(self, utility_gain, risk_sigma, implementation_cost):
        self.utility_gain = utility_gain
        self.risk_sigma = risk_sigma
        self.cost = implementation_cost

    def calculate_synergy_coefficient(self):
        """
        Հաշվարկում է S-կոֆիցիենտը՝ մեր ալգորիթմի հիմքը:
        S = ΔUtility / (σ_Risk * Cost)
        """
        if self.risk_sigma == 0 or self.cost == 0:
            return float('inf')  # Կատարյալ լուծում՝ զրոյական ռիսկով/ծախսով
        
        s_coefficient = self.utility_gain / (self.risk_sigma * self.cost)
        return s_coefficient

# Օրինակ՝ ջրային ռեսուրսի օպտիմալացման հաշվարկ
# Utility Gain = 1000 (խնայված ջրի արժեքը)
# Risk Sigma = 0.05 (ցածր ռիսկ)
# Cost = 200 (ծախս)

model = SynergenEngine(utility_gain=1000, risk_sigma=0.05, implementation_cost=200)
s_value = model.calculate_synergy_coefficient()

print(f"Systemic Synergy Coefficient (S): {s_value}")
