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
