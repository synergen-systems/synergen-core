# SYNERGEN Cognitive Assessment Engine (v2.0)
# Purpose: Convert candidate responses into trait vectors

questions = {
    1: "Systemic Entropy: Do you add resources or subtract elements to solve efficiency loss? Explain physically.",
    2: "Risk/Synergy: What non-monetary data do you need to justify a 50% growth/20% failure solution?",
    3: "Domain Analogy: Apply water dynamics (flow/pressure/resistance) to market regulation. Where does it fail?",
    4: "Hidden Dependencies: Identify the smallest factor with the largest global impact today.",
    5: "Impact Ethics: How long can you work in a high-paying job with zero impact on the S-coefficient?"
}

# Յուրաքանչյուր հարց կապված է trait-ների հետ
question_trait_map = {
    1: ["systemic_optimizer", "analytical"],
    2: ["high_risk_tolerance", "cross_domain_logic"],
    3: ["flow_optimizer", "cross_domain_logic"],
    4: ["dynamic_system_analyst", "analytical"],
    5: ["strategic_systems_design", "logic_integrator"]
}

def score_response(response: str) -> float:
    """
    Հաշվարկում է պատասխանի որակը 0-10 սկալայով։
    Կրիտերիաներ՝ երկարություն, բառապաշար, հիմնաբառեր։
    """
    if not response or len(response.strip()) < 10:
        return 0.0

    score = 0.0

    # Երկարություն — խորությունը ցույց է տալիս
    word_count = len(response.split())
    if word_count >= 50:
        score += 3.0
    elif word_count >= 20:
        score += 1.5

    # Systemic հիմնաբառեր
    systemic_keywords = [
        "system", "flow", "pressure", "entropy", "optimize",
        "reduce", "efficiency", "dynamic", "vector", "coefficient",
        "impact", "risk", "dependency", "variable", "threshold"
    ]
    keyword_hits = sum(1 for kw in systemic_keywords if kw.lower() in response.lower())
    score += min(keyword_hits * 1.0, 5.0)

    # Անալոգիա կամ բանաձև կա՞
    if any(sym in response for sym in ["=", "/", "→", "∝", "%", "σ", "Δ"]):
        score += 2.0

    return round(min(score, 10.0), 2)


def conduct_assessment(responses: dict) -> dict:
    """
    Ստանում է {question_id: response} dictionary,
    վերադարձնում է candidate-ի trait vector-ը։
    
    :param responses: {1: "պատասխան", 2: "պատասխան", ...}
    :return: {"trait_name": score, ...}
    """
    print("Analyzing cognitive fingerprint...")

    trait_scores = {}
    trait_counts = {}

    for q_id, response in responses.items():
        score = score_response(response)
        traits = question_trait_map.get(q_id, [])

        for trait in traits:
            if trait not in trait_scores:
                trait_scores[trait] = 0.0
                trait_counts[trait] = 0
            trait_scores[trait] += score
            trait_counts[trait] += 1

    # Միջին արժեք յուրաքանչյուր trait-ի համար
    final_vector = {
        trait: round(trait_scores[trait] / trait_counts[trait], 2)
        for trait in trait_scores
    }

    print("Analysis complete.")
    return final_vector


# ============================================================
# Test
# ============================================================

if __name__ == "__main__":
    test_responses = {
        1: "To solve efficiency loss, I subtract entropy sources rather than adding resources. Physically, this mirrors thermodynamic optimization — reducing resistance in the flow system yields higher output without additional input.",
        2: "I need variance data on systemic dependencies, failure cascade coefficients, and the σ of second-order effects. Monetary risk alone ignores dynamic threshold collapse.",
        3: "Water dynamics map well to market flow — pressure is liquidity, resistance is regulation. It fails at phase transitions, where market behavior becomes non-linear and turbulent.",
        4: "Soil microbiome diversity. It controls food systems, carbon cycles, and pharmaceutical discovery — yet receives minimal systemic attention.",
        5: "Zero days. The S-coefficient is the only valid metric of contribution. High pay with zero systemic impact is entropy in human form."
    }

    vector = conduct_assessment(test_responses)

    print("\nCognitive Trait Vector:")
    for trait, score in vector.items():
        print(f"  {trait}: {score}")
