import json
import os


# =====================================================
# Project Paths
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

SKILLS_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "role_skills.json"
)


# =====================================================
# Load Role Skills
# =====================================================

try:
    with open(SKILLS_PATH, "r", encoding="utf-8") as file:
        ROLE_SKILLS = json.load(file)

except FileNotFoundError:
    raise FileNotFoundError(
        f"Role skills file not found: {SKILLS_PATH}"
    )


# =====================================================
# Model Prediction → JSON Role Mapping
# =====================================================

ROLE_MAPPING = {

    "Data Science": "Data Scientist",

    "Data Analyst": "Data Analyst",

    "Python Developer": "Python Developer",

    # Update this mapping if your JSON changes
    "Java Developer": "Software Engineer"

}


# =====================================================
# Get Skills for a Role
# =====================================================

def get_role_skills(role):
    """
    Return the required skills for
    the predicted resume category.

    If the role does not exist,
    an empty list is returned.
    """

    mapped_role = ROLE_MAPPING.get(role, role)

    return ROLE_SKILLS.get(mapped_role, [])