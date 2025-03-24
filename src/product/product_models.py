import datetime
import typing
from typing import Optional

from sqlalchemy import DateTime, ForeignKey
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole


if typing.TYPE_CHECKING:
    from ingridient.ingridient_models import Ingredient
    from category.category_models import Category
    from cart.cart_models import CartItem

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
    __tablename__ = 'product_item'
    id: Mapped[int] = mapped_column(primary_key=True)

    price: Mapped[int]
    size:Mapped[Optional[int]] #Int?
    Mapped[Optional[int]] = mapped_column(nullable=True)

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', nullable=False))
    product: Mapped["Product"] = relationship(back_populates='items', uselist=False)

    cart_items: Mapped["CartItem"] = relationship(back_populates="product_item")


    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())