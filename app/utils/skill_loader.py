import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SKILLS_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "role_skills.json"
)

with open(SKILLS_PATH, "r", encoding="utf-8") as file:
    ROLE_SKILLS = json.load(file)


# Mapping between model predictions and JSON role names
ROLE_MAPPING = {
    "Data Science": "Data Scientist",
    "Python Developer": "Python Developer",
    "Data Analyst": "Data Analyst",
    "Java Developer": "Software Engineer"   # Change this if your JSON has a better match
}


def get_role_skills(role):

    # Convert model prediction to JSON role name
    mapped_role = ROLE_MAPPING.get(role, role)

    return ROLE_SKILLS.get(mapped_role, [])