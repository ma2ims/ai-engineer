# Level 1 — Foundation

Level ini adalah pondasi awal sebelum masuk ke LLM Application, RAG, AI Agent, dan Production AI System.

Target utama Level 1: learner bisa membuat API sederhana yang menerima data JSON, menyimpan data ke database, dijalankan dengan Docker, dan dikelola menggunakan Git.

---

## Skill yang Dipelajari

```text
1. Python basic
2. JSON basic
3. API basic
4. Git basic
5. Database basic
6. Linux command
7. Docker basic
```

---

## Output Akhir Level 1

Project:

```text
projects/daily-report-api
```

Fitur project:

```text
[ ] Health check endpoint
[ ] Create daily report
[ ] Get all daily reports
[ ] Get report by ID
[ ] Save data to SQLite
[ ] Return JSON response
[ ] Run with Docker Compose
[ ] Versioned with Git
```

---

## Urutan Belajar

Ikuti urutan ini agar tidak lompat terlalu jauh:

```text
01-python-basic.md
02-json-basic.md
03-api-basic.md
04-git-basic.md
05-database-basic.md
06-linux-command.md
07-docker-basic.md
```

Jika file detail belum lengkap, gunakan checklist di dokumen ini sebagai panduan praktik awal.

---

## Minggu 1 — Python dan JSON

Tujuan:

```text
- memahami variable
- memahami list dan dictionary
- membuat function
- membaca/menulis file
- membaca/menulis JSON
```

Latihan:

```text
1. Buat script Python untuk menghitung total pakan.
2. Buat dictionary data laporan kandang.
3. Simpan data laporan ke file JSON.
4. Baca kembali file JSON dan tampilkan summary.
```

Contoh output:

```text
Farm: Tobasa Farm
Population: 21000
Mortality: 35
Feed Used: 1250 kg
Average Weight: 1.2 kg
```

Checklist:

```text
[ ] Bisa membuat variable
[ ] Bisa menggunakan list
[ ] Bisa menggunakan dictionary
[ ] Bisa membuat if/else
[ ] Bisa membuat loop
[ ] Bisa membuat function
[ ] Bisa membaca file JSON
[ ] Bisa menulis file JSON
```

---

## Minggu 2 — API dan Git

Tujuan:

```text
- memahami HTTP method
- membuat API dengan FastAPI
- menerima JSON request body
- mengembalikan JSON response
- memakai Git untuk version control
```

Latihan API:

```text
1. Buat endpoint GET /health
2. Buat endpoint POST /reports
3. Buat endpoint GET /reports
4. Test endpoint via /docs
```

Latihan Git:

```bash
git checkout -b learning/level-01-api
git add .
git commit -m "learning: add basic report API"
git push origin learning/level-01-api
```

Checklist:

```text
[ ] Bisa menjalankan FastAPI
[ ] Bisa membuka Swagger docs
[ ] Bisa membuat GET endpoint
[ ] Bisa membuat POST endpoint
[ ] Bisa menerima JSON body
[ ] Bisa commit dengan Git
[ ] Bisa push branch ke GitHub
```

---

## Minggu 3 — Database dan Linux

Tujuan:

```text
- memahami table, row, column
- memahami SQL dasar
- memakai SQLite dari Python
- menggunakan terminal Linux untuk navigasi project
```

Latihan Database:

```text
1. Buat table daily_reports
2. Insert report baru
3. Select semua report
4. Select report by ID
```

Latihan Linux:

```bash
pwd
ls -la
cd projects/daily-report-api
cat README.md
grep -r "FastAPI" .
```

Checklist:

```text
[ ] Bisa membuat table SQLite
[ ] Bisa insert data
[ ] Bisa select data
[ ] Bisa update data sederhana
[ ] Bisa delete data sederhana
[ ] Bisa navigasi folder via terminal
[ ] Bisa mencari teks dengan grep
```

---

## Minggu 4 — Docker dan Mini Project

Tujuan:

```text
- memahami Dockerfile
- memahami Docker Compose
- menjalankan API dalam container
- memastikan project bisa dijalankan orang lain
```

Command:

```bash
cd projects/daily-report-api
docker compose up --build
```

Buka:

```text
http://localhost:8000/docs
```

Checklist:

```text
[ ] Bisa membaca Dockerfile
[ ] Bisa menjalankan docker compose up
[ ] Bisa melihat log container
[ ] Bisa stop container
[ ] Bisa rebuild container
[ ] API bisa diakses dari localhost
```

---

## Final Checklist Level 1

Level ini dianggap selesai jika:

```text
[ ] Project daily-report-api berjalan lokal
[ ] Project daily-report-api berjalan dengan Docker
[ ] Endpoint /health berjalan
[ ] Endpoint POST /reports berjalan
[ ] Endpoint GET /reports berjalan
[ ] Endpoint GET /reports/{id} berjalan
[ ] Data tersimpan ke SQLite
[ ] README project jelas
[ ] Perubahan sudah di-commit ke Git
[ ] Learner bisa menjelaskan alur Client → API → Database → Response
```

---

## Alur Data yang Harus Dipahami

```text
Client / Swagger UI
        ↓
FastAPI endpoint
        ↓
Pydantic model validation
        ↓
SQLite database
        ↓
JSON response
```

---

## Pertanyaan Review Diri

Jawab sebelum naik ke Level 2:

```text
1. Apa bedanya GET dan POST?
2. Apa itu JSON request body?
3. Apa fungsi Pydantic model?
4. Kenapa data perlu disimpan ke database?
5. Apa fungsi Dockerfile?
6. Apa fungsi docker-compose.yml?
7. Kenapa commit kecil lebih baik?
8. Bagaimana cara orang lain menjalankan project ini setelah clone repo?
```

---

## Setelah Level 1

Lanjut ke:

```text
Level 2 — LLM Application
```

Di Level 2, API yang sudah dipahami akan dikembangkan menjadi aplikasi yang bisa terhubung ke LLM API seperti OpenAI, Anthropic, Gemini, atau local model melalui LiteLLM/Ollama.
