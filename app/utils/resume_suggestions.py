def generate_suggestions(missing_skills, ats_score, jd_match=None):

    suggestions = []

    # Missing skills
    if missing_skills:
        for skill in missing_skills[:5]:
            suggestions.append(
                f"Consider adding experience or projects related to '{skill}'."
            )

    # ATS score suggestions
    if ats_score < 60:
        suggestions.append(
            "Increase the number of relevant technical skills in your resume."
        )
        suggestions.append(
            "Add measurable achievements using numbers and percentages."
        )

    elif ats_score < 80:
        suggestions.append(
            "Tailor your resume to better match the target role."
        )

    else:
        suggestions.append(
            "Your resume has good skill coverage. Focus on improving project descriptions."
        )

    # JD Match suggestions
    if jd_match is not None:

        if jd_match < 60:
            suggestions.append(
                "Your resume differs significantly from the uploaded Job Description."
            )
            suggestions.append(
                "Customize your resume keywords according to the Job Description."
            )

        elif jd_match < 80:
            suggestions.append(
                "Your resume partially matches the Job Description. Consider adding missing technologies."
            )

        else:
            suggestions.append(
                "Excellent alignment with the Job Description."
            )

    return suggestions