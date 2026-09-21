from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import SearchResponse, JobOut
from .services.search import search_jobs

router = APIRouter(prefix="/api")

@router.get("/health")
def health():
    return {"status": "ok", "service": "JobHunter AI"}

@router.get("/jobs/search", response_model=SearchResponse)
async def search(
    q: str = Query(..., min_length=1),
    location: str = "",
    refresh: bool = False,
    db: Session = Depends(get_db),
):
    jobs = await search_jobs(db, q, location, refresh)
    return {"query": q, "total": len(jobs), "jobs": jobs}

@router.get("/jobs/{job_id}", response_model=JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.get(__import__("app.models", fromlist=["Job"]).Job, job_id)
    if not job:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Job not found")
    return job
