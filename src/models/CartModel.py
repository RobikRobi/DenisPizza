import datetime
import typing

from sqlalchemy import ForeignKey, Integer, DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


if typing.TYPE_CHECKING:
    from src.models.UserModel import User
    from src.models.ProductModel import ProductItem
    from src.models.IngridientModel import Ingredient


class Cart(Base):
    __tablename__ = 'cart_table'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
 
    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)# userId Int? @unique
    user: Mapped["User"] = relationship(back_populates="cart", uselist=False)# user User? @relation(fields: [userId], references: [id])
    
    token: Mapped[str]# token String
    totalAmount: Mapped[int] = mapped_column(nullable=True, default=0)# totalAmount Int @default(0)
    cart_items: Mapped[list["CartItem"]] = relationship(back_populates="cart", uselist=True)#     cartItems CartItem[]
    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())#     updatedAt DateTime @updatedAt

class CartItem(Base):
    __tablename__ = 'cart_item'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    product_item: Mapped["ProductItem"] = relationship("ProductItem", back_populates="cart_items")#     productItem ProductItem @relation(fields: [productItemId], references: [id])
    product_item_id: Mapped[int] = mapped_column(ForeignKey('product_items.id'), nullable=False)#     productItemId Int

    cart: Mapped["Cart"] = relationship(back_populates="cart_items", uselist=False)#     cart Cart @relation(fields: [cartId], references: [id])
    cartId: Mapped[int] = mapped_column(ForeignKey('cart_table.id'), nullable=False)#     cartId Int

    quantity: Mapped[int]#     quantity Int

    ingredients: Mapped[list["Ingredient"]] = relationship(secondary="icartItem_ingredients", back_populates="cart_items", uselist=True)#     ingridients Ingredient[]

    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())#     updatedAt DateTime @updatedAt



    
    class CartItemIngredient(Base):
        __tablename__ = "cartItem_ingredients"
        cart_item_id: Mapped[int] = mapped_column(ForeignKey("cart_item.id"), primary_key=True)
        ingredients_id: Mapped[int] = mapped_column(ForeignKey("ingredients_table.id"), primary_key=True)