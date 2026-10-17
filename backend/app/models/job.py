from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    recruiter_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("now()")
    )
