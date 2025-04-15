import typing
import datetime

from sqlalchemy import DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


if typing.TYPE_CHECKING:
    from src.models.ProductModel import Product
    from src.models.CartModel import CartItem


class Ingredient(Base):
    __tablename__ = 'ingredients_table'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    price: Mapped[int]
    imageURL: Mapped[str]

    products: Mapped[list["Product"]] = relationship(secondary="product_ingredients", back_populates="ingredients")#     products Product[]

    cart_items: Mapped[list["CartItem"]] =  relationship(secondary="cartItem_ingredients", back_populates="ingredients")#     cartItems CartItem[]

    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())# 


