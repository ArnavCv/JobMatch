from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate, JobOut

router = APIRouter()

@router.get("/", response_model=List[JobOut])
def list_jobs(db: Session = Depends(get_db)):
    
    jobs = db.query(Job).all()
    return jobs

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=JobCreate)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    
    new_job = Job(**job.model_dump())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.get("/{id}", response_model=JobOut)
def get_job(id: int, db: Session = Depends(get_db)):
    
    job = db.query(Job).filter(Job.id == id).first()
    
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Job with id: {id} not found")
    
    return job

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(id: int, db: Session = Depends(get_db)):
    
    job = db.query(Job).filter(Job.id == id)
    
    if job.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with ID: {id} not found")

    job.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=JobOut)
def update_job(id: int, updated_job: JobUpdate, db: Session = Depends(get_db)):
    
    job_query = db.query(Job).filter(Job.id == id)
    job = job_query.first()
    
    if job == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with ID: {id} not found")

    job_query.update(updated_job.model_dump(), synchronize_session=False) # type: ignore
    db.commit()
    
    return job_query.first()