from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class SaleItemBase(BaseModel):
    sale_id: UUID
    product_id: UUID
    quantity: int
    unit_price: Decimal
    discount_amount: Decimal | None = None
    total_price: Decimal


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemUpdate(BaseModel):
    quantity: int | None = None
    unit_price: Decimal | None = None
    discount_amount: Decimal | None = None
    total_price: Decimal | None = None


class SaleItemRead(SaleItemBase):
    model_config = ConfigDict(from_attributes=True)

    sale_item_id: UUID
