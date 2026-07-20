import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "trained_models")

import joblib

model = joblib.load("trained_models/optimized_resume_classifier.pkl")

tfidf = joblib.load("trained_models/tfidf_vectorizer.pkl")

label_encoder = joblib.load("trained_models/label_encoder.pkl")