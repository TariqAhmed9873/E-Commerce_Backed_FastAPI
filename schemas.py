from pydantic import BaseModel
from datetime import datetime


# schemas for making the user
class CreateUser(BaseModel):
    user_name : str
    user_email : str
    password : str
    user_role : str
    created_at : datetime

class ResponceUser(BaseModel):
    user_id : int
    user_name : str
    user_email : str
    user_role : str
    created_at : datetime


# schemas for making the user product
class CreateProducts(BaseModel):
    product_name : str
    description : str
    price : int
    stock : int
    category : int
    created_at : datetime

class ResponceProducts(BaseModel):
    product_id : int
    product_name : str
    description : str
    price : int
    stock : int
    category : int
    created_at : datetime