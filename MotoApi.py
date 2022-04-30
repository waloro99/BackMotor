import motor as m
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    res = m.hola()
    return {"Hello world! " + res}