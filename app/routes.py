
from flask import (
    Blueprint,
    render_template,
    request
)

from app.services import (
    save_uploaded_file,
    analyze_resume
)
main = Blueprint("main", __name__)


@main.route("/")
def home():

    return render_template("index.html")


@main.route("/upload", methods=["POST"])
@main.route("/upload", methods=["POST"])
def upload_resume():

    # Resume (Required)
    resume_file = request.files["resume"]

    # Job Description (Optional)
    jd_file = request.files.get("job_description")

    result = analyze_resume(
        resume_file,
        jd_file
    )

    return render_template(
        "result.html",
        result=result
    )