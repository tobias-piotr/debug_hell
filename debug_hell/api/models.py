import uuid

from pydantic import BaseModel


class Demon(BaseModel):
    """Demon model."""

    id: uuid.UUID
    name: str

    class Config:
        orm_mode = True


class DemonCreatePayload(BaseModel):
    """Demon create payload."""

    name: str
