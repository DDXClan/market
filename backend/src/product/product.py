from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models.models import Category, Brand, Product
from backend.src.database import get_session
from backend.src.product.shemas import AddCategory, AddBrand, AddProduct

products = APIRouter(prefix='/products', tags=['product'])


# current_user: User = Depends(get_current_user)
@products.post('/add_category')
async def create_category(new_category: AddCategory, db: AsyncSession = Depends(get_session)):
    category = Category(category_name=new_category.category_name)
    try:
        db.add(category)
        await db.commit()
        return category
    except:
        raise HTTPException(status_code=400, detail='category is exist')


@products.post('/add_brand')
async def create_brand(new_brand: AddBrand, db: AsyncSession = Depends(get_session)):
    brand = Brand(brand_name=new_brand.brand_name)
    try:
        db.add(brand)
        await db.commit()
        return brand
    except:
        raise HTTPException(status_code=400, detail='brand is exist')


@products.post('/add_product')
async def create_product(new_product: AddProduct, db: AsyncSession = Depends(get_session)):
    product = Product(product_name=new_product.product_name, description=new_product.description,
                      category_id=new_product.category_id, brand_id=new_product.brand_id, cost=new_product.cost)
    try:
        db.add(product)
        await db.commit()
        return product
    except:
        raise HTTPException(status_code=400, detail='product is exist')
