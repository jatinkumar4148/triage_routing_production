
import os, json, requests

JIRA_URL = os.getenv("JIRA_URL", "https://your-domain.atlassian.net/rest/api/3/issue")
JIRA_TOKEN = os.getenv("JIRA_TOKEN", "")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")

ZENDESK_URL = os.getenv("ZENDESK_URL", "https://your-subdomain.zendesk.com/api/v2/tickets.json")
ZENDESK_TOKEN = os.getenv("ZENDESK_TOKEN", "")
ZENDESK_EMAIL = os.getenv("ZENDESK_EMAIL", "")

def create_jira_ticket(summary, description, priority):
    if not JIRA_TOKEN:
        return {"system": "jira", "status": "skipped (no token)", "summary": summary}
    payload = {
        "fields": {
            "project": {"key": "PROJ"},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"},
            "priority": {"name": priority}
        }
    }
    r = requests.post(JIRA_URL, json=payload, auth=(JIRA_EMAIL, JIRA_TOKEN))
    return {"system": "jira", "status": r.status_code, "response": r.text}

def create_zendesk_ticket(subject, comment, priority):
    if not ZENDESK_TOKEN:
        return {"system": "zendesk", "status": "skipped (no token)", "subject": subject}
    payload = {
        "ticket": {
            "subject": subject,
            "comment": {"body": comment},
            "priority": priority.lower()
        }
    }
    r = requests.post(ZENDESK_URL, json=payload, auth=(f"{ZENDESK_EMAIL}/token", ZENDESK_TOKEN))
    return {"system": "zendesk", "status": r.status_code, "response": r.text}
