from fastapi import FastAPI
from routers import user_login, orders, payment, product_catlog, review, shoping_cart
from database import engine
from models import Base

# Create all database tables
Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/home")
async def home():
    return{
        "Message":"This is for E-Commerce Backend System"
    }

# Authentication routes
app.include_router(user_login.router)

# Orders routes
app.include_router(orders.router)

# Payment routes
app.include_router(payment.router)

# product catlog reoutes
app.include_router(product_catlog.router)

# review routes
app.include_router(review.router)

# shoping cart routes
app.include_router(shoping_cart.router)