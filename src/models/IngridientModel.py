import typing
import datetime

from sqlalchemy import DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


if typing.TYPE_CHECKING:
    from src.models.ProductModel import Product
    from src.models.CartModel import CartItem


class Ingredient(Base):
    __tablename__ = 'ingredients_tabel'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    imageURL: Mapped[str]

    products: Mapped[list["Product"]] = relationship(secondary="product_ingredients", back_populates="ingredients")#     products Product[]

    cartItems: Mapped[list["CartItem"]] = relationship(back_populates="ingredient")#     cartItems CartItem[]

    # createdAt: Mapped[DateTime] = mapped_column(default=datetime.datetime.now(datetime.timezone.utc)) 
    # updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.datetime.now(datetime.timezone.utc))


