# 🚀 AI Triage & Routing System

An intelligent full-stack system that automates support ticket classification, prioritization, and routing.

---

## 🧠 Overview

This project demonstrates how AI can streamline customer support systems by:

* Understanding user issues (tickets)
* Assigning category & priority
* Routing tickets to the correct team/system
* Using RAG (Retrieval-Augmented Generation) for better decisions

---

## ✨ Features

* Ticket classification (Billing, Technical, Sales, HR, etc.)
* Priority detection (Low / Medium / High)
* Smart routing system:

  * Jira → Technical / Security
  * Zendesk → Billing / Sales / Account / General
  * HR System → HR / Payroll
* Lightweight RAG support
* Agent-based routing logic
* Full-stack app (FastAPI + React)
* Local history storage (Frontend)

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python

### Frontend

* React.js

### AI Components

* Rule-based classification
* RAG (static knowledge base)
* Agent-based routing

### Integrations

* Jira
* Zendesk

---

## 📂 Project Structure

backend/
│── app/
│   ├── main.py
│   ├── routes/
│   ├── agents/
│   ├── services/
│   ├── rag/
│   └── integrations/

frontend/
│── src/
│   ├── App.js
│   └── index.js

---

## ⚙️ Setup Instructions

### Backend

cd backend
python -m venv .venv
..venv\Scripts\activate
pip install -r requirements.txt

Run server:

uvicorn app.main --reload

---

### Frontend

cd frontend
npm install
npm start

---

## 🔑 Environment Variables (Optional)

JIRA_URL=your_url
JIRA_EMAIL=your_email
JIRA_TOKEN=your_token

ZENDESK_URL=your_url
ZENDESK_EMAIL=your_email
ZENDESK_TOKEN=your_token

---

## 📡 API

POST /api/triage

Request:
{
"text": "My payment failed but money got deducted"
}

Response:
{
"category": "Billing",
"priority": "High",
"target_team": "Finance",
"system": "Zendesk"
}

---

## ⚠️ Limitations

* Rule-based logic (not real LLM yet)
* Static RAG (no vector DB)
* No database storage
* Basic error handling

---

## 🚀 Future Improvements

* Integrate real LLM (OpenAI / Gemini)
* Add vector database (FAISS)
* Add database (MongoDB / PostgreSQL)
* Deploy on cloud
* Improve UI/UX

---

## 👨‍💻 Author

Jatin Gound
B.Tech CSE (AI & ML)

---
