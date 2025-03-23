import datetime
import typing
from typing import Optional

from sqlalchemy import DateTime, ForeignKey
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole


if typing.TYPE_CHECKING:
    from src.ingridient.ingridient_shema import Ingredient
    from src.category.category_shema import Category
    from src.cart.cart_shema import CartItem

class Product(Base):
    __tablename__ = 'product_tabel'
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    imageURL: Mapped[str]

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
    category: Mapped["Category"]  = relationship(back_populates="products", uselist=False) 

    ingredients: Mapped[list["Ingredient"]] = relationship('Ingredient', secondary='product_ingredients', back_populates='products')
    items: Mapped[list["ProductItem"]] = relationship('ProductItem', back_populates='product')

    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())


class ProductItem(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    price: Mapped[int]
    size:Mapped[Optional[int]] #Int?
    Mapped[Optional[int]] = mapped_column(nullable=True)

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', nullable=False))
    product: Mapped["Product"] = relationship(back_populates='items', uselist=False)

    cart_items: Mapped["CartItem"] = relationship(back_populates="productItem")


    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())