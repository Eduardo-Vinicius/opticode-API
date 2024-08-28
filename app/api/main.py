from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title = "OptiDrive Swagger",
    description = "Api referente ao projeto do OptiDrive.",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
