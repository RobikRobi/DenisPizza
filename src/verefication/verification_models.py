import datetime
import typing
from typing import Optional

from sqlalchemy import String, DateTime, ForeignKey
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from user.user_enum import UserRole

if typing.TYPE_CHECKING:
    from src.user.user_models import User


class VereficationCode(Base):
    __tablename__ = 'verification_table'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user: Mapped["User"] = relationship(back_populates="vereficationCode", uselist=False)

    userId: Mapped[int] = mapped_column(unique=True)

    code: Mapped[str]
    createdAt:Mapped[DateTime] = mapped_column(default=datetime.now())