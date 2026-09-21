from datetime import datetime
from pydantic import BaseModel, ConfigDict

class JobOut(BaseModel):
    id: int
    title: str
    company: str
    description: str
    location: str
    work_type: str
    experience_level: str
    salary: str
    source: str
    source_url: str
    published_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class SearchResponse(BaseModel):
    query: str
    total: int
    jobs: list[JobOut]
