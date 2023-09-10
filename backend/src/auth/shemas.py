from pydantic import EmailStr, BaseModel


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class Login(BaseModel):
    username: str
    password: str
