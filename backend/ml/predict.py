import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR,"ml", "artifacts", "tone_classifier.pkl")

model = joblib.load(MODEL_PATH)

def predict_tone(text: str):
    return model.predict([text])[0]
