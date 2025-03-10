🌐 IoT Backend API (FastAPI + MySQL)
Backend API untuk monitoring data sensor IoT berbasis FastAPI & MySQL.
API ini memungkinkan perangkat IoT mengirimkan data sensor dan memungkinkan pengguna melihat riwayat serta data realtime perangkat yang terdaftar.

📌 Fitur Utama
✅ Autentikasi Pengguna (Register, Login, JWT)
✅ Manajemen Perangkat (Device UUID + Device Name)
✅ Penerimaan & Penyimpanan Data Sensor
✅ Monitoring Data Sensor (Realtime & History)
✅ Integrasi MySQL Database
✅ Deploy ke cPanel / VPS

📁 Struktur Proyek
ba
📂 iot_backend/
│── 📂 app/
│   ├── 📂 models/        # Model database (SQLAlchemy ORM)
│   ├── 📂 schemas/       # Schema validasi (Pydantic)
│   ├── 📂 crud/          # Operasi database (CRUD)
│   ├── 📂 routers/       # API routes (FastAPI endpoints)
│   │   ├── users.py      # Manajemen akun
│   │   ├── devices.py    # Manajemen perangkat IoT
│   │   ├── sensors.py    # Data sensor (realtime & history)
│   ├── 📂 database.py    # Koneksi ke database
│   ├── 📂 security.py    # Hashing & autentikasi
│   ├── main.py           # Entry point aplikasi
│   ├── asgi.py           # File ASGI untuk deploy di cPanel
│── 📜 requirements.txt    # Dependensi proyek
│── 📜 .env                # Konfigurasi lingkungan
│── 📜 README.md           # Dokumentasi proyek (file ini)
🛠️ Instalasi & Konfigurasi
1️⃣ Clone Repository

git clone https://github.com/username/iot_backend.git
cd iot_backend

2️⃣ Buat & Aktifkan Virtual Environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Konfigurasi Database
Buat file .env dan tambahkan:

env

DATABASE_URL=mysql+pymysql://username:password@localhost/iot_db
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

5️⃣ Jalankan Migrations

alembic upgrade head

6️⃣ Jalankan Server

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Akses API di: http://127.0.0.1:8000/docs (Swagger UI)

🚀 API Endpoints

📌 Autentikasi

Method	Endpoint	Deskripsi
POST	/users/register	Registrasi pengguna
POST	/users/login	Login & dapatkan token

📌 Manajemen Perangkat

Method	Endpoint	Deskripsi
POST	/devices/register	Daftarkan perangkat baru
GET	/devices/list	Lihat semua perangkat user

🔹 Contoh JSON Request untuk Register Perangkat:

json

{
  "uuid": "123e4567-e89b-12d3-a456-426614174000",
  "device_name": "Kolam Tambak 1"
}

📌 Data Sensor

Method	Endpoint	Deskripsi
POST	/sensors/data	Kirim data sensor dari IoT
GET	/sensors/realtime/{uuid}	Ambil data sensor terbaru
GET	/sensors/history/{uuid}	Ambil riwayat data sensor

🔹 Contoh JSON Request untuk Kirim Data Sensor:

json

{
  "device_uuid": "123e4567-e89b-12d3-a456-426614174000",
  "temperature": 28.5,
  "salinity": 35.0,
  "ph": 7.2,
  "do": 6.5,
  "ammonia": 0.02
}
