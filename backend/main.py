from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


# http://localhost:8000/docs

# Create a FastAPI instance
app = FastAPI()

sessions = {}

# Pydantic model for validating resume submission
class ResumeSubmission(BaseModel):
    latex_code: str
    job_url: str

# Defind what the suggesttions are


@app.post("/submit_resume")
def submit_resume(submission: ResumeSubmission):
    session_id = f"session_{len(sessions) + 1}"
    sessions[session_id] = {
        "latex_code": submission.latex_code,
        "job_url": submission.job_url,
        "status": "submitted",
        "suggestions": []  # Placeholder for AI suggestions
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
