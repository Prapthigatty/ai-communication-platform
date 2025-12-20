APOLOGY_WORDS = [
    "sorry", "apologize", "apologies", "regret", "forgive"
]

HEDGING_WORDS = [
    "just", "maybe", "perhaps", "might", "possibly"
]

AGGRESSIVE_WORDS = [
    "unacceptable", "immediately", "must", "should have"
]

def count_matches(text: str, word_list: list) -> int:
    text = text.lower()
    return sum(text.count(word) for word in word_list)
