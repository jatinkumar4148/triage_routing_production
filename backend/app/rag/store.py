
# Knowledge Base for RAG
KB = [
    # 🔵 BILLING / PAYMENTS
    {"text": "Payment failed during checkout", "label": "Billing"},
    {"text": "Card declined while making payment", "label": "Billing"},
    {"text": "Charged twice for same order", "label": "Billing"},
    {"text": "Refund not received", "label": "Billing"},
    {"text": "Invoice not generated", "label": "Billing"},

    # 🟣 TECHNICAL ISSUES
    {"text": "App crashes on login", "label": "Technical"},
    {"text": "Website not loading properly", "label": "Technical"},
    {"text": "Error 500 on dashboard", "label": "Technical"},
    {"text": "Unable to upload files", "label": "Technical"},
    {"text": "API not responding", "label": "Technical"},

    # 🟢 HR / PAYROLL
    {"text": "Salary not credited", "label": "Payroll"},
    {"text": "Incorrect salary amount", "label": "Payroll"},
    {"text": "Payslip not received", "label": "Payroll"},
    {"text": "Leave balance incorrect", "label": "HR"},
    {"text": "Need update on leave policy", "label": "HR"},

    # 🟡 SALES / PRICING
    {"text": "Need information about product pricing", "label": "Sales"},
    {"text": "What is the cost of your service", "label": "Sales"},
    {"text": "Do you offer discounts", "label": "Sales"},
    {"text": "Request for product demo", "label": "Sales"},
    {"text": "Interested in purchasing product", "label": "Sales"},

    # 🟠 ACCOUNT MANAGEMENT
    {"text": "Unable to login to account", "label": "Account"},
    {"text": "Forgot password reset not working", "label": "Account"},
    {"text": "Account locked after multiple attempts", "label": "Account"},
    {"text": "Update email address", "label": "Account"},
    {"text": "Delete my account", "label": "Account"},

    # 🔴 SECURITY
    {"text": "Suspicious login detected", "label": "Security"},
    {"text": "Unauthorized access to account", "label": "Security"},
    {"text": "Report phishing email", "label": "Security"},
    {"text": "Data breach concern", "label": "Security"},
    {"text": "Password compromised", "label": "Security"},

    # ⚪ GENERAL / INFO
    {"text": "Need help using the platform", "label": "General"},
    {"text": "How does this service work", "label": "General"},
    {"text": "Where can I find documentation", "label": "General"},
    {"text": "General inquiry about features", "label": "General"},
    {"text": "Contact support team", "label": "General"},
]

def retrieve_similar(query: str, k: int = 2):
    # Naive similarity by keyword overlap
    scores = []
    qset = set(query.lower().split())
    for item in KB:
        iset = set(item["text"].lower().split())
        score = len(qset & iset)
        scores.append((score, item))
    scores.sort(key=lambda x: x[0], reverse=True)
    return [it for sc, it in scores[:k]]
