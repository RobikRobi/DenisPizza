import datetime
import typing

from sqlalchemy import DateTime, ForeignKey, String, JSON
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole
from src.orders.orders_enum import OrderStatus

if typing.TYPE_CHECKING:
    from src.user.user_models import User

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    userId: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)# userId Int?

    user: Mapped["User"] = relationship(back_populates="orders")# user: User? @relation(fields: [userId], references: [id])
    

    token: Mapped[str]# token String

    totalAmout: Mapped[int]# totalAmount Int 
    status: Mapped[OrderStatus]# status OrderStatus
    paymenId: Mapped[str | None] = mapped_column(String, nullable=True)# paymentId String?

    orderItem: Mapped[JSON]# orderItems Json

    fullName: Mapped[str]# fullName String
    email: Mapped[str]# email String
    phone: Mapped[str]# phone String
    adress: Mapped[str]# address String
    comment: Mapped[str | None] = mapped_column(nullable=True)# comment String?    

    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())
