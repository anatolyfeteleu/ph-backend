import datetime

from sqlalchemy import TIMESTAMP, BigInteger
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import functions

from src.config import TZ


class BaseModelMixin(object):

    id: Mapped[int] = mapped_column(
        BigInteger,
        autoincrement=True, primary_key=True
    )

    created: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False,
        default=functions.now,
        server_default=functions.now(tz=TZ),
        info={"verbose_name": "created"}
    )
    modified: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False,
        default=functions.now,
        server_default=functions.now(tz=TZ),
        onupdate=functions.now,
        info={"verbose_name": "modified"}
    )
