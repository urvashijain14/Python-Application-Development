
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(gt=0, le=100)
    course: str = Field(min_length=2, max_length=50)
