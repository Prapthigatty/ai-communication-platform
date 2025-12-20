from app.utils.rules import APOLOGY_WORDS, HEDGING_WORDS, AGGRESSIVE_WORDS
def generate_rewrite(text: str, tone: str):
    lower_text = text.lower()

    # Case 1: Apology due to delay
    if "delay" in lower_text or "late" in lower_text or "responded earlier" in lower_text:
        return (
            "Apologies for the delayed response. "
            "Thank you for your patience."
        )

    # Case 2: Follow-up messages
    if "follow" in lower_text or "checking" in lower_text:
        return (
            "Following up to check if you had time to review this. "
            "Please let me know your thoughts."
        )

    # Case 3: Aggressive tone softening
    if tone == "aggressive":
        return (
            "I would appreciate an update on the status of this task. "
            "Please let me know how we can proceed."
        )

    # Default: polite professional rewrite
    if tone in ["passive", "over_apologetic"]:
        return (
            "Please let me know if you have any updates. "
            "I look forward to your response."
        )

    return text.strip()

