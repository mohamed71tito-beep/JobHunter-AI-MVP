from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class JobRecord:
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


class JobSource(ABC):
    name = "base"

    @abstractmethod
    async def search(self, query: str, location: str = "") -> list[JobRecord]:
        raise NotImplementedError