from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from ..models import Job

from ..sources.adzuna import AdzunaSource
from ..sources.jobopportunities import JobOpportunitiesSource


sources = [
    JobOpportunitiesSource(),
    AdzunaSource(),
]


async def search_jobs(
    db: Session,
    query: str,
    location: str = "",
    refresh: bool = False,
):
    stmt = select(Job).where(
        or_(
            Job.title.ilike(f"%{query}%"),
            Job.description.ilike(f"%{query}%"),
        )
    )

    if location:
        stmt = stmt.where(
            Job.location.ilike(f"%{location}%")
        )

    existing = list(db.scalars(stmt).all())

    if refresh or not existing:
        for source in sources:
            try:
                records = await source.search(query, location)

                for record in records:
                    if not record.source_url:
                        continue

                    exists = db.scalar(
                        select(Job).where(
                            Job.source_url == record.source_url
                        )
                    )

                    if not exists:
                        db.add(Job(**record.__dict__))

            except Exception as exc:
                print(
                    f"Source '{source.name}' failed: {exc}"
                )

        db.commit()

        existing = list(db.scalars(stmt).all())

    return existing