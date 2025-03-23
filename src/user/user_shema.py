import datetime
import typing
from typing import Optional

from sqlalchemy import String, DateTime 
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole

class User(Base):
     __tablename__ = "user_table"

     id: Mapped[int] = mapped_column(primary_key=True)
     fullName: Mapped[str]
     email: Mapped[str] = mapped_column(String, unique=True)
     password: Mapped[str]
     role: Mapped[UserRole] = mapped_column(default=UserRole.USER) 
     verified: Mapped[datetime.date]

     provider: Mapped[str]
     providerId: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    # orders Order[]                 
    # cart Cart?
    # vereficationCode VerficationCode?

     createdAt: Mapped[DateTime] = mapped_column(default=datetime.now())
     updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.now())