from app.utils.preprocess import preprocess_text
from ml.predict import predict_tone
from app.services.scoring import calculate_scores
from app.services.rewrite import generate_rewrite

def analyze_text(text: str):
    cleaned_text = preprocess_text(text)
    tone = predict_tone(cleaned_text)

    confidence, professionalism, insights = calculate_scores(text)
    rewrite = generate_rewrite(text, tone)

    return {
        "original_text": text,
        "cleaned_text": cleaned_text,
        "tone": tone,
        "confidence_score": confidence,
        "professionalism_score": professionalism,
        "insights": insights,
        "rewrite_suggestion": rewrite
    }
