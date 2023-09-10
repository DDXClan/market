from pydantic import EmailStr, BaseModel


class AddCategory(BaseModel):
    category_name: str


class AddBrand(BaseModel):
    brand_name: str


class AddProduct(BaseModel):
    product_name: str
    description: str
    category_id: int
    brand_id: int
    cost: int

    class Config:
        from_attributes = True
