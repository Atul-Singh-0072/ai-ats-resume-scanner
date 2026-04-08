from flask import Flask, render_template, request
from utils.parser import extract_text
from main import get_ats_score
from database import init_db

import webbrowser
import threading

app = Flask(__name__)

# Initialize DB
init_db()

# 🔥 Function to open browser automatically
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

@app.route("/", methods=["GET", "POST"])
def index():
    error = None

    # Default values
    score = 0
    matched_keywords = []
    analysis = {"strengths": [], "weaknesses": [], "suggestions": []}
    breakdown = {"ats_match": 0, "skills": 0, "experience": 0}
    rewrite = ""   # ✅ FIX: define default

    if request.method == "POST":
        try:
            file = request.files.get("resume")
            jd = request.form.get("jd")

            if not file or file.filename == "":
                error = "Please upload a resume."
            elif not jd:
                error = "Please enter job description."
            else:
                resume_text = extract_text(file)

                result = get_ats_score(resume_text, jd)

                score = result.get("score", 0)
                matched_keywords = result.get("matched_keywords", [])
                analysis = result.get("analysis", analysis)
                breakdown = result.get("breakdown", breakdown)
                rewrite = result.get("rewrite", "")  # ✅ FIX: move inside POST

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        score=score,
        matched_keywords=matched_keywords,
        analysis=analysis,
        breakdown=breakdown,
        rewrite=rewrite,   # ✅ works now
        error=error
    )

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)