from app.utils.rules import APOLOGY_WORDS, HEDGING_WORDS, AGGRESSIVE_WORDS, count_matches

def calculate_scores(text: str):
    apology_count = count_matches(text, APOLOGY_WORDS)
    hedging_count = count_matches(text, HEDGING_WORDS)
    aggressive_count = count_matches(text, AGGRESSIVE_WORDS)

    confidence_score = max(0, 100 - (apology_count * 15 + hedging_count * 10))
    professionalism_score = max(0, 100 - aggressive_count * 20)

    insights = []

    if apology_count >= 1:
        insights.append("Apologetic language detected")

    if hedging_count >= 1:
        insights.append("Hedging language indicates low assertiveness")

    if aggressive_count >= 1:
        insights.append("Aggressive tone indicators found")

    print("DEBUG COUNTS:", apology_count, hedging_count, aggressive_count)
    return confidence_score, professionalism_score, insights
