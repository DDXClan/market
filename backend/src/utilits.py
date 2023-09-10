import jwt

from backend.models.models import User
from backend.src.database import async_session
from sqlalchemy import select
from fastapi import HTTPException, Depends

from backend.src.settings import SECRET_KEY, ALGORITHM, oauth2_scheme


async def get_user_by_username(username):
    async with async_session() as session:
        try:
            result = await session.execute(select(User).where(User.username == username))
            user = result.scalar()
            return user
        except:
            raise HTTPException(status_code=404, detail='user not found')


async def verify_jwt_token(token: str):
    try:
        decode_data = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return decode_data
    except:
        return HTTPException(status_code=403, detail='token invalid')


async def get_current_user(token: str = Depends(oauth2_scheme)):
    decode_data = await verify_jwt_token(token)
    user = await get_user_by_username(decode_data['sub'])
    return user
