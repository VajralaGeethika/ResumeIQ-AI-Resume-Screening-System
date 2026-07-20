import os
from app.utils.resume_suggestions import generate_suggestions

from app.utils.file_parser import (
    extract_text_from_pdf,
    extract_text_from_docx
)

from app.utils.predictor import (
    predict_resume_with_confidence
)

UPLOAD_FOLDER = "app/uploads"


def save_uploaded_file(file):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    return filepath


def extract_resume_text(filepath):

    extension = filepath.split(".")[-1].lower()

    if extension == "pdf":
        return extract_text_from_pdf(filepath)

    elif extension == "docx":
        return extract_text_from_docx(filepath)

    else:
        raise ValueError("Unsupported File")

from app.utils.ats_score import calculate_ats_score

from app.utils.jd_matcher import calculate_jd_match


def analyze_resume(resume_file, jd_file=None):

    # Save Resume
    resume_path = save_uploaded_file(resume_file)

    # Extract Resume Text
    resume_text = extract_resume_text(resume_path)

    # Predict Category
    result = predict_resume_with_confidence(resume_text)

    # ATS Score
    ats_result = calculate_ats_score(
        resume_text,
        result["category"]
    )

    # Default JD Match
    jd_match = None

    # If JD uploaded
    if jd_file and jd_file.filename != "":

        jd_path = save_uploaded_file(jd_file)

        jd_text = extract_resume_text(jd_path)

        jd_match = calculate_jd_match(
            resume_text,
            jd_text
        )

    suggestions = generate_suggestions(
    ats_result["missing_skills"],
    ats_result["ats_score"],
    jd_match
)

    return {

    "category": result["category"],

    "confidence": result["confidence"],

    "ats_score": ats_result["ats_score"],

    "matched_skills": ats_result["matched_skills"],

    "missing_skills": ats_result["missing_skills"],

    "jd_match": jd_match,

    "suggestions": suggestions,

    "preview": resume_text[:1500]

}