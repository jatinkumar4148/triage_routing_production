
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.triage import router as triage_router

app = FastAPI(title="AI Triage & Routing (Prod)")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(triage_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "ok", "service": "triage-routing"}
