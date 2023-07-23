from pydantic import BaseModel, EmailStr



class CreateSubscriberSchema(BaseModel):

    email: EmailStr
    