from fastapi import APIRouter, Depends, HTTPException

from backend.models.models import User
from backend.src.auth.shemas import CreateUser, Login
from backend.src.auth.utilits import hashed_password, verify_password, generate_jwt_token
from backend.src.database import get_session

from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.utilits import get_user_by_username, get_current_user

auth = APIRouter(prefix='/auth', tags=['auth'])


@auth.post('/register')
async def create_user(new_user: CreateUser, db: AsyncSession = Depends(get_session)):
    hash_password = await hashed_password(new_user.password)
    user = User(username=new_user.username, email=new_user.email, password=hash_password)
    try:
        db.add(user)
        await db.commit()
        return user
    except:
        raise HTTPException(status_code=400, detail='user is exist')


@auth.post('/login')
async def login(user_login: Login):
    user = await get_user_by_username(user_login.username)
    if await verify_password(user_login.password, user.password):
        token = await generate_jwt_token({'sub': user.username})
        return {'access_token': token, 'token_type': 'bearer'}
    else:
        raise HTTPException(status_code=403, detail='username or password is invalid')


@auth.get('/me')
async def get_user_me(current_user: User = Depends(get_current_user)):
    return current_user
