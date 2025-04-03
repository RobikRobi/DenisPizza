import datetime
import typing

from sqlalchemy import DateTime, ForeignKey, String, JSON, Enum
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from src.enum.OrdersEnum import OrderStatus

if typing.TYPE_CHECKING:
    from src.models.UserModel import User

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    userId: Mapped[int] = mapped_column(ForeignKey('users.id'))# userId Int? nullable=True

    user: Mapped["User"] = relationship(back_populates="orders")# user: User? @relation(fields: [userId], references: [id])
    

    token: Mapped[str]# token String

    totalAmout: Mapped[int]# totalAmount Int 
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus))# status OrderStatus
    paymenId: Mapped[str] = mapped_column(nullable=True)# paymentId String?

    order_items: Mapped[dict] = mapped_column(JSON, nullable=False)# orderItems Json

    fullName: Mapped[str]# fullName String
    email: Mapped[str]# email String
    phone: Mapped[str]# phone String
    adress: Mapped[str]# address String
    comment: Mapped[str] = mapped_column(nullable=True)# comment String?    

    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())# 