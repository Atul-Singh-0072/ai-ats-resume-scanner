from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="llama-3.1-8b-instant"
)

def run_ats_agent(resume, jd):
    prompt = f"""
    You are an intelligent ATS system.

    Analyze the resume based on the job description.

    Return:
    - ATS Score (0-100)
    - Missing Keywords
    - Strengths
    - Weaknesses
    - Suggestions

    Resume:
    {resume}

    Job Description:
    {jd}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content