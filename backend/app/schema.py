from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    id: int = Field(...)
    name: str = Field(..., min_length=1, max_length=128)
    email: EmailStr
