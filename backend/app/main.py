from fastapi import FastAPI
from app.database import engine, Base
from app.routes.auth import router as auth_router
from app.routes.jobs import router as job_router
from app.routes.users import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(job_router, prefix="/jobs", tags=["Jobs"])
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "JobMatch API Running"}