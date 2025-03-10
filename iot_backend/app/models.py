from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))

    devices = relationship("Device", back_populates="owner")

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    registered = Column(Boolean, default=False)

    owner = relationship("User", back_populates="devices")
    sensor_data = relationship("SensorData", back_populates="device")

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    temperature = Column(Float, nullable=True)
    salinity = Column(Float, nullable=True)
    ph = Column(Float, nullable=True)
    do = Column(Float, nullable=True)
    ammonia = Column(Float, nullable=True)

    device = relationship("Device", back_populates="sensor_data")
