from pydantic import BaseModel, EmailStr


class ContactUsSchema(BaseModel):
    name: str
    email: EmailStr
    message: str