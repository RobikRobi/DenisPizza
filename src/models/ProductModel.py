import datetime
import typing
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Integer
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


if typing.TYPE_CHECKING:
    from src.models.IngridientModel import Ingredient
    from src.models.CategoryModel import Category
    from src.models.CartModel import CartItem


class Product(Base):
    __tablename__ = 'product_tabel'
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    imageURL: Mapped[str]

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
    category: Mapped["Category"]  = relationship(back_populates="products", uselist=False) 

    ingredients: Mapped[list["Ingredient"]] = relationship('Ingredient', secondary='product_ingredients', back_populates='products')
    items: Mapped[list["ProductItem"]] = relationship('ProductItem', back_populates='product')

    # createdAt: Mapped[DateTime] = mapped_column(default=datetime.datetime.now(datetime.timezone.utc)) 
    # updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.datetime.now(datetime.timezone.utc))


class ProductItem(Base):
    __tablename__ = 'product_item'
    
    id: Mapped[int] = mapped_column(primary_key=True)

    price: Mapped[int]
    size: Mapped[int | None] = mapped_column(Integer, nullable=False)#Int?
    pizzaType: Mapped[int | None] = mapped_column(Integer, nullable=False)

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', nullable=False))
    product: Mapped["Product"] = relationship(back_populates='items', uselist=False)

    cart_items: Mapped["CartItem"] = relationship(back_populates="product_item")


    # createdAt: Mapped[DateTime] = mapped_column(default=datetime.datetime.now(datetime.timezone.utc)) 
    # updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.datetime.now(datetime.timezone.utc))