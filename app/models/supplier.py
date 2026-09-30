import uuid

from sqlalchemy import UUID, Boolean, Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, autoincrement=False
    )
    company_name = Column(String(50), nullable=False)
    contact_name = Column(String(50), nullable=True)
    email = Column(String, unique=True, nullable=False)
    supplier_phone = Column(String(20), unique=True, nullable=True)
    address = Column(String(50), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    products = relationship("Product", back_populates="supplier")
