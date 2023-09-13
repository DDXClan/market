from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from models.database import get_session, Product, Category, Brand
from sqlalchemy import select

item = APIRouter(prefix='/item', tags=['item'])


class CreateItem(BaseModel):
    product_name: str
    description: str
    quantity: int
    cost: int
    category_id: int
    brand_id: int


@item.post('/create')
async def create_item(new_item: CreateItem, db: AsyncSession = Depends(get_session)):
    product = Product(product_name=new_item.product_name, description=new_item.description,
                      quantity=new_item.quantity, cost=new_item.cost, category_id=new_item.category_id)
    try:
        db.add(product)
        await db.commit()
        return {'message': 'Success'}
    except:
        raise HTTPException(status_code=400, detail='data invalid')


class AddCategoryOrBrand(BaseModel):
    name: str


@item.post('/add_category')
async def create_category(add_category: AddCategoryOrBrand, db: AsyncSession = Depends(get_session)):
    category = Category(category_name=add_category.name)
    try:
        db.add(category)
        await db.commit()
        return {'message': 'Success'}
    except:
        raise HTTPException(status_code=400, detail='category is exist')


@item.post('/add_brand')
async def create_brand(add_brand: AddCategoryOrBrand, db: AsyncSession = Depends(get_session)):
    brand = Brand(brand_name=add_brand.name)
    try:
        db.add(brand)
        await db.commit()
        return {'message': 'Success'}
    except:
        raise HTTPException(status_code=400, detail='brand is exist')


@item.get('/all')
async def get_all_item(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Product))
    items = result.scalars().all()
    return items


@item.get('/search={search}')
async def get_items_by_name(search: str, db: AsyncSession = Depends(get_session)):
    try:
        result = await db.execute(select(Product).where(Product.product_name.like(f'%{search}%')))
        return result.scalars().all()
    except:
        raise HTTPException(status_code=404, detail='item not found')


@item.get('/{item_id}')
async def get_item_by_id(item_id: int, db: AsyncSession = Depends(get_session)):
    try:
        result = await db.execute(select(Product).where(Product.id == item_id))
        return result.scalar_one()
    except:
        raise HTTPException(status_code=404, detail='item not found')


@item.get('/category/{category_id}')
async def get_items_by_category(category_id: int, db: AsyncSession = Depends(get_session)):
    try:
        result = await db.execute(select(Product).where(Product.category_id == category_id))
        return result.scalars().all()
    except:
        raise HTTPException(status_code=404, detail='category not found')
