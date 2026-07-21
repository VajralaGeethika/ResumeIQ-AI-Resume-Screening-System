import re

from app.utils.skill_loader import (
    get_role_skills
)


# =====================================================
# ATS Score Calculator
# =====================================================

def calculate_ats_score(resume_text, predicted_role):
    """
    Calculate ATS score based on
    the predicted resume category.

    Steps:
    1. Load skills for the predicted role
    2. Compare resume with required skills
    3. Identify matched skills
    4. Identify missing skills
    5. Calculate ATS score
    """

    # -------------------------
    # Prepare Resume Text
    # -------------------------

    resume = resume_text.lower()

    # -------------------------
    # Load Required Skills
    # -------------------------

    role_skills = get_role_skills(predicted_role)

    matched_skills = []
    missing_skills = []

    # -------------------------
    # Skill Matching
    # -------------------------

    for skill in role_skills:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, resume):
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    # -------------------------
    # ATS Score Calculation
    # -------------------------

    if not role_skills:
        ats_score = 0

    else:

        matched_count = len(matched_skills)

        total_skills = len(role_skills)

        ats_score = round(
            (matched_count / total_skills) * 100,
            2
        )

    # -------------------------
    # Final Result
    # -------------------------

    return {

        "ats_score": ats_score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills

    }