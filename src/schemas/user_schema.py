from pydantic import BaseModel,EmailStr

class UserSignUpSchema(BaseModel):
    username: str
    password: str
    email_id: EmailStr

class UserAuthenticationSchema(BaseModel):
    username: str
    password: str

