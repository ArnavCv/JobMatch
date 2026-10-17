from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    skills: Mapped[str | None] = mapped_column(Text, nullable=True)
    experience: Mapped[str | None] = mapped_column(Text, nullable=True)
    profile_picture_path: Mapped[str | None] = mapped_column(String, nullable=True)
    resume_path: Mapped[str | None] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("now()")
    )
