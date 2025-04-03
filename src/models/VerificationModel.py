import datetime
import typing


from sqlalchemy import DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

if typing.TYPE_CHECKING:
    from src.models.UserModel import User


class VereficationCode(Base):
    __tablename__ = 'verification_table'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user: Mapped["User"] = relationship(back_populates="vereficationCode", uselist=False)

    userId: Mapped[int] = mapped_column(unique=True)

    code: Mapped[str]
    
    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())#     createdAt DateTime @default(now())
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())# 