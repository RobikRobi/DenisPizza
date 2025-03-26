import datetime
import typing
from typing import Optional

from sqlalchemy import String, DateTime 
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole

if typing.TYPE_CHECKING:
    from orders.orders_models import Order
    from cart.cart_models import Cart
    from src.verefication.verification_models import VereficationCode

class User(Base):
     __tablename__ = "user_table"

     id: Mapped[int] = mapped_column(primary_key=True)
     fullName: Mapped[str]
     email: Mapped[str] = mapped_column(String, unique=True)
     password: Mapped[str]
     role: Mapped[UserRole] = mapped_column(default=UserRole.USER) 
     verified: Mapped[datetime.date]

     provider: Mapped[str]
     providerId: Mapped[Optional[str | None]] = mapped_column(String, nullable=True)
     orders: Mapped[list["Order"]] = relationship(back_populates="user", uselist=True)    
     cart: Mapped["Cart"] = relationship(back_populates="user", uselist=False, nullable=True)
     vereficationCode: Mapped["VereficationCode"] = relationship(back_populates="user", uselist=False, nullable=True)

     createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())
     updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())