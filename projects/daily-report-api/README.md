# Daily Report API

Project ini adalah mini project Level 1 untuk belajar pondasi AI Engineer.

Tujuannya bukan membuat aplikasi besar, tetapi memahami alur dasar backend:

```text
Client / Swagger UI → FastAPI → Pydantic Validation → SQLite → JSON Response
```

---

## Skill yang Dilatih

```text
[ ] Python project structure
[ ] FastAPI basic
[ ] JSON request dan response
[ ] Pydantic validation
[ ] SQLite database
[ ] Dockerfile
[ ] Docker Compose
[ ] Git commit workflow
```

---

## Struktur Project

```text
daily-report-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── models.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Fitur API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/` | root message |
| GET | `/health` | cek API aktif |
| POST | `/reports` | membuat laporan harian |
| GET | `/reports` | mengambil semua laporan |
| GET | `/reports/{report_id}` | mengambil laporan berdasarkan ID |

---

## Menjalankan dengan Docker

Dari root repo:

```bash
cd projects/daily-report-api
docker compose up --build
```

Buka API docs:

```text
http://localhost:8000/docs
```

Health check:

```bash
curl http://localhost:8000/health
```

Stop:

```bash
docker compose down
```

---

## Menjalankan Tanpa Docker

```bash
cd projects/daily-report-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Buka:

```text
http://127.0.0.1:8000/docs
```

---

## Contoh Request

Endpoint:

```text
POST /reports
```

Body:

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

Contoh curl:

```bash
curl -X POST http://localhost:8000/reports \
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

Ambil semua report:

```bash
curl http://localhost:8000/reports
```

Ambil report by ID:

```bash
curl http://localhost:8000/reports/1
```

---

## Alur Kode

```text
app/main.py
  - mendefinisikan endpoint API
  - menerima request
  - mengembalikan response

app/models.py
  - mendefinisikan schema request dengan Pydantic

app/database.py
  - membuat koneksi SQLite
  - membuat table
  - menjalankan query insert/select
```

---

## Database

Project ini memakai SQLite untuk belajar.

File database default:

```text
app.db
```

File ini tidak perlu di-commit ke Git karena masuk `.gitignore`.

---

## Practice Task

Setelah API berhasil jalan, lakukan latihan ini:

```text
1. Tambahkan field note pada DailyReport
2. Update table database
3. Update POST /reports
4. Update GET /reports
5. Test via Swagger UI
6. Commit perubahan ke Git
```

Contoh commit:

```bash
git add .
git commit -m "learning: add note field to daily report api"
```

---

## Completion Checklist

Project dianggap selesai jika:

```text
[ ] Docker Compose bisa jalan
[ ] /health return status ok
[ ] POST /reports berhasil membuat data
[ ] GET /reports menampilkan list data
[ ] GET /reports/{id} bisa mengambil data tertentu
[ ] ID tidak ditemukan return 404
[ ] Data tetap ada setelah API restart
[ ] Learner bisa menjelaskan fungsi setiap file
```

---

## Next Step

Setelah project ini selesai, lanjut ke Level 2:

```text
LLM Application
```

Project ini nanti bisa dikembangkan menjadi API yang membuat ringkasan laporan menggunakan LLM.
