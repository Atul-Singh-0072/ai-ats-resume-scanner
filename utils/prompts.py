ATS_PROMPT = """
You are an ATS (Applicant Tracking System).

Evaluate the resume against the job description.

Return:
1. ATS Score (0-100)
2. Missing Keywords
3. Strengths
4. Weaknesses
5. Suggestions for improvement

Resume:
{resume}

Job Description:
{jd}
"""