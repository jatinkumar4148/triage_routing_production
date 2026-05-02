
from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.router_agent import route_ticket

router = APIRouter()

class Ticket(BaseModel):
    text: str

@router.post("/triage")
def triage(t: Ticket):
    return route_ticket(t.text)
