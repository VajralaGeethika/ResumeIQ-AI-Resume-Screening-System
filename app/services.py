import os

from app.utils.file_parser import (
    extract_text_from_pdf,
    extract_text_from_docx
)

from app.utils.predictor import (
    predict_resume_with_confidence
)

from app.utils.ats_score import (
    calculate_ats_score
)

from app.utils.jd_matcher import (
    calculate_jd_match
)

from app.utils.resume_suggestions import (
    generate_suggestions
)


# =====================================================
# Upload Folder
# =====================================================

UPLOAD_FOLDER = "app/uploads"


# =====================================================
# Save Uploaded File
# =====================================================

def save_uploaded_file(file):
    """
    Save the uploaded file
    and return its file path.
    """

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    return filepath


# =====================================================
# Extract Resume / JD Text
# =====================================================

def extract_resume_text(filepath):
    """
    Extract text from PDF or DOCX files.
    """

    extension = filepath.split(".")[-1].lower()

    if extension == "pdf":
        return extract_text_from_pdf(filepath)

    if extension == "docx":
        return extract_text_from_docx(filepath)

    raise ValueError("Unsupported file format.")


# =====================================================
# Resume Analysis Pipeline
# =====================================================

def analyze_resume(resume_file, jd_file=None):
    """
    Complete Resume Analysis Pipeline

    Steps:
    1. Save Resume
    2. Extract Resume Text
    3. Predict Resume Category
    4. Calculate ATS Score
    5. Calculate JD Match (Optional)
    6. Generate Resume Suggestions
    7. Return Analysis Results
    """

    # -------------------------
    # Save Resume
    # -------------------------

    resume_path = save_uploaded_file(resume_file)

    # -------------------------
    # Extract Resume Text
    # -------------------------

    resume_text = extract_resume_text(resume_path)

    # -------------------------
    # Resume Classification
    # -------------------------

    prediction = predict_resume_with_confidence(
        resume_text
    )

    # -------------------------
    # ATS Score
    # -------------------------

    ats_result = calculate_ats_score(
        resume_text,
        prediction["category"]
    )

    # -------------------------
    # JD Match (Optional)
    # -------------------------

    jd_match = None

    if jd_file and jd_file.filename:

        jd_path = save_uploaded_file(jd_file)

        jd_text = extract_resume_text(jd_path)

        jd_match = calculate_jd_match(
            resume_text,
            jd_text
        )

    # -------------------------
    # Resume Suggestions
    # -------------------------

    suggestions = generate_suggestions(
        ats_result["missing_skills"],
        ats_result["ats_score"],
        jd_match
    )

    # -------------------------
    # Final Response
    # -------------------------

    return {

        "category": prediction["category"],

        "confidence": prediction["confidence"],

        "ats_score": ats_result["ats_score"],

        "matched_skills": ats_result["matched_skills"],

        "missing_skills": ats_result["missing_skills"],

        "jd_match": jd_match,

        "suggestions": suggestions,

        "preview": resume_text[:1500]

    }