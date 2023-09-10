from fastapi import FastAPI, Depends
import uvicorn

from backend.models.models import User
from backend.src.auth.auth import auth
from backend.src.product.product import products
from backend.src.utilits import get_current_user

app = FastAPI()
app.include_router(auth)
app.include_router(products)

if __name__ == '__main__':
    uvicorn.run(app)
