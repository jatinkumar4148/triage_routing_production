
import os
from app.rag.store import KB, retrieve_similar

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

def classify_ticket(text: str):
    """Hybrid classification: rule-based + RAG retrieval"""
    t = text.lower()

    # CATEGORY - Rule-based (fast)
    if any(w in t for w in ["pay", "bill", "refund", "invoice", "charge"]):
        category = "Billing"

    elif any(w in t for w in ["error", "bug", "crash", "api", "not working"]):
        category = "Technical"

    elif any(w in t for w in ["salary", "payslip", "payroll"]):
        category = "Payroll"

    elif any(w in t for w in ["leave", "policy", "hr"]):
        category = "HR"

    elif any(w in t for w in ["price", "cost", "pricing", "buy", "purchase", "demo"]):
        category = "Sales"

    elif any(w in t for w in ["hack", "unauthorized", "unauthorised", "breach", "phishing", "security", "suspicious", "compromised", "hacked"]):
        category = "Security"

    elif any(w in t for w in ["login", "password", "account", "reset", "locked"]):
        category = "Account"

    else:
        category = "General"

    # 🔥 Improve with RAG (override if strong match)
    rag_context = retrieve_similar(text, k=2)
    if rag_context and rag_context[0]["label"] in ["Billing", "Technical", "Payroll", "HR", "Sales", "Account", "Security"]:
        if category != "Security" or rag_context[0]["label"] == "Security":
            category = rag_context[0]["label"]

    # PRIORITY
    if any(w in t for w in ["urgent", "asap", "immediately", "down", "blocked", "critical"]):
        priority = "High"
    elif any(w in t for w in ["issue", "problem", "not working", "failed", "error", "unable"]):
        priority = "Medium"
    else:
        priority = "Low"

    return {
        "category": category,
        "priority": priority,
        "rag_context": rag_context
    }

def classify_with_prompt(text: str, context: str):
    """Legacy function for compatibility"""
    result = classify_ticket(text)
    return {
        "category": result["category"],
        "priority": result["priority"],
        "used_context": context
    }

def process_ticket(text: str):
    """Main function: classify + route"""
    result = classify_ticket(text)
    
    # Routing logic based on category
    routing_map = {
        "Technical": {"team": "Engineering Team", "system": "Jira", "confidence": 0.87},
        "Billing": {"team": "Billing Team", "system": "Zendesk", "confidence": 0.85},
        "Account": {"team": "Account Support", "system": "Zendesk", "confidence": 0.80},
        "Security": {"team": "Security Team", "system": "Jira", "confidence": 0.92},
        "Sales": {"team": "Sales Team", "system": "Zendesk", "confidence": 0.78},
        "Payroll": {"team": "HR Payroll", "system": "HR System", "confidence": 0.88},
        "HR": {"team": "HR Team", "system": "HR System", "confidence": 0.80},
        "General": {"team": "Support Team", "system": "Zendesk", "confidence": 0.75}
    }
    
    route_info = routing_map.get(result["category"], routing_map["General"])
    
    return {
        "category": result["category"],
        "priority": result["priority"],
        "target_team": route_info["team"],
        "system": route_info["system"],
        "confidence": route_info["confidence"],
        "rag_context": result["rag_context"]
    }
