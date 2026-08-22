from fastapi import FastAPI


app = FastAPI()

@app.get("/home")
async def home():
    return{
        "Message":"This is for E-Commerce Backend System"
    }

