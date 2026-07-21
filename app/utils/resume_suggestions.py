# =====================================================
# Resume Improvement Suggestions
# =====================================================

def generate_suggestions(missing_skills, ats_score, jd_match=None):
    """
    Generate personalized suggestions based on:

    1. Missing Skills
    2. ATS Score
    3. Job Description Match
    """

    suggestions = []

    # =================================================
    # Missing Skills Suggestions
    # =================================================

    if missing_skills:

        for skill in missing_skills[:5]:

            suggestions.append(
                f"Consider adding experience, certifications, or projects related to '{skill}'."
            )

    # =================================================
    # ATS Score Suggestions
    # =================================================

    if ats_score < 60:

        suggestions.extend([
            "Increase the number of relevant technical skills in your resume.",
            "Add measurable achievements using numbers and percentages.",
            "Include more projects related to your target role.",
            "Improve your resume with industry-specific keywords."
        ])

    elif ats_score < 80:

        suggestions.extend([
            "Tailor your resume to better match the target role.",
            "Strengthen your project descriptions with measurable impact."
        ])

    else:

        suggestions.append(
            "Your resume has good skill coverage. Continue improving project descriptions and measurable achievements."
        )

    # =================================================
    # Job Description Match Suggestions
    # =================================================

    if jd_match is not None:

        if jd_match < 60:

            suggestions.extend([
                "Your resume differs significantly from the uploaded Job Description.",
                "Customize your resume keywords according to the Job Description.",
                "Highlight the skills and technologies mentioned in the Job Description."
            ])

        elif jd_match < 80:

            suggestions.extend([
                "Your resume partially matches the Job Description.",
                "Consider adding the missing tools and technologies required for this role."
            ])

        else:

            suggestions.append(
                "Excellent alignment with the uploaded Job Description."
            )

    # =================================================
    # Remove Duplicate Suggestions
    # =================================================

    suggestions = list(dict.fromkeys(suggestions))

    return suggestions