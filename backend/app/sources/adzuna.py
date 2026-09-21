from datetime import datetime

import httpx

from .base import JobSource, JobRecord
from ..config import settings


class AdzunaSource(JobSource):
    name = "adzuna"

    async def search(
        self,
        query: str,
        location: str = ""
    ) -> list[JobRecord]:

        if not settings.adzuna_app_id or not settings.adzuna_app_key:
            return []

        country = settings.adzuna_country.lower()

        url = (
            f"https://api.adzuna.com/v1/api/jobs/"
            f"{country}/search/1"
        )

        params = {
            "app_id": settings.adzuna_app_id,
            "app_key": settings.adzuna_app_key,
            "what": query,
            "content-type": "application/json",
            "results_per_page": 20,
        }

        if location:
            params["where"] = location

        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        jobs = []

        for item in data.get("results", []):
            company = item.get("company") or {}
            location_data = item.get("location") or {}

            company_name = (
                company.get("display_name")
                or "Unknown company"
            )

            location_name = (
                location_data.get("display_name")
                or location
                or "Not specified"
            )

            salary_min = item.get("salary_min")
            salary_max = item.get("salary_max")

            if salary_min and salary_max:
                salary = f"{salary_min} - {salary_max}"
            elif salary_min:
                salary = f"From {salary_min}"
            elif salary_max:
                salary = f"Up to {salary_max}"
            else:
                salary = "Not specified"

            contract_time = item.get("contract_time") or ""
            contract_type = item.get("contract_type") or ""

            work_type = "Not specified"

            if contract_time == "full_time":
                work_type = "Full-time"
            elif contract_time == "part_time":
                work_type = "Part-time"

            experience_level = "Not specified"

            created = item.get("created")
            published_at = None

            if created:
                try:
                    published_at = datetime.fromisoformat(
                        created.replace("Z", "+00:00")
                    )
                except ValueError:
                    published_at = None

            jobs.append(
                JobRecord(
                    title=item.get("title", "Untitled job"),
                    company=company_name,
                    description=item.get("description", ""),
                    location=location_name,
                    work_type=work_type,
                    experience_level=experience_level,
                    salary=salary,
                    source=self.name,
                    source_url=item.get("redirect_url", ""),
                    published_at=published_at,
                )
            )

        return jobs