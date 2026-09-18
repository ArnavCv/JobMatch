from sqlalchemy import TIMESTAMP, Column, Integer, String, text, CheckConstraint
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text('now()')
    )

    __table_args__ = (
        CheckConstraint(
            "role IN ('job_seeker', 'recruiter')",
            name="check_user_role"
        ),
    )