from datetime import datetime

from sqlalchemy import TIMESTAMP, String, text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text('now()')
    )

    __table_args__ = (
        CheckConstraint(
            "role IN ('job_seeker', 'recruiter')",
            name="check_user_role"
        ),
    )
