
from app.rag.store import retrieve_similar
from app.services.llm_service import process_ticket
from app.integrations.tools import create_jira_ticket, create_zendesk_ticket
import uuid

def route_ticket(text: str):
    # Use improved classification
    result = process_ticket(text)

    # Generate ticket ID
    ticket_id = f"TCK-{str(uuid.uuid4())[:8].upper()}"

    # Create ticket in target system
    system = result["system"]
    if system == "Jira":
        ticket = create_jira_ticket(summary=text[:80], description=text, priority=result["priority"])
    elif system == "HR System":
        # For HR System, just skip (similar to Zendesk)
        ticket = {"system": "HR System", "status": "skipped (no token)", "subject": text[:80]}
    else:
        ticket = create_zendesk_ticket(subject=text[:80], comment=text, priority=result["priority"])

    return {
        "ticket_id": ticket_id,
        "input": text,
        "category": result["category"],
        "priority": result["priority"],
        "target_team": result["target_team"],
        "system": result["system"],
        "confidence": result["confidence"],
        "integration_result": ticket,
        "rag_context": result["rag_context"]
    }
