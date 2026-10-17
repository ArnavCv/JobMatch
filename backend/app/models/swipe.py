from datetime import datetime

from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    ForeignKey,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Swipe(Base):
    __tablename__ = "swipes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id"),
        nullable=False
    )

    action: Mapped[bool] = mapped_column(Boolean, nullable=False)

    created_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("now()")
    )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "job_id",
            name="uq_swipe_user_job"
        ),
    )
