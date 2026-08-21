from fastapi import FastAPI


app = FastAPI()

@app.get("/home")
async def home():
    return{
        "Message":"This is for E-Commerce Backend System"
    }

@app.get("/add")
async def add():
    return {
        "message":"The Adding API"
    }