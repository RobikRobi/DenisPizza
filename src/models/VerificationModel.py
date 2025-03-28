import datetime
import typing


from sqlalchemy import DateTime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if typing.TYPE_CHECKING:
    from src.models.UserModel import User


class VereficationCode(Base):
    __tablename__ = 'verification_table'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user: Mapped["User"] = relationship(back_populates="vereficationCode", uselist=False)

    userId: Mapped[int] = mapped_column(unique=True)

    code: Mapped[str]
    
    # createdAt: Mapped[DateTime] = mapped_column(default=datetime.datetime.now(datetime.timezone.utc)) 
    # updatedAt: Mapped[DateTime] = mapped_column(onupdate=datetime.datetime.now(datetime.timezone.utc))