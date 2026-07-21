from flask import (
    Blueprint,
    render_template,
    request
)

from app.services import analyze_resume

main = Blueprint("main", __name__)


# =====================================================
# Home Page
# =====================================================
@main.route("/")
def home():
    """Render the application's home page."""
    return render_template("index.html")


# =====================================================
# Single Resume Analysis
# =====================================================
@main.route("/upload", methods=["POST"])
def upload_resume():
    """
    Analyze a single resume with an optional
    Job Description and display the results.
    """

    resume_file = request.files["resume"]
    jd_file = request.files.get("job_description")

    analysis_result = analyze_resume(
        resume_file,
        jd_file
    )

    return render_template(
        "result.html",
        result=analysis_result
    )


# =====================================================
# Recruiter Dashboard
# =====================================================
@main.route("/dashboard")
def recruiter_dashboard():
    """Render the recruiter dashboard."""
    return render_template("recruiter_dashboard.html")


# =====================================================
# Multiple Resume Analysis
# =====================================================
@main.route("/dashboard/upload", methods=["POST"])
def upload_multiple_resumes():
    """
    Analyze multiple uploaded resumes,
    calculate ATS scores,
    and rank candidates.
    """

    resumes = request.files.getlist("resumes")

    # Handle empty upload
    if not resumes or resumes[0].filename == "":
        return render_template(
            "recruiter_dashboard.html",
            error="Please upload at least one resume."
        )

    candidates = []

    # Analyze every uploaded resume
    for resume in resumes:

        analysis_result = analyze_resume(resume)

        candidates.append({
            "filename": resume.filename,
            "category": analysis_result["category"],
            "confidence": analysis_result["confidence"],
            "ats_score": analysis_result["ats_score"]
        })

    # Rank candidates by ATS Score
    candidates.sort(
        key=lambda candidate: candidate["ats_score"],
        reverse=True
    )

    # ==========================
    # Dashboard Statistics
    # ==========================

    total_candidates = len(candidates)

    highest_ats = max(
        candidate["ats_score"]
        for candidate in candidates
    )

    average_ats = round(
        sum(
            candidate["ats_score"]
            for candidate in candidates
        ) / total_candidates,
        2
    )

    average_confidence = round(
        sum(
            candidate["confidence"]
            for candidate in candidates
        ) / total_candidates,
        2
    )

    # ==========================
    # Chart Data
    # ==========================

    candidate_names = [
        candidate["filename"]
        for candidate in candidates
    ]

    ats_scores = [
        candidate["ats_score"]
        for candidate in candidates
    ]

    return render_template(
        "dashboard_results.html",
        candidates=candidates,
        total_candidates=total_candidates,
        highest_ats=highest_ats,
        average_ats=average_ats,
        average_confidence=average_confidence,
        candidate_names=candidate_names,
        ats_scores=ats_scores
    )