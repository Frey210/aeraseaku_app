from sqlalchemy.orm import Session
from app import models, schemas, security
from datetime import datetime

# User CRUD
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.hash_password(user.password)
    db_user = models.User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Device CRUD
def register_device(db: Session, device_data: schemas.DeviceRegister, user_id: int):
    device = db.query(models.Device).filter(models.Device.uuid == device_data.uuid).first()
    
    if device:
        if not device.registered:
            # Jika device sudah ada tetapi belum terdaftar, update data
            device.user_id = user_id
            device.device_name = device_data.device_name  # Simpan nama device
            device.registered = True
            db.commit()
            db.refresh(device)
            return device
        else:
            return None  # Jika sudah terdaftar, tidak boleh daftar ulang

    # Jika device belum ada, buat baru
    new_device = models.Device(
        uuid=device_data.uuid,
        device_name=device_data.device_name,  # Simpan nama device
        registered=True,
        user_id=user_id
    )
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device


def get_device_by_uuid(db: Session, uuid: str):
    return db.query(models.Device).filter(models.Device.uuid == uuid).first()

def get_devices_by_user(db: Session, user_id: int):
    return db.query(models.Device).filter(models.Device.user_id == user_id).all()

# Sensor Data CRUD
def save_sensor_data(db: Session, sensor_data: schemas.SensorDataCreate):
    device = get_device_by_uuid(db, sensor_data.device_uuid)
    if not device:
        return None  # Jika device tidak ditemukan, return None

    sensor_entry = models.SensorData(
        device_id=device.id,
        temperature=sensor_data.temperature,
        salinity=sensor_data.salinity,
        ph=sensor_data.ph,
        do=sensor_data.do,
        ammonia=sensor_data.ammonia
    )
    
    db.add(sensor_entry)
    db.commit()
    db.refresh(sensor_entry)
    return sensor_entry

def get_latest_sensor_data(db: Session, device_uuid: str):
    device = get_device_by_uuid(db, device_uuid)
    if not device:
        return None
    return db.query(models.SensorData).filter(models.SensorData.device_id == device.id).order_by(models.SensorData.timestamp.desc()).first()

def get_sensor_history(db: Session, device_uuid: str, start_time: str, end_time: str):
    device = get_device_by_uuid(db, device_uuid)
    if not device:
        return None

    try:
        start_dt = datetime.fromisoformat(start_time)
        end_dt = datetime.fromisoformat(end_time)
    except ValueError:
        return None  # Return None jika format waktu salah

    return db.query(models.SensorData).filter(
        models.SensorData.device_id == device.id,
        models.SensorData.timestamp >= start_dt,
        models.SensorData.timestamp <= end_dt
    ).all()
