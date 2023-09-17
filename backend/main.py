from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routers.user import user
from routers.item import item
app = FastAPI()
app.include_router(user)
app.include_router(item)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники (не рекомендуется в продакшн)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host='26.8.118.81')