from pydantic import BaseModel

class JobCreate(BaseModel):
    recruiter_id: int
    title: str
    description: str

class JobUpdate(BaseModel):
    title: str
    description: str

class JobOut(BaseModel):
    title: str
    description: str
