from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Text, text
from app.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    skills = Column(Text, nullable=True)
    experience = Column(Text, nullable=True)
    profile_picture_path = Column(String, nullable=True)
    resume_path = Column(String, nullable=True)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()")
    )