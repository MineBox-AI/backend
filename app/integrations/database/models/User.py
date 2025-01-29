from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    auth0_id: str = Field(nullable=False, unique=True, index=True)
    name: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True, index=True)
