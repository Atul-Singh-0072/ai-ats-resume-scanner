from agents.ats_agent import run_ats_agent
from agents.scorer_agent import scorer_agent
from agents.reviewer_agent import reviewer_agent
from agents.rewriter_agent import rewriter_agent
from database import save_result
import re


def extract_score(text):
    match = re.search(r'(\d{1,3})', str(text))
    return min(int(match.group(1)), 100) if match else 0


def extract_keywords(text):
    words = re.findall(r'\b[A-Za-z]+\b', str(text))
    return list(set(words))[:10]


def format_analysis(text):
    sections = {"strengths": [], "weaknesses": [], "suggestions": []}
    current = None

    for line in str(text).split("\n"):
        line = line.strip()

        if "Strengths" in line:
            current = "strengths"
            continue
        elif "Weaknesses" in line:
            current = "weaknesses"
            continue
        elif "Suggestions" in line:
            current = "suggestions"
            continue

        if current and line:
            clean = re.sub(r'^\d+\.\s*', '', line)
            clean = clean.replace("**", "")
            sections[current].append(clean)

    return sections


def get_ats_score(resume, jd):
    try:
        ats_output = run_ats_agent(resume, jd)
        score_output = scorer_agent(resume, jd)
        review_output = reviewer_agent(resume, jd)
        rewrite_output = rewriter_agent(resume, jd)

        score = extract_score(score_output)
        keywords = extract_keywords(resume + " " + jd)
        formatted_analysis = format_analysis(review_output)

        breakdown = {
            "ats_match": score,
            "skills": min(score + 5, 100),
            "experience": max(score - 10, 0)
        }

        save_result(score_output, review_output, rewrite_output)

        return {
            "score": score,
            "matched_keywords": keywords,
            "analysis": formatted_analysis,
            "breakdown": breakdown,
            "ats": ats_output,
            "rewrite": rewrite_output
        }

    except Exception as e:
        return {
            "score": 0,
            "matched_keywords": [],
            "analysis": {"strengths": [], "weaknesses": [], "suggestions": [str(e)]},
            "breakdown": {"ats_match": 0, "skills": 0, "experience": 0}
        }