from app.utils.preprocessing import clean_resume

from app.utils.model_loader import (
    model,
    tfidf,
    label_encoder
)


# =====================================================
# Resume Prediction
# =====================================================

def predict_resume_with_confidence(resume_text):
    """
    Predict the resume category and confidence score.

    Pipeline:
    1. Clean Resume Text
    2. Convert Text to TF-IDF Features
    3. Predict Resume Category
    4. Calculate Prediction Confidence
    5. Decode Category Label
    """

    # -------------------------
    # Clean Resume Text
    # -------------------------

    cleaned_text = clean_resume(resume_text)

    # -------------------------
    # TF-IDF Vectorization
    # -------------------------

    resume_vector = tfidf.transform([cleaned_text])

    # -------------------------
    # Model Prediction
    # -------------------------

    predicted_label = model.predict(resume_vector)

    # -------------------------
    # Prediction Confidence
    # -------------------------

    prediction_probabilities = model.predict_proba(
        resume_vector
    )

    confidence_score = (
        prediction_probabilities.max() * 100
    )

    # -------------------------
    # Decode Category
    # -------------------------

    predicted_category = label_encoder.inverse_transform(
        predicted_label
    )[0]

    # -------------------------
    # Final Result
    # -------------------------

    return {

        "category": predicted_category,

        "confidence": round(
            confidence_score,
            2
        ),

        "resume_text": resume_text

    }