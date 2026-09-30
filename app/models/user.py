import enum
import uuid

from sqlalchemy import (
    UUID,
    Boolean,
    Column,
    DateTime,
    Enum,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class UserRole(str, enum.Enum):
    CASHIER = "cashier"
    STORE_MANAGER = "store_manager"


class User(Base):
    __tablename__ = "users"

    user_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, autoincrement=False
    )
    username = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    role = Column(Enum(UserRole, name="user_role_enum"), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    hashed_password = Column(String(200), nullable=False)

    sales = relationship("Sale", back_populates="user")
