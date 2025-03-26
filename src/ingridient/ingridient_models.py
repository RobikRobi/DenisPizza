import typing
import datetime

from sqlalchemy import ForeignKey, String, DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole

if typing.TYPE_CHECKING:
    from src.product.product_models import Product
    from src.cart.cart_models import CartItem

class Ingredient(Base):
    __tablename__ = 'ingredients_tabel'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    imageURL: Mapped[str]

    products: Mapped[list["Product"]] = relationship(secondary="product_ingredients", back_populates="ingredients")#     products Product[]

    cartItems: Mapped[list["CartItem"]] = relationship(back_populates="ingredient")#     cartItems CartItem[]

    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())#     updatedAt DateTime @updatedAt


