from datetime import datetime

from sqlalchemy import String, Text, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    company: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    description: Mapped[str] = mapped_column(
        Text,
        default=""
    )

    location: Mapped[str] = mapped_column(
        String(255),
        default=""
    )

    work_type: Mapped[str] = mapped_column(
        String(100),
        default=""
    )

    experience_level: Mapped[str] = mapped_column(
        String(100),
        default=""
    )

    salary: Mapped[str] = mapped_column(
        String(255),
        default=""
    )

    source: Mapped[str] = mapped_column(
        String(100),
        index=True
    )

    source_url: Mapped[str] = mapped_column(
        String(1000),
        unique=True
    )

    published_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    collected_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )