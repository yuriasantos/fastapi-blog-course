from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)

class ShowUser(BaseModel):
    email: EmailStr
    is_active: bool

    class ConfigDict():
        from_attributes = True
