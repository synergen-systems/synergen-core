from active_challenges import get_challenges
from candidates import get_candidates

def run_synergy_check():
    challenges = get_challenges()
    candidates = get_candidates()
    
    # Մենք թիրախավորում ենք խցանումների խնդիրը (CHAL-003)
    traffic_challenge = challenges[2] 
    
    print(f"--- SYNERGEN MATCHING SESSION ---")
    print(f"Targeting Challenge: {traffic_challenge['title']}\n")

    for candidate in candidates:
        # Հաշվում ենք, թե քանի հատկանիշ է համընկնում
        matches = set(candidate['cognitive_vector']) & set(traffic_challenge['required_cognitive_traits'])
        score = len(matches)
        
        print(f"Candidate: {candidate['name']}")
        print(f"Match Score: {score}")
        if score >= 2:
            print(f"Result: SUCCESS. Candidate is a HIGH MATCH for this cluster.\n")
        else:
            print(f"Result: Candidate requires additional synergy nodes.\n")

if __name__ == "__main__":
    run_synergy_check()
