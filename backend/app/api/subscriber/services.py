from db.db import db_session
from db.models.history import History
from db.models.subscribers import Subscriber
from fastapi import Depends, HTTPException, status
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession



class SubscriberService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def subscribe_email(self, info):
        try:
            email = info.dict()['email']
        except:
            raise HTTPException(detail="No email provided", status_code=status.HTTP_400_BAD_REQUEST)

        statement = select(Subscriber).where(Subscriber.email == email)

        check = await self.session.execute(statement)

        if check.scalars().first():
            raise HTTPException(detail="Email is already Subscribed", status_code= status.HTTP_403_FORBIDDEN)

        

        new_email = Subscriber(email=email)
        self.session.add(new_email)
        await self.session.commit()
        await self.session.refresh(new_email)

        return True

