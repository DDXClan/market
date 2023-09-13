from fastapi import FastAPI
import uvicorn
from routers.user import user
from routers.item import item
app = FastAPI()
app.include_router(user)
app.include_router(item)


if __name__ == '__main__':
    uvicorn.run(app)