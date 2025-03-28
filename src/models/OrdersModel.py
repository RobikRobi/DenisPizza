import datetime
import typing

from sqlalchemy import DateTime, ForeignKey, String, JSON, Enum
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.enum.OrdersEnum import OrderStatus

if typing.TYPE_CHECKING:
    from src.models.UserModel import User

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    userId: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)# userId Int?

    user: Mapped["User"] = relationship(back_populates="orders")# user: User? @relation(fields: [userId], references: [id])
    

    token: Mapped[str]# token String

    totalAmout: Mapped[int]# totalAmount Int 
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), nullable=False)# status OrderStatus
    paymenId: Mapped[str | None] = mapped_column(String, nullable=True)# paymentId String?

    order_items: Mapped[dict] = mapped_column(JSON, nullable=False)# orderItems Json

    fullName: Mapped[str]# fullName String
    email: Mapped[str]# email String
    phone: Mapped[str]# phone String
    adress: Mapped[str]# address String
    comment: Mapped[str | None] = mapped_column(nullable=True)# comment String?    

    # createdAt: Mapped[DateTime] = mapped_column(default=datetime.datetime.now(datetime.timezone.utc)) 
    # updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.datetime.now(datetime.timezone.utc))