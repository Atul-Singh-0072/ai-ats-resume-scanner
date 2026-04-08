# 🤖 AI ATS Resume Analyzer (Multi-Agent AI System)

An advanced AI-powered Applicant Tracking System (ATS) that evaluates resumes against job descriptions using a **multi-agent architecture powered by LLMs (Groq + LangChain)**.

This system simulates how real-world ATS tools work and enhances them with intelligent reasoning, detailed feedback, and automatic resume rewriting.

---

## 📌 Project Overview

Modern hiring platforms use ATS systems to filter resumes based on keyword relevance and formatting.
This project **replicates and improves that process using AI**.

👉 Instead of a single model, this system uses **multiple specialized AI agents**, each responsible for a specific task.

---

## 📸 Screenshots

> ⚠️ Replace image paths with your actual files (recommended: `/images/ss1.png`, etc.)

![Dashboard](![WhatsApp Image 2026-04-08 at 4 41 27 PM](https://github.com/user-attachments/assets/60a5cad6-d893-484a-93ca-138fe887bf47)
)
![Analysis](![WhatsApp Image 2026-04-08 at 4 41 27 PM (1)](https://github.com/user-attachments/assets/7e69959d-ace8-49bc-81fe-109894f7a038)
)
![Score](![WhatsApp Image 2026-04-08 at 4 41 31 PM](https://github.com/user-attachments/assets/4e737004-c6f2-4e36-9027-25b9568e2877)
)
![Feedback](![WhatsApp Image 2026-04-08 at 4 41 31 PM (1)](https://github.com/user-attachments/assets/108247c1-7f6a-4c76-a905-0cdeb3ceea67)
)

---

## 🧠 Multi-Agent Architecture (CORE IDEA)

```
User Input (Resume + Job Description)
            ↓
        Flask Backend
            ↓
      Agent Orchestrator (main.py)
            ↓
 ┌─────────────────────────────────┐
 │        Multi-Agent System       │
 │                                 │
 │  🤖 ATS Agent       → Overall analysis
 │  📊 Scorer Agent    → Score + keywords
 │  🧠 Reviewer Agent  → Strengths/Weaknesses
 │  ✍️ Rewriter Agent  → Resume improvement
 │                                 │
 └─────────────────────────────────┘
            ↓
        SQLite Database
            ↓
     Frontend Dashboard (UI + Charts)
```

---

## 🤖 Agents Explained

### 1️⃣ ATS Agent (Global Intelligence Agent)

* Performs holistic evaluation of resume vs job description
* Understands context and semantic alignment
* Acts like a virtual recruiter

### 2️⃣ 📊 Scorer Agent (Analytical Agent)

* Extracts keywords from job description
* Matches them with resume
* Calculates ATS score (0–100)
* Detects missing skills

### 3️⃣ 🧠 Reviewer Agent (Evaluation Agent)

* Identifies strengths and weaknesses
* Suggests improvements
* Evaluates clarity and structure

### 4️⃣ ✍️ Rewriter Agent (Generative Agent)

* Rewrites resume professionally
* Aligns content with job description
* Improves ATS compatibility

---

## 🔥 Why Multi-Agent System?

| Traditional Approach       | Multi-Agent Approach |
| -------------------------- | -------------------- |
| One LLM handles everything | Specialized agents   |
| Hard to scale              | Modular design       |
| Generic output             | Structured output    |
| Less control               | High flexibility     |

---

## ⚙️ Tech Stack

**AI / LLM**

* Groq API
* LangChain

**Backend**

* Python
* Flask

**Frontend**

* HTML
* CSS
* JavaScript

**Visualization**

* Chart.js

**Database**

* SQLite

---

## 📊 Features

* ✅ Multi-agent AI system
* ✅ ATS score calculation
* ✅ Keyword extraction & matching
* ✅ Resume feedback generation
* ✅ AI-powered resume rewriting
* ✅ Interactive dashboard UI
* ✅ Graph-based score visualization
* ✅ Data persistence (SQLite)

---

## 📁 Project Structure

```
ai-ats-resume-scanner/
├── app.py
├── main.py
├── database.py
│
├── agents/
│   ├── ats_agent.py
│   ├── scorer_agent.py
│   ├── reviewer_agent.py
│   └── rewriter_agent.py
│
├── utils/
│   ├── parser.py
│   ├── scorer.py
│   └── prompts.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

```bash
git clone https://github.com/Atul-Singh-0072/ai-ats-resume-scanner.git
cd ai-ats-resume-scanner

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set API Key
set GROQ_API_KEY=your_api_key

# Run project
python app.py
```

Open in browser:
👉 http://127.0.0.1:5000

---

## 💾 Database Design

| Field   | Description      |
| ------- | ---------------- |
| score   | ATS score output |
| review  | Feedback         |
| rewrite | Improved resume  |

---

## 📊 UI Features

* 🎯 ATS Score visualization (chart + circle)
* 🏷️ Keyword tags display
* 📋 Structured feedback cards
* ✍️ Resume preview section

---

## 🚀 Future Enhancements

* 🔐 User authentication
* ☁️ Cloud deployment (AWS / GCP)
* 📄 Resume download (PDF/DOCX)
* 🧠 Memory-enabled AI agents
* 📊 Advanced analytics dashboard

---

## 💡 Key Learnings

* Multi-agent system design
* LLM integration in real-world apps
* Prompt engineering
* Full-stack AI development
* Modular architecture

---

## 📌 Use Cases

* Job seekers optimizing resumes
* HR automation tools
* Career coaching platforms
* Resume screening systems

---

## 👨‍💻 Author

**Atul Singh**
🔗 https://github.com/Atul-Singh-0072

---

## ⭐ Support

If you like this project, please ⭐ star the repository!

---

## 🏷️ Topics

`ai` `nlp` `ats-scanner` `resume-analysis` `llm` `flask` `python` `generative-ai` `web-app`
