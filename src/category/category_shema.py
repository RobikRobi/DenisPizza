import datetime
import typing

from sqlalchemy import DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole

if typing.TYPE_CHECKING:
    from src.product.product_shema import Product


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    products: Mapped[list["Product"]]  = relationship(back_populates="category", uselist=True) 

    
    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())
