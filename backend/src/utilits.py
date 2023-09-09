from backend.models.models import User
from backend.src.database import async_session
from sqlalchemy import select
from fastapi import HTTPException


async def get_user_by_username(username):
    async with async_session() as session:
        try:
            result = await session.execute(select(User).where(User.username == username))
            user = result.scalar()
            return user
        except:
            raise HTTPException(status_code=404, detail='user not found')
