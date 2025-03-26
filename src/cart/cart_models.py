import datetime
import typing

from sqlalchemy import ForeignKey, String, Integer, DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole


if typing.TYPE_CHECKING:
    from src.user.user_models import User
    from src.product.product_models import ProductItem
    from src.ingridient.ingridient_models import Ingredient

class Cart(Base):
    __tablename__ = 'cart_table'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
 
    userId: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True, unique=True)# userId Int? @unique
    user: Mapped["User"] = relationship(back_populates="cart", uselist=False)# user User? @relation(fields: [userId], references: [id])
    
    token: Mapped[str]# token String
    totalAmout: Mapped[int | None] = mapped_column(Integer, nullable=False, default=0)# totalAmount Int @default(0)
    cart_items: Mapped[list["CartItem"]] = relationship(back_populates="cart", uselist=True)#     cartItems CartItem[]
    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())#     updatedAt DateTime @updatedAt

class CartItem(Base):
    __tablename__ = 'cart_item'
    id: Mapped[int] = mapped_column(primary_key=True)
    
    product_item: Mapped["ProductItem"] = relationship("ProductItem", back_populates="cart_items")#     productItem ProductItem @relation(fields: [productItemId], references: [id])
    product_item_id: Mapped[int] = mapped_column(ForeignKey('product_items.id'), nullable=False)#     productItemId Int

    cart: Mapped["Cart"] = relationship(back_populates="cart_items", uselist=False)#     cart Cart @relation(fields: [cartId], references: [id])
    cartId: Mapped[int]#     cartId Int

    quantity: Mapped[int]#     quantity Int

    ingridients: Mapped[list["Ingredient"]] = relationship(secondary="ingredients_tabel", back_populates="cart_items", uselist=True)#     ingridients Ingredient[]

    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())#     updatedAt DateTime @updatedAt