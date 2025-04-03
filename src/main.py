from fastapi import FastAPI
import uvicorn
from src.db import engine, Base
from binascii import Error

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/init")
async def create_db():
    async with engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.drop_all)
        except Error as e:
            print(e)     
        await  conn.run_sync(Base.metadata.create_all)
    return({"msg":"db creat! =)"})