def calculate_candidate_score(candidate, challenge):
    chal_id = challenge["id"]
    weights = trait_weights.get(chal_id, {})
    
    # Flexible data retrieval
    candidate_traits = candidate.get("traits", candidate.get("cognitive_vector", {}))
    
    # --- YOUR ADDITION START ---
    # If it's a list, convert to dict with max score (10.0)
    if isinstance(candidate_traits, list):
        candidate_traits = {t: 10.0 for t in candidate_traits}
    # --- YOUR ADDITION END ---
    
    score = 0.0
    for trait, weight in weights.items():
        if trait in candidate_traits:
            skill_level = candidate_traits[trait]
            score += weight * skill_level
            
    return round(score, 2)
def match_candidates_to_challenges_from_vector(candidate):
    """Մեկ candidate-ի trait vector-ը բոլոր challenges-ի դեմ։"""
    from active_challenges import get_challenges
    results = []
    for challenge in get_challenges():
        score = calculate_candidate_score(candidate, challenge)
        threshold = challenge["s_threshold"]
        results.append({
            "challenge_id": challenge["id"],
            "challenge_title": challenge["title"],
            "score": score,
            "threshold": threshold,
            "matched": score >= threshold
        })
    return sorted(results, key=lambda x: x["score"], reverse=True)
