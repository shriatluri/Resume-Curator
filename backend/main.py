from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from typing import Optional

# http://localhost:8000/docs

# Create a FastAPI instance
app = FastAPI()

sessions = {}

# Pydantic model for validating resume submission
class ResumeSubmission(BaseModel):
    latex_code: str
    job_url: str

# Defind what the suggesttions are
class Suggestion(BaseModel):
    id: str
    section: str
    original_text: str
    suggested_text: str
    reason: Optional[str] = None
    status: str = "pending"

@app.post("/submit_resume")
def submit_resume(submission: ResumeSubmission):
    session_id = f"session_{len(sessions) + 1}"
    sessions[session_id] = {
        "latex_code": submission.latex_code,
        "job_url": submission.job_url,
        "status": "submitted",
        "suggestions": [] # where the suggestions are stored
    }
    return {"session_id": session_id}

@app.get("/session/{session_id}")
def get_session(session_id: str):
    if session_id not in sessions:
        return {'error': 'Session not found'}
    return sessions[session_id]

@app.post("/session/{session_id}/status")
def update_status(session_id: str, status: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    sessions[session_id]["status"] = status
    return {"session_id": session_id, "new_status": status}

@app.post("/session/{session_id}/add_suggestion")
def add_suggestion(session_id: str, suggestion: Suggestion):
    if session_id not in sessions:
        return {'error': 'Session not found'}
    sessions[session_id]["suggestions"].append(suggestion.dict())
    return {"message": "Suggestion added", "suggestion": suggestion}

# Apporve and Reject Suggestions - need to convert to integer
@app.post("/session/{session_id}/approve_suggestion/{suggestion_id}")
def approve_suggestion(session_id: str, suggestion_id: str):
    if session_id not in sessions:
        return {'error': 'Session not found'}
    try:
        index = int(suggestion_id)
        sessions[session_id]["suggestions"][index]["status"] = "approved"
        return {"message": "Suggestion approved", "suggestion": sessions[session_id]["suggestions"][index]}
    except ValueError:
        return {'error': 'Invalid suggestion ID'}


@app.post("/session/{session_id}/reject_suggestion/{suggestion_id}")
def reject_suggestion(session_id: str, suggestion_id: str):
    if session_id not in sessions:
        return {'error': 'Session not found'}
    try:
        index = int(suggestion_id)
        sessions[session_id]["suggestions"][index]["status"] = "rejected"
        return {"message": "Suggestion rejected", "suggestion": sessions[session_id]["suggestions"][index]}
    except ValueError:
        return {'error': 'Invalid suggestion ID'}