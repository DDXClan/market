from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
load_dotenv()

DATA_BASE_URL = os.environ["DATA_BASE_URL"]
ALGORITHM = os.environ['ALGORITHM']
SECRET_KEY = os.environ['SECRET_KEY']
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')