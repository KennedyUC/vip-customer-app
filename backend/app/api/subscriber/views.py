from db.db import db_session
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .schema import CreateSubscriberSchema
from .services import SubscriberService

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def subscribe_email(email: CreateSubscriberSchema, session: AsyncSession = Depends(db_session)):
    """
    Example of request body

    {

        "email" : "huzzy@api.com"

    }
    """
    await SubscriberService(session).subscribe_email(email)

    return {
        "status": "success"
    }
