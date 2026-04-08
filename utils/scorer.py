def keyword_match(resume, jd):
    jd_words = set(jd.lower().split())
    resume_words = set(resume.lower().split())

    match = jd_words.intersection(resume_words)

    if len(jd_words) == 0:
        return 0, []

    score = (len(match) / len(jd_words)) * 100

    return round(score, 2), list(match)