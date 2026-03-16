from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class ProcessInput(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "message": "hello from VPS",
        "time": datetime.utcnow().isoformat()
    }


@app.get("/hello")
def hello(name: str = "world"):
    return {
        "message": f"hello {name}"
    }


@app.post("/process")
def process(data: ProcessInput):
    text = data.text

    return {
        "original": text,
        "upper": text.upper(),
        "length": len(text),
        "time": datetime.utcnow().isoformat()
    }
