from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    name: str
    description: str | None = None
    is_active: bool | None = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_active: bool | None = True


class CategoryRead(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    category_id: UUID
