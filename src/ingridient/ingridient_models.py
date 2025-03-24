import typing

from sqlalchemy import ForeignKey, String
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole

class Ingredient(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    imageURL: Mapped[str]

#     products Product[]

#     cartItems CartItem[]

#     createdAt DateTime @default(now())
#     updatedAt DateTime @updatedAt

