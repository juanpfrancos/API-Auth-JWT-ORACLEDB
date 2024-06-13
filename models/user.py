from pydantic import BaseModel, validator, EmailStr
from typing import Optional
from datetime import date

class UserSignUp(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str
    address: str
    country: str
    state: str
    city: str
    zip_code: str
    date_of_birth: date
    gender: str
    profile_picture: str | None = None
    account_type: str
    language: str | None = "en"

    @validator('gender')
    def validate_gender(cls, value):
        allowed_values = ['male', 'female', 'other']
        if value not in allowed_values:
            raise ValueError(f'Gender must be one of {allowed_values}')
        return value

    @validator('account_type')
    def validate_account_type(cls, value):
        allowed_values = ['admin', 'regular', 'guest']
        if value not in allowed_values:
            raise ValueError(f'Account type must be one of {allowed_values}')
        return value


class UserLogin(BaseModel):
    username: str
    password: str
    grant_type: str