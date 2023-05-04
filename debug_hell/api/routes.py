from typing import Annotated

import sqlalchemy as sa
from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from debug_hell.api import models
from debug_hell.database import models as db_models
from debug_hell.database.session import get_session

router = APIRouter(tags=["demons"], prefix="/demons")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_demon(
    db_session: Annotated[AsyncSession, Depends(get_session)],
    body: models.DemonCreatePayload = Body(...),
) -> models.Demon:
    """Create a new demon."""
    demon = db_models.Demon(**body.dict())
    db_session.add(demon)
    await db_session.commit()
    await db_session.refresh(demon)
    return models.Demon.from_orm(demon)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_demons(
    db_session: Annotated[AsyncSession, Depends(get_session)],
) -> list[models.Demon]:
    """Get the list of demons."""
    result = await db_session.execute(sa.select(db_models.Demon))
    return [models.Demon.from_orm(demon) for demon in result.scalars()]
