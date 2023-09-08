from fastapi import FastAPI
import uvicorn

from backend.src.auth.auth import auth

app = FastAPI()
app.include_router(auth)


if __name__ == '__main__':
    uvicorn.run(app)