# 03 — API Basic

API adalah cara aplikasi saling berkomunikasi.

Target modul ini: learner paham konsep API, HTTP method, status code, request JSON, response JSON, dan bisa membuat API sederhana menggunakan FastAPI.

---

## Kenapa API Penting untuk AI Engineer?

AI system biasanya tidak berdiri sendiri. AI perlu terhubung ke aplikasi, database, workflow, dan tool lain.

Contoh:

```text
Mobile App → API → Database
Dashboard → API → AI Service
AI Agent → API → Tool / System
n8n → API → LLM Layer
```

---

## 1. Konsep Dasar API

API menerima request dan mengembalikan response.

```text
Client mengirim request
        ↓
API memproses data
        ↓
API mengirim response
```

Contoh endpoint:

```text
GET  /health
POST /reports
GET  /reports
GET  /reports/1
```

---

## 2. HTTP Method Dasar

| Method | Fungsi |
|---|---|
| GET | mengambil data |
| POST | membuat data baru |
| PUT | mengganti data secara penuh |
| PATCH | mengubah sebagian data |
| DELETE | menghapus data |

Untuk Level 1, fokus dulu ke:

```text
GET dan POST
```

---

## 3. Status Code Penting

| Status | Arti |
|---:|---|
| 200 | OK / request berhasil |
| 201 | data berhasil dibuat |
| 400 | request salah |
| 401 | belum login |
| 403 | tidak punya akses |
| 404 | data tidak ditemukan |
| 500 | error server |

---

## 4. Install FastAPI

Masuk ke folder project latihan:

```bash
mkdir api-practice
cd api-practice
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```

Buat file:

```text
main.py
```

---

## 5. API Pertama

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "API is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }
```

Jalankan:

```bash
uvicorn main:app --reload
```

Buka:

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

---

## 6. Path Parameter

Path parameter dipakai untuk mengambil data spesifik.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/reports/{report_id}")
def get_report(report_id: int):
    return {
        "id": report_id,
        "farm_name": "Tobasa Farm"
    }
```

Contoh akses:

```text
GET /reports/1
```

---

## 7. Query Parameter

Query parameter biasanya dipakai untuk filter/search.

```python
@app.get("/reports")
def get_reports(farm_name: str | None = None):
    return {
        "filter": farm_name,
        "data": []
    }
```

Contoh akses:

```text
GET /reports?farm_name=Tobasa%20Farm
```

---

## 8. Request Body dengan Pydantic

FastAPI memakai Pydantic untuk validasi data.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DailyReport(BaseModel):
    date: str
    farm_name: str
    population: int
    mortality: int
    feed_used_kg: float
    average_weight: float

@app.post("/reports")
def create_report(report: DailyReport):
    return {
        "message": "Report created",
        "data": report
    }
```

Contoh request body:

```json
{
  "date": "2026-04-28",
  "farm_name": "Tobasa Farm",
  "population": 21000,
  "mortality": 35,
  "feed_used_kg": 1250,
  "average_weight": 1.2
}
```

---

## 9. Simpan Data Sementara di Memory

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
reports = []

class DailyReport(BaseModel):
    date: str
    farm_name: str
    population: int
    mortality: int
    feed_used_kg: float
    average_weight: float

@app.post("/reports")
def create_report(report: DailyReport):
    report_data = report.model_dump()
    report_data["id"] = len(reports) + 1
    reports.append(report_data)

    return {
        "message": "Report created",
        "data": report_data
    }

@app.get("/reports")
def get_reports():
    return {
        "data": reports
    }

@app.get("/reports/{report_id}")
def get_report(report_id: int):
    for report in reports:
        if report["id"] == report_id:
            return {"data": report}

    raise HTTPException(status_code=404, detail="Report not found")
```

Catatan:

```text
Data di memory akan hilang saat server restart.
Di modul database, data akan disimpan permanen ke SQLite.
```

---

## 10. Test API dengan Swagger UI

FastAPI otomatis membuat dokumentasi API.

Buka:

```text
http://127.0.0.1:8000/docs
```

Langkah test:

```text
1. Buka /docs
2. Pilih POST /reports
3. Klik Try it out
4. Isi JSON body
5. Klik Execute
6. Cek response
7. Test GET /reports
```

---

## 11. Test API dengan curl

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Create report:

```bash
curl -X POST http://127.0.0.1:8000/reports \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2026-04-28",
    "farm_name": "Tobasa Farm",
    "population": 21000,
    "mortality": 35,
    "feed_used_kg": 1250,
    "average_weight": 1.2
  }'
```

Get reports:

```bash
curl http://127.0.0.1:8000/reports
```

---

## Mini Exercise

Buat API dengan endpoint:

```text
GET  /health
POST /reports
GET  /reports
GET  /reports/{report_id}
```

Field report:

```text
date
farm_name
population
mortality
feed_used_kg
average_weight
```

Rules:

```text
- response harus JSON
- jika report_id tidak ditemukan, return 404
- test via /docs dan curl
```

---

## Common Error

### ModuleNotFoundError: No module named fastapi

Artinya FastAPI belum terinstall di environment aktif.

```bash
pip install fastapi uvicorn
```

### Address already in use

Port 8000 sedang dipakai.

```bash
uvicorn main:app --reload --port 8001
```

### 422 Unprocessable Entity

Format request body tidak sesuai Pydantic model. Cek field, tipe data, dan nama key.

---

## Checklist

```text
[ ] Paham konsep request dan response
[ ] Paham GET dan POST
[ ] Paham status code dasar
[ ] Bisa menjalankan FastAPI
[ ] Bisa membuka /docs
[ ] Bisa membuat endpoint /health
[ ] Bisa menerima JSON body
[ ] Bisa memakai Pydantic model
[ ] Bisa return JSON response
[ ] Bisa return 404 jika data tidak ditemukan
```

---

## Next Module

Lanjut ke:

```text
04-git-basic.md
```
