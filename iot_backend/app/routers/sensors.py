from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter(prefix="/sensors", tags=["sensors"])  # Deklarasi router

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/data")
def receive_sensor_data(sensor_data: schemas.SensorDataCreate, db: Session = Depends(get_db)):
    """
    Menerima data sensor dari perangkat IoT berdasarkan UUID device.
    """
    # Validasi apakah device dengan UUID ini sudah terdaftar
    device = crud.get_device_by_uuid(db, sensor_data.device_uuid)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    # Simpan data sensor ke database
    return crud.store_sensor_data(db, sensor_data)
    

@router.get("/realtime/{device_uuid}", response_model=schemas.SensorDataResponse)
def get_latest_sensor_data(device_uuid: str, db: Session = Depends(get_db)):
    """
    Mengambil data sensor terbaru dari device berdasarkan UUID.
    """
    data = crud.get_latest_sensor_data(db, device_uuid)
    if not data:
        raise HTTPException(status_code=404, detail="No sensor data found")
    return data


@router.get("/history/{device_uuid}")
def get_sensor_history(device_uuid: str, start_time: str, end_time: str, db: Session = Depends(get_db)):
    """
    Mengambil riwayat data sensor dalam rentang waktu tertentu.
    """
    history = crud.get_sensor_history(db, device_uuid, start_time, end_time)
    if not history:
        raise HTTPException(status_code=404, detail="No sensor data found for given time range")
    return history
