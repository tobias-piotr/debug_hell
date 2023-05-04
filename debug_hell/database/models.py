import uuid

import sqlalchemy as sa
from sqlalchemy import orm


class Base(orm.DeclarativeBase):
    """Base database model."""


class Demon(Base):
    """Demon database model."""

    __tablename__ = "demon"

    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        default=uuid.uuid4,
        primary_key=True,
    )
    name: orm.Mapped[str] = orm.mapped_column(sa.String(63))
