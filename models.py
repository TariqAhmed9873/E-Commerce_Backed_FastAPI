from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base


#making models for user
class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_email = Column(String)
    password = Column(String)
    user_role = Column(String)
    created_at = Column(DateTime)


# making the models for product
class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    description = Column(Text)
    price = Column(Integer)
    stock = Column(Integer)
    category = Column(Integer)
    created_at = Column(DateTime)


