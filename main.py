from core_engine import SynergenEngine
from active_challenges import get_challenges

def run_synergen_demo():
    print("--- SYNERGEN SYSTEM INITIALIZED ---")
    
    # 1. Վերցնում ենք ակտիվ խնդիրները
    all_challenges = get_challenges()
    
    # 2. Օրինակ՝ հաշվարկում ենք առաջին խնդրի S-կոֆիցիենտը
    # Ենթադրենք՝ Utility=1000, Risk=0.05, Cost=150
    pilot_project = SynergenEngine(utility_gain=1000, risk_sigma=0.05, implementation_cost=150)
    s_val = pilot_project.calculate_synergy_coefficient()
    
    print(f"Current Target: {all_challenges[0]['title']}")
    print(f"Calculated Systemic Synergy (S): {s_val:.2f}")
    print("Status: Ready for Expert Integration.")

if __name__ == "__main__":
    run_synergen_demo()
