import re

import re
from app.utils.skill_loader import get_role_skills


def calculate_ats_score(resume_text, predicted_role):

    resume = resume_text.lower()

    role_skills = get_role_skills(predicted_role)

    matched_skills = []
    missing_skills = []

    for skill in role_skills:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, resume):
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(role_skills) == 0:
        ats_score = 0
    else:
        ats_score = round(
            (len(matched_skills) / len(role_skills)) * 100,
            2
        )

    return {
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }