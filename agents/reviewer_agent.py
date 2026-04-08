from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

llm = ChatGroq(
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="llama-3.1-8b-instant"
)

def reviewer_agent(resume, jd):
    prompt = f"""
    Review this resume:
    - Strengths
    - Weaknesses
    - Suggestions

    Resume:
    {resume}

    Job Description:
    {jd}
    """

    return llm.invoke([HumanMessage(content=prompt)]).content