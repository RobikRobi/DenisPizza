import datetime
import typing
from typing import Optional

from sqlalchemy import String, DateTime, Enum
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.enum.UserEnum import UserRole
from sqlalchemy.sql import func

if typing.TYPE_CHECKING:
    from src.models.OrdersModel import Order
    from src.models.CartModel import Cart
    from src.models.VerificationModel import VereficationCode

tz = datetime.timezone('UTC')

class User(Base):
     __tablename__ = "user_table"

     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
     fullName: Mapped[str]
     email: Mapped[str] = mapped_column(String, unique=True)
     password: Mapped[str]
     role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.USER)
     verified: Mapped[datetime.date]

     provider: Mapped[str]
     providerId: Mapped[Optional[str]] = mapped_column(nullable=True)
     orders: Mapped[list["Order"]] = relationship(back_populates="user", uselist=True)    
     cart: Mapped["Cart"] = relationship(back_populates="user", uselist=False, nullable=True)
     vereficationCode: Mapped["VereficationCode"] = relationship(back_populates="user", uselist=False, nullable=True)

     createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())#     createdAt DateTime @default(now())
     updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())# 