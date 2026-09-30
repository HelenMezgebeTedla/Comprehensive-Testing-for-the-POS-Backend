from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.sale import SalesStatus


class SalesBase(BaseModel):
    customer_id: UUID
    user_id: UUID
    sale_date: datetime
    subtotal: Decimal
    tax_amount: Decimal
    discount_amount: Decimal | None = None
    total_amount: Decimal
    status: SalesStatus


class SalesCreate(SalesBase):
    pass


class SalesUpdate(BaseModel):
    customer_id: UUID
    user_id: UUID
    sale_date: datetime | None = None
    subtotal: Decimal | None = None
    tax_amount: Decimal | None = None
    discount_amount: Decimal | None = None
    total_amount: Decimal | None = None
    status: SalesStatus | None = None


class SalesRead(SalesBase):
    model_config = ConfigDict(from_attributes=True)

    sale_id: UUID
    sale_date: datetime
