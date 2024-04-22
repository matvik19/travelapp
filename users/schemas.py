from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MinLen, MaxLen


class CreateUser(BaseModel):
    # username: str = Field(..., min_length=3, max_length=30)
    username: Annotated[str, MinLen(3), MaxLen(30)]
    email: EmailStr
    password: int
