from datetime import datetime

from sqlalchemy import String, TIMESTAMP, Boolean, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):

    __tablename__ = "account_user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(
        String, nullable=False,
        info={"verbose_name": "email"}
    )
    username: Mapped[str] = mapped_column(
        String, nullable=False,
        info={"verbose_name": "username"}
    )
    created: Mapped[str] = mapped_column(
        TIMESTAMP, default=datetime.utcnow,
        info={"verbose_name": "created"}
    )
    modified: Mapped[str] = mapped_column(
        TIMESTAMP,  default=datetime.utcnow,
        info={"verbose_name": "modified"}
    )
    password: Mapped[str] = mapped_column(
        String, nullable=False,
        info={"verbose_name": "password"}
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=False,
        info={"verbose_name": "is active"}
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False,
        info={"verbose_name": "is superuser"}
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False,
        info={"verbose_name": "is verified"}
    )
