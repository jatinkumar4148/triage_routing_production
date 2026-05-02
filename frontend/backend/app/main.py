
from fastapi import FastAPI
from app.routes.triage import router as triage_router

app = FastAPI(title="AI Triage & Routing (Prod)")

app.include_router(triage_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "ok", "service": "triage-routing"}
