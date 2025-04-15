from fastapi import FastAPI
from src.db import engine, Base
from binascii import Error

from src.auth.auth_router import app as auth_app


app = FastAPI()

app.include_router(auth_app)

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