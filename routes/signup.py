from fastapi import APIRouter, HTTPException, status
from models.user import UserSignUp
from config import pwd_context
from queries import verify_user_exist, signup_user
import uuid
import codecs

signup = APIRouter(tags=['Users'])


@signup.post("/signup", response_model=UserSignUp, status_code=status.HTTP_201_CREATED)
async def user(input_user: UserSignUp):
    user = verify_user_exist(input_user.username, input_user.email)
    if user != None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User already exists")
    try:
        user_dict = dict(input_user)
        user_dict.update({"password":pwd_context.encrypt(input_user.password),"id":codecs.decode(uuid.uuid4().hex, 'hex')})
        signup_user(user_dict)
        del user_dict["id"]
        return UserSignUp(**user_dict)
    except Exception as e:
        return {"error": f"User not created {str(e)}"}