from imp import reload
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"hello":"Fast API"}

def start_app():
    uvicorn.run("fastapi_d.main:app", host="0.0.0.0", port=8000, reload=True)
