import os
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime
from dotenv import load_dotenv
from jose import JWTError, jwt
from src.schemas.token_schemas import Token, TokenData

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def create_access_token(data: dict,expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta: expire = datetime.utcnow() + expires_delta
    else: datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({ 'exp': expire })
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username = payload.get('sub')
        if username is None:
            raise JWTError('Could not validate user credentials')
        token_data = TokenData(username)
    except Exception as e:
        print(e)
    