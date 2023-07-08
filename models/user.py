from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    fullname: str
    username: str
    email: str
    password: str
    app_name: str
