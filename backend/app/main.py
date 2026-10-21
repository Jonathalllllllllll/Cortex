from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="Cortex API")

@app.get("/health")
def health():
    return {"status": "ok"}

