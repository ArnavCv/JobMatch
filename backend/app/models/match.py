from datetime import datetime

from sqlalchemy import (
    TIMESTAMP,
    ForeignKey,
    String,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="matched"
    )

    created_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("now()")
    )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "job_id",
            name="uq_match_user_job"
        ),
    )
