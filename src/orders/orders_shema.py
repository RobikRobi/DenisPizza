import datetime
import typing

from sqlalchemy import DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole

class Order(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    # user: User? @relation(fields: [userId], references: [id])
    # userId Int?

    # token String

    # totalAmount Int 
    # status OrderStatus
    # paymentId String?

    # orderItems Json

    # fullName String
    # email String
    # phone String
    # address String
    # comment String?    

    createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())
    updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())
