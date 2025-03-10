from fastapi import FastAPI
from app.database import engine, Base
from .routers import users, devices, sensors


Base.metadata.create_all(bind=engine)

app = FastAPI(title="IoT Backend API")

app.include_router(users.router)
app.include_router(devices.router)
app.include_router(sensors.router)

@app.get("/")
def root():
    return {"message": "Welcome to IoT Backend API"}
