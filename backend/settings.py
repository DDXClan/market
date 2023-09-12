import os
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

load_dotenv()

DATA_BASE_URL = os.environ['DATA_BASE_URL']
SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']
oauth2sheme = OAuth2PasswordBearer('/user/login')

