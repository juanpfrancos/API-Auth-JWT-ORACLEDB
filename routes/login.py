from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from queries import auth_user, get_auth_user
from config import SECRET_KEY
from models.user import UserLogin


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

login = APIRouter(tags=['Users'])

# Setup OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Generate JWT
def create_access_token(data: dict, expires_delta: int):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Decode jwt and verify authenticated user
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    user = get_auth_user(username)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return user


# Get access token
@login.post("/login")
def login_for_access_token(login_credentials: UserLogin):
    user = auth_user(login_credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user["USERNAME"]}, expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {"access_token": access_token, "token_type": "bearer"}