from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI instance
app = FastAPI()

# Pydantic model for validating resume submission
class ResumeSubmission(BaseModel):
    latex_code = str
    job_url = str


