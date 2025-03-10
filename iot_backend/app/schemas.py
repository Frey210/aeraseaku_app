from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User Schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

# Device Schema
class DeviceRegister(BaseModel):
    uuid: str
    device_name: str  # Tambahkan nama perangkat

class DeviceResponse(BaseModel):
    id: int
    uuid: str
    registered: bool
    user_id: Optional[int] = None

    class Config:
        orm_mode = True

# Sensor Data Schema
class SensorDataCreate(BaseModel):
    temperature: Optional[float]
    salinity: Optional[float]
    ph: Optional[float]
    do: Optional[float]
    ammonia: Optional[float]

class SensorDataResponse(SensorDataCreate):
    id: int
    device_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
