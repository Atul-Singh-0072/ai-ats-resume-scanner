![WhatsApp Image 2026-04-08 at 4 41 27 PM (1)](https://github.com/user-attachments/assets/c3ed27de-4634-4773-8956-8cd8f755ceae)
![WhatsApp Image 2026-04-08 at 4 41 31 PM](https://github.com/user-attachments/assets/14e9e2f6-eaf3-40d0-ae58-edf99e859312)
![WhatsApp Image 2026-04-08 at 4 41 31 PM (1)](https://github.com/user-attachments/assets/2f93ef58-950a-4af9-a6e5-27056657d914)
![WhatsApp Image 2026-04-08 at 4 41 27 PM](https://github.com/user-attachments/assets/edf14071-56b3-43c0-a97c-b61a598e4d4b)
#  AI ATS Resume Analyzer (Multi-Agent AI System)

An advanced **AI-powered Applicant Tracking System (ATS)** that evaluates resumes against job descriptions using a **multi-agent architecture powered by LLMs (Groq + LangChain)**.

This system simulates how real-world ATS tools work in companies and enhances it with **intelligent reasoning, feedback, and resume rewriting**.

---

# 📌 Project Overview

Modern hiring systems use ATS to filter resumes based on keyword relevance and formatting. This project replicates and improves that process using AI.

👉 Instead of a single model, this system uses **multiple specialized AI agents**, each responsible for a specific task.

---

# 🧠 Multi-Agent Architecture (CORE IDEA)

Unlike traditional systems, this project follows a **modular agent-based design**:

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

# 🤖 Agents Explained in Detail

## 1️⃣ ATS Agent (Global Intelligence Agent)

### 📌 Purpose:

Provides a **holistic evaluation** of the resume against the job description.

### 🧠 What it does:

* Understands the entire resume context
* Compares semantic alignment with JD
* Generates high-level ATS insights
* Acts like a **virtual recruiter**

### 💡 Output:

* Overall analysis
* Fitment summary
* Context-aware reasoning

### 🎯 Why important:

This is the **"brain" of the system** — gives human-like understanding beyond keywords.

---

## 2️⃣ 📊 Scorer Agent (Analytical Agent)

### 📌 Purpose:

Calculates **ATS score and keyword matching**

### 🧠 What it does:

* Extracts keywords from JD
* Matches them with resume
* Computes relevance score
* Identifies missing skills

### 💡 Output:

* ATS Score (0–100)
* Matched keywords
* Missing keywords

### 🎯 Why important:

Simulates **real ATS filtering logic** used in companies.

---

## 3️⃣ 🧠 Reviewer Agent (Evaluation Agent)

### 📌 Purpose:

Provides **detailed feedback on resume quality**

### 🧠 What it does:

* Identifies strengths
* Detects weaknesses
* Suggests improvements
* Evaluates structure & clarity

### 💡 Output:

* Strengths
* Weaknesses
* Actionable suggestions

### 🎯 Why important:

Helps user **improve resume quality**, not just score.

---

## 4️⃣ ✍️ Rewriter Agent (Generative Agent)

### 📌 Purpose:

Automatically **improves and rewrites the resume**

### 🧠 What it does:

* Rephrases content professionally
* Aligns resume with JD
* Adds missing keywords naturally
* Improves ATS compatibility

### 💡 Output:

* Optimized resume content

### 🎯 Why important:

Turns insights into **actionable output** — real value for users.

---

# 🔥 Why Multi-Agent System?

| Traditional Approach    | Multi-Agent Approach |
| ----------------------- | -------------------- |
| One LLM does everything | Specialized agents   |
| Less control            | Modular design       |
| Hard to scale           | Easy to extend       |
| Generic output          | Structured output    |

👉 This architecture is used in **modern AI systems and startups**

---

# ⚙️ Tech Stack

## 🧠 AI / LLM

* Groq API (Ultra-fast inference)
* LangChain (Agent orchestration)

## 🖥️ Backend

* Python
* Flask

## 🎨 Frontend

* HTML
* CSS (Custom UI)
* JavaScript
* Chart.js (Visualization)

## 💾 Database

* SQLite

---

# 📊 Features

* ✅ Multi-agent AI system
* ✅ ATS score calculation
* ✅ Keyword extraction & matching
* ✅ Resume feedback generation
* ✅ AI-powered resume rewriting
* ✅ Dynamic dashboard UI
* ✅ Graph-based score visualization
* ✅ Data persistence (SQLite)

---

# 📁 Project Structure

```
ai-ats-resume-scanner/
│
├── app.py                  # Flask app (entry point)
├── main.py                 # Agent orchestration
├── database.py             # DB operations
│
├── agents/                 # AI Agents
│   ├── ats_agent.py
│   ├── scorer_agent.py
│   ├── reviewer_agent.py
│   └── rewriter_agent.py
│
├── utils/
│   ├── parser.py           # Resume parser (PDF/DOCX)
│   ├── scorer.py           # Keyword logic
│   └── prompts.py          # LLM prompts
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

# 🚀 Installation & Setup

```bash
git clone https://github.com/Atul-Singh-0072/ai-ats-resume-scanner.git
cd ai-ats-resume-scanner
```

### Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Set API Key

```bash
set GROQ_API_KEY=your_api_key
```

### Run project

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 💾 Database Design

| Field   | Description      |
| ------- | ---------------- |
| score   | ATS score output |
| review  | Feedback         |
| rewrite | Improved resume  |

---

# 📸 UI Features

* 🎯 Score visualization (chart + circle)
* 🏷️ Keyword tags
* 📋 Structured feedback cards
* ✍️ Resume preview section

---

# 🚀 Future Enhancements

* 🔐 User authentication system
* ☁️ Cloud deployment (AWS / GCP)
* 📄 Download resume (PDF/DOCX)
* 🧠 Memory-enabled agents
* 📊 Advanced analytics dashboard

---

# 💡 Key Learnings

* Multi-agent system design
* LLM integration in production apps
* Prompt engineering
* Full-stack AI development
* Modular architecture

---

# 📌 Use Cases

* Job seekers optimizing resumes
* HR automation tools
* Career coaching platforms
* Resume screening systems

---

# 👨‍💻 Author

**Atul Singh**
GitHub: https://github.com/Atul-Singh-0072

---

# ⭐ Support

If you like this project, please ⭐ star the repository!
