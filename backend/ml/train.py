import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

# Sample labeled data (we will expand later)
data = {
    "text": [
        "I am extremely sorry for the inconvenience caused",
        "Please let me know if you need any further details",
        "You should have completed this by now",
        "Just checking in regarding the task",
        "I apologize again for disturbing you",
        "This delay is unacceptable",
        "Kindly find the attached report",
        "I was wondering if you had time to review this"
    ],
    "label": [
        "over_apologetic",
        "professional",
        "aggressive",
        "passive",
        "over_apologetic",
        "aggressive",
        "professional",
        "passive"
    ]
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.25, random_state=42
)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

accuracy = pipeline.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

import os

os.makedirs("ml/artifacts", exist_ok=True)

joblib.dump(pipeline, "ml/artifacts/tone_classifier.pkl")
print("Model saved successfully.")

