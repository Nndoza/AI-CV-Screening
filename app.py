from flask import Flask, render_template, request
import PyPDF2
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

SKILLS = [
    "AWS",
    "Python",
    "Linux",
    "Docker",
    "Terraform",
    "CI/CD",
    "Kubernetes",
    "Flask",
    "Git"
]

@app.route("/", methods=["GET", "POST"])
def upload_cv():

    extracted_text = ""
    detected_skills = []
    score = 0

    if request.method == "POST":

        file = request.files["cv"]

        if file:

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

            file.save(filepath)

            pdf_reader = PyPDF2.PdfReader(filepath)

            for page in pdf_reader.pages:

                extracted_text += page.extract_text()

            for skill in SKILLS:

                if skill.lower() in extracted_text.lower():

                    detected_skills.append(skill)
                    score = int((len(detected_skills) / len(SKILLS)) * 100)

    return render_template(
        "index.html",
        text=extracted_text,
        skills=detected_skills,
        score=score
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)