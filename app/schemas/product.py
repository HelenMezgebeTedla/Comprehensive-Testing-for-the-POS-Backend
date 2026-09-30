from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: Decimal
    quantity: int
    category_id: UUID | None = None
    supplier_id: UUID | None = None
    barcode: str | None = None
    is_active: bool | None = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = None
    price: Decimal | None = None
    quantity: int | None = None
    category_id: UUID | None = None
    supplier_id: UUID | None = None
    barcode: str | None = None


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    product_id: UUID
    created_at: datetime
