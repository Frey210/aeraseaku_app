from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database
from app.dependencies import get_current_user

router = APIRouter(prefix="/devices", tags=["devices"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_device(device_data: schemas.DeviceRegister, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(get_current_user)):
    """
    Mendaftarkan device baru dengan UUID dan nama device.
    """
    registered_device = crud.register_device(db, device_data, current_user.id)
    
    if not registered_device:
        raise HTTPException(status_code=400, detail="Device already registered or invalid UUID")

    return {"message": "Device registered successfully", "device": registered_device}

@router.get("/my-devices", response_model=list[schemas.DeviceResponse])
def get_user_devices(db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(get_current_user)):
    """
    Mengambil daftar semua device yang dimiliki oleh user.
    """
    devices = crud.get_devices_by_user(db, current_user.id)
    return devices

