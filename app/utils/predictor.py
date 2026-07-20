import numpy as np

from app.utils.preprocessing import clean_resume
from app.utils.model_loader import (
    model,
    tfidf,
    label_encoder
)


def predict_resume_with_confidence(resume_text):

    cleaned_text = clean_resume(resume_text)

    vector = tfidf.transform([cleaned_text])

    prediction = model.predict(vector)

    probabilities = model.predict_proba(vector)

    print(probabilities)
    print("Sum:", probabilities.sum())
    print("Max:", probabilities.max())

    confidence = probabilities.max() * 100

    category = label_encoder.inverse_transform(prediction)[0]

    return {
        "category": category,
        "confidence": round(confidence, 2),
        "resume_text": resume_text
    }
