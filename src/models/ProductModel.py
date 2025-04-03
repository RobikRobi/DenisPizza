import datetime
import typing

from sqlalchemy import DateTime, ForeignKey
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


if typing.TYPE_CHECKING:
    from src.models.IngridientModel import Ingredient
    from src.models.CategoryModel import Category
    from src.models.CartModel import CartItem


class Product(Base):
    __tablename__ = 'product_tabel'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str]
    imageURL: Mapped[str]

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
    category: Mapped["Category"]  = relationship(back_populates="products", uselist=False) 

    ingredients: Mapped[list["Ingredient"]] = relationship('Ingredient', secondary='product_ingredients', back_populates='products')
    items: Mapped[list["ProductItem"]] = relationship('ProductItem', back_populates='product')

    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())# 

class ProductItem(Base):
    __tablename__ = 'product_item'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    price: Mapped[int]
    size: Mapped[int] = mapped_column(nullable=True)#Int?
    pizzaType: Mapped[int] = mapped_column(nullable=True)

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', nullable=False))
    product: Mapped["Product"] = relationship(back_populates='items', uselist=False)

    cart_items: Mapped["CartItem"] = relationship(back_populates="product_item")


    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())# 