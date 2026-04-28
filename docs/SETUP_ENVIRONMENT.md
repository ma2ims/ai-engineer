# Setup Environment

Dokumen ini berisi panduan menyiapkan environment lokal untuk belajar AI Engineer dari repo ini.

## 1. Tools yang Dibutuhkan

Minimal install:

- Git
- Python 3.11+
- Docker Desktop / Docker Engine
- VS Code
- Terminal / shell

Opsional:

- Postman / Insomnia
- DB Browser for SQLite
- GitHub CLI

## 2. Cek Git

```bash
git --version
```

Setup identitas Git:

```bash
git config --global user.name "Nama Kamu"
git config --global user.email "email@example.com"
```

Cek config:

```bash
git config --list
```

## 3. Clone Repository

```bash
git clone https://github.com/ma2ims/ai-engineer.git
cd ai-engineer
```

Cek status repo:

```bash
git status
```

## 4. Cek Python

```bash
python --version
```

atau:

```bash
python3 --version
```

Target versi:

```text
Python 3.11 atau lebih baru
```

## 5. Membuat Virtual Environment

Masuk ke mini project:

```bash
cd modules/level-01-foundation/mini-project-daily-report-api
```

Buat virtual environment:

```bash
python -m venv .venv
```

Aktifkan di macOS/Linux:

```bash
source .venv/bin/activate
```

Aktifkan di Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependency:

```bash
pip install -r requirements.txt
```

## 6. Cek Docker

```bash
docker --version
```

Cek Docker Compose:

```bash
docker compose version
```

Test Docker:

```bash
docker run hello-world
```

## 7. Menjalankan Mini Project Tanpa Docker

```bash
cd modules/level-01-foundation/mini-project-daily-report-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Buka:

```text
http://localhost:8000/docs
```

## 8. Menjalankan Mini Project Dengan Docker

```bash
cd modules/level-01-foundation/mini-project-daily-report-api
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

## 9. Struktur Folder yang Perlu Dipahami

```text
ai-engineer/
├── docs/
│   └── dokumentasi belajar
├── modules/
│   └── materi per level
└── projects/
    └── project latihan tambahan jika nanti dibuat
```

## 10. Checklist Setup

```text
[ ] Git sudah terinstall
[ ] Python 3.11+ sudah terinstall
[ ] Docker sudah berjalan
[ ] Repo berhasil di-clone
[ ] Virtual environment berhasil dibuat
[ ] Dependency berhasil di-install
[ ] FastAPI docs bisa dibuka
[ ] Docker Compose berhasil menjalankan project
```

## 11. Masalah Umum

### Port 8000 sudah dipakai

Cek process:

```bash
lsof -i :8000
```

Stop process atau jalankan di port lain:

```bash
uvicorn app.main:app --reload --port 8001
```

### Docker tidak jalan

Pastikan Docker Desktop / Docker Engine aktif, lalu cek:

```bash
docker ps
```

### Module not found

Pastikan berada di folder project yang benar dan dependency sudah diinstall:

```bash
pip install -r requirements.txt
```

## Next Step

Setelah setup selesai, lanjut ke:

```text
docs/LEARNING_CHECKLIST.md
modules/level-01-foundation/README.md
```
