import jwt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, JSON, Integer, ForeignKey, TIMESTAMP, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
import uuid
from datetime import datetime
from settings import DATA_BASE_URL, SECRET_KEY, ALGORITHM, oauth2sheme
from fastapi import Depends

async_engine = create_async_engine(DATA_BASE_URL)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


Base = declarative_base()


class Role(Base):
    __tablename__ = 'Roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, nullable=False)


class User(Base):
    __tablename__ = 'User'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    role_id = Column(ForeignKey(Role.id))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, nullable=False, unique=True)


class Brand(Base):
    __tablename__ = 'Brand'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_name = Column(String, nullable=False, unique=True)


class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    category_id = Column(ForeignKey(Category.id))
    brand_id = Column(ForeignKey(Brand.id))
    quantity = Column(Integer)
    cost = Column(Integer, nullable=False)


class Basket(Base):
    __tablename__ = 'Basket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(User.id), nullable=True)
    product_id = Column(ForeignKey(Product.id), nullable=True)


class FollowProducts(Base):
    __tablename__ = 'FollowProducts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(User.id), nullable=True)
    product_id = Column(ForeignKey(Product.id), nullable=True)


class PurchaseHistory(Base):
    __tablename__ = 'PurchaseHistory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(User.id), nullable=True)
    product_id = Column(ForeignKey(Product.id), nullable=True)
    sold_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)


async def get_user_by_username(session: AsyncSession, username: str) -> User:
    result = await session.execute(select(User).where(User.username == username))
    return result.scalar_one()


async def verify_jwt_token(token: str) -> dict:
    try:
        decode_data = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return decode_data
    except jwt.PyJWTError:
        return None


async def get_user_by_jwt(token: str = Depends(oauth2sheme),
                          db: AsyncSession = Depends(get_session)) -> User:
    decode_data = await verify_jwt_token(token)
    result = await get_user_by_username(db, decode_data.get('sub'))
    return result


