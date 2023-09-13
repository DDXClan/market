import jwt
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from models.database import get_session, User, get_user_by_username, get_user_by_jwt
import bcrypt
from datetime import timedelta, datetime
from settings import SECRET_KEY, ALGORITHM

user = APIRouter(prefix='/user', tags=['User'])
EXPIRATION_TIME = timedelta(minutes=60)


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str


async def generate_hash_password(password) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


@user.post('/registration')
async def registration(new_user: CreateUser, db: AsyncSession = Depends(get_session)):
    user_created = User(username=new_user.username, email=new_user.email,
                        password=await generate_hash_password(new_user.password))
    try:
        db.add(user_created)
        await db.commit()
        return {'message': 'Success'}
    except:
        raise HTTPException(status_code=400, detail='user is exist')


class LoginUser(BaseModel):
    username: str
    password: str


async def verify_password(password, hashed_password) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


async def generate_jwt_token(data: dict) -> str:
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({'exp': expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


@user.post('/login')
async def login(login_user: LoginUser, db: AsyncSession = Depends(get_session)):
    try:
        auth_user = await get_user_by_username(db, login_user.username)
        if await verify_password(login_user.password, auth_user.password):
            token = await generate_jwt_token({'sub': auth_user.username})
            return {'token': token, 'type': 'bearer'}
        else:
            raise HTTPException(status_code=403, detail='invalid username or password')
    except:
        raise HTTPException(status_code=403, detail='invalid username or password')


@user.get('/me')
async def local_info(current_user: User = Depends(get_user_by_jwt)):
    return current_user
