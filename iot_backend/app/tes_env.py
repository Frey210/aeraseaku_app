from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:password@localhost/iot_aquaculture"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("✅ Koneksi sukses!")
except Exception as e:
    print("❌ Koneksi gagal:", e)
