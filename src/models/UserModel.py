import datetime
import typing
from typing import Optional

from sqlalchemy import String, DateTime, Enum
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.enum.UserEnum import UserRole

if typing.TYPE_CHECKING:
    from src.models.OrdersModel import Order
    from src.models.CartModel import Cart
    from src.models.VerificationModel import VereficationCode

tz = datetime.timezone('UTC')

class User(Base):
     __tablename__ = "user_table"

     id: Mapped[int] = mapped_column(primary_key=True)
     fullName: Mapped[str]
     email: Mapped[str] = mapped_column(String, unique=True)
     password: Mapped[str]
     role: Mapped[UserRole] = mapped_column(Enum(OrderStatus), nullable=False, default=UserRole.USER)
     verified: Mapped[datetime.date]

     provider: Mapped[str]
     providerId: Mapped[Optional[str | None]] = mapped_column(String, nullable=True)
     orders: Mapped[list["Order"]] = relationship(back_populates="user", uselist=True)    
     cart: Mapped["Cart"] = relationship(back_populates="user", uselist=False, nullable=True)
     vereficationCode: Mapped["VereficationCode"] = relationship(back_populates="user", uselist=False, nullable=True)

    #  createdAt: Mapped[DateTime] = mapped_column(default=datetime.datetime.now(datetime.timezone.utc)) 
    #  updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.datetime.now(datetime.timezone.utc))