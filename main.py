# SYNERGEN Main (v2.0)

from core_engine import SynergenEngine
from matching_engine import match_candidates_to_challenges

if __name__ == "__main__":
    print("=" * 60)
    print("SYNERGEN ENGINE — Matching Report")
    print("=" * 60)

    engine = SynergenEngine(
        utility_gain=1000,
        risk_sigma=0.05,
        implementation_cost=200
    )
    print(f"\nS-Coefficient: {engine.calculate_synergy_coefficient()}")

    print("\n" + "=" * 60)
    print("CANDIDATE — CHALLENGE MATCHING")
    print("=" * 60)

    for result in match_candidates_to_challenges():
        print(f"\n[{result['challenge_id']}] {result['challenge_title']}")
        for m in result["matches"]:
            status = "✅ MATCH" if m["matched"] else "❌ NO MATCH"
            print(f"  {m['candidate']}: score={m['score']} | threshold={m['threshold']} | {status}")
