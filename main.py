# SYNERGEN Main (v3.0)
# Full pipeline: Assessment → Trait Vector → Challenge Matching

from core_engine import SynergenEngine
from matching_engine import match_candidates_to_challenges_from_vector
from cognitive_assessment import questions, conduct_assessment

# ============================================================
# System Check
# ============================================================

def run_system_check():
    print("=" * 60)
    print("SYNERGEN ENGINE — System Check")
    print("=" * 60)
    engine = SynergenEngine(
        utility_gain=1000,
        risk_sigma=0.05,
        implementation_cost=200
    )
    s_value = engine.calculate_synergy_coefficient()
    print(f"\nGlobal S-Coefficient: {s_value}")
    if s_value >= 4.5:
        print("System Status: ✅ OPERATIONAL")
    else:
        print("System Status: ⚠️ BELOW THRESHOLD")

# ============================================================
# Assessment Flow
# ============================================================

def run_assessment():
    print("\n" + "=" * 60)
    print("SYNERGEN COGNITIVE ASSESSMENT")
    print("=" * 60)

    name = input("\nEnter your name: ").strip()
    if not name:
        name = "Unknown Node"

    print(f"\nWelcome, {name}. Answer the following questions.\n")

    responses = {}
    for q_id, question in questions.items():
        print(f"\n[Q{q_id}] {question}")
        response = input("→ Your answer: ").strip()
        responses[q_id] = response

    print("\nProcessing...")
    trait_vector = conduct_assessment(responses)

    print("\nCognitive Trait Vector:")
    for trait, score in trait_vector.items():
        print(f"  {trait}: {score}")

    return name, trait_vector

# ============================================================
# Matching Flow
# ============================================================

def run_matching(name, trait_vector):
    print("\n" + "=" * 60)
    print("SYNERGEN — CHALLENGE MATCHING")
    print("=" * 60)

    candidate = {
        "name": name,
        "traits": trait_vector
    }

    results = match_candidates_to_challenges_from_vector(candidate)

    matched = [r for r in results if r["matched"]]
    not_matched = [r for r in results if not r["matched"]]

    if matched:
        print(f"\n✅ {name} matched to {len(matched)} challenge(s):\n")
        for r in matched:
            print(f"  [{r['challenge_id']}] {r['challenge_title']}")
            print(f"   Score: {r['score']} | Threshold: {r['threshold']}")
    else:
        print(f"\n❌ No matches found for {name}.")

    if not_matched:
        print(f"\nNot matched ({len(not_matched)}):")
        for r in not_matched:
            print(f"  [{r['challenge_id']}] {r['challenge_title']} | Score: {r['score']} | Threshold: {r['threshold']}")

# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    run_system_check()
    name, trait_vector = run_assessment()
    run_matching(name, trait_vector)
