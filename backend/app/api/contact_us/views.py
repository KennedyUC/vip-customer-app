from db.db import db_session
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .schema import ContactUsSchema
from .services import ContatctUsService

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def contact_us(
        query: ContactUsSchema,
        session: AsyncSession = Depends(db_session)):

    response = await ContatctUsService(session).contact_us_create(query)
    if response:
        return {
            "status": "success"
        }
