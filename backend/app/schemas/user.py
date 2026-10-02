from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Literal

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password_hash: str
    role: Literal["job_seeker", "recruiter"]

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    email: EmailStr
    role: str

class UserLogin(BaseModel):
    email: EmailStr
    password_hash: str