import datetime
import typing

from sqlalchemy import ForeignKey, String
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole

class Cart(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
 
    # user User? @relation(fields: [userId], references: [id])
    # userId Int? @unique
 
    # token String
 
    # totalAmount Int @default(0)

#     cartItems CartItem[]
 
#     createdAt DateTime @default(now())
#     updatedAt DateTime @updatedAt

class CartItem(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    
#     productItem ProductItem @relation(fields: [productItemId], references: [id])
#     productItemId Int

#     cart Cart @relation(fields: [cartId], references: [id])
#     cartId Int

#     quantity Int

#     ingridients Ingredient[]

#     createdAt DateTime @default(now())
#     updatedAt DateTime @updatedAt