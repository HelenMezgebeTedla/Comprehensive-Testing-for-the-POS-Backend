from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.user import UserRole


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    role: UserRole
    is_active: bool | None = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    role: UserRole | None = None
    is_active: bool | None = True


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    user_id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime
