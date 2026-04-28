# Local Setup Guide

Panduan ini digunakan untuk menyiapkan environment lokal sebelum mulai belajar dari repo ini.

Target setup:

```text
Git
Python
Docker
Text editor / VS Code
Terminal
```

---

## 1. Clone Repository

```bash
git clone https://github.com/ma2ims/ai-engineer.git
cd ai-engineer
```

Cek isi repo:

```bash
ls -la
```

---

## 2. Cek Git

```bash
git --version
```

Jika belum ada Git, install terlebih dahulu.

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install git -y
```

Set nama dan email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Cek konfigurasi:

```bash
git config --list
```

---

## 3. Cek Python

```bash
python3 --version
```

Jika belum ada Python:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

Cek pip:

```bash
pip3 --version
```

---

## 4. Buat Virtual Environment

Masuk ke project:

```bash
cd projects/daily-report-api
```

Buat virtual environment:

```bash
python3 -m venv .venv
```

Aktifkan:

```bash
source .venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan API tanpa Docker:

```bash
uvicorn app.main:app --reload
```

Buka:

```text
http://localhost:8000/docs
```

---

## 5. Cek Docker

```bash
docker --version
```

Cek Docker Compose:

```bash
docker compose version
```

Jika Docker belum terpasang, install Docker sesuai OS yang digunakan.

Cek Docker berjalan:

```bash
docker run hello-world
```

---

## 6. Jalankan Project dengan Docker

Dari folder:

```bash
projects/daily-report-api
```

Jalankan:

```bash
docker compose up --build
```

Buka:

```text
http://localhost:8000/docs
```

Stop container:

```bash
docker compose down
```

---

## 7. Cek API

Health check:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

---

## 8. Create Report via cURL

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

---

## 9. Basic Git Workflow untuk Belajar

Buat branch belajar:

```bash
git checkout -b learning/level-01
```

Cek perubahan:

```bash
git status
```

Commit perubahan:

```bash
git add .
git commit -m "Practice level 01 foundation"
```

Push branch:

```bash
git push origin learning/level-01
```

---

## 10. Troubleshooting

### Port 8000 sudah dipakai

Cek process:

```bash
ss -tulpn | grep 8000
```

Atau ubah port Docker Compose:

```yaml
ports:
  - "8001:8000"
```

Buka:

```text
http://localhost:8001/docs
```

### Docker permission denied

Tambahkan user ke group docker:

```bash
sudo usermod -aG docker $USER
```

Logout lalu login ulang.

### Module tidak ditemukan

Pastikan dependency sudah diinstall:

```bash
pip install -r requirements.txt
```

Jika pakai Docker, rebuild:

```bash
docker compose up --build
```

---

## Setup Selesai Jika

```text
[ ] Repo berhasil di-clone
[ ] Python bisa dijalankan
[ ] Git bisa digunakan
[ ] Docker bisa menjalankan hello-world
[ ] Daily Report API bisa berjalan
[ ] Swagger docs bisa dibuka
[ ] Endpoint /health mengembalikan status ok
```
