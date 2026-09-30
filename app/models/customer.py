import uuid

from sqlalchemy import UUID, Boolean, Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, autoincrement=False
    )
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_no = Column(String(20), nullable=True)
    address = Column(String(50), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    sale = relationship("Sale", back_populates="customer")
