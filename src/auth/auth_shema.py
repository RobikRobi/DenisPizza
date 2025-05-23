import datetime
from pydantic import BaseModel, EmailStr, field_validator

class LoginUser(BaseModel):
    
    email: EmailStr
    password: str   
    
class RegisterUser(BaseModel):
        
    email: EmailStr
    
    name: str
    surname: str
    
    dob:datetime.date

    password: str | bytes 
    
    @field_validator("password")
    def check_password(cls, v):
        if len(v) < 8:
            raise ValueError("password must be at least 8 characters")
        return v

class ShowUser(BaseModel):
    
    id: int
    name: str
    surname: str
    email: EmailStr
    
    
    dob: datetime.date

class ShowUserWithToken(BaseModel):
    

    email: EmailStr
    name: str
    surname: str
    
    
    dob: datetime.date

    token: str

class UpdateUser(BaseModel):

    name: str | None
    surname: str | None
    email: EmailStr | None  
    password: str | bytes | None
    
    @field_validator("password")
    def check_password(cls, v):
        if not v:
            return None
        if  len(v) < 8:
            raise ValueError("password must be at least 8 characters")
        return v