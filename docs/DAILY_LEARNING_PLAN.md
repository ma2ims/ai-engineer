# Daily Learning Plan — Level 1 Foundation

Dokumen ini berisi rencana belajar harian untuk menyelesaikan Level 1 Foundation.

Durasi ideal:

```text
14–28 hari
```

Gunakan tempo yang realistis. Yang penting konsisten dan setiap topik menghasilkan praktik kecil.

---

## Minggu 1 — Python dan JSON

### Day 1 — Setup dan Orientasi Repo

Target:

```text
[ ] Clone repo
[ ] Baca README.md
[ ] Baca docs/START_HERE.md
[ ] Baca docs/LOCAL_SETUP.md
[ ] Jalankan project dengan Docker
```

Commit contoh:

```bash
git commit -m "Setup learning environment"
```

---

### Day 2 — Python Variable dan Data Type

Target:

```text
[ ] Membuat variable string, integer, float, boolean
[ ] Menjalankan file Python
[ ] Mencetak output dengan print
```

Latihan:

```text
Buat script yang menyimpan data nama farm, populasi ayam, umur ayam, dan status aktif.
```

---

### Day 3 — Python List dan Dictionary

Target:

```text
[ ] Membuat list
[ ] Loop list
[ ] Membuat dictionary
[ ] Mengakses value dari dictionary
```

Latihan:

```text
Buat list berisi 3 daily report, masing-masing report berbentuk dictionary.
```

---

### Day 4 — Condition dan Function

Target:

```text
[ ] Membuat if/else
[ ] Membuat function
[ ] Return value dari function
```

Latihan:

```text
Buat function calculate_depletion(dead, population).
Jika deplesi lebih dari 5%, tampilkan warning.
```

---

### Day 5 — File Handling

Target:

```text
[ ] Menulis file txt
[ ] Membaca file txt
[ ] Membuat catatan output sederhana
```

Latihan:

```text
Buat daily_note.txt dan isi dengan ringkasan laporan operasional.
```

---

### Day 6 — JSON Basic

Target:

```text
[ ] Membuat file JSON
[ ] Membaca JSON dengan Python
[ ] Mengubah dictionary ke JSON
[ ] Menulis JSON ke file
```

Latihan:

```text
Buat daily_report.json lalu baca dengan Python.
```

---

### Day 7 — Review Minggu 1

Target:

```text
[ ] Review semua latihan
[ ] Rapikan catatan
[ ] Commit semua progress
[ ] Tulis hal yang belum paham
```

Commit contoh:

```bash
git add .
git commit -m "Complete week 1 Python and JSON practice"
```

---

## Minggu 2 — API dan Git

### Day 8 — FastAPI Basic

Target:

```text
[ ] Membuat endpoint /
[ ] Membuat endpoint /health
[ ] Menjalankan uvicorn
[ ] Membuka Swagger docs
```

---

### Day 9 — GET Endpoint

Target:

```text
[ ] Membuat endpoint GET /reports
[ ] Mengembalikan response JSON
[ ] Membaca response di browser atau curl
```

---

### Day 10 — POST Endpoint

Target:

```text
[ ] Membuat model Pydantic
[ ] Menerima JSON body
[ ] Mengembalikan response JSON
```

Latihan:

```text
POST /reports dengan data daily report.
```

---

### Day 11 — Git Basic

Target:

```text
[ ] git status
[ ] git add
[ ] git commit
[ ] git log
[ ] git branch
```

Latihan:

```text
Buat branch learning/api-practice dan commit perubahan API.
```

---

### Day 12 — GitHub Push

Target:

```text
[ ] Push branch ke GitHub
[ ] Cek branch di GitHub
[ ] Baca kembali commit history
```

---

### Day 13 — API Review

Target:

```text
[ ] Test endpoint /health
[ ] Test GET /reports
[ ] Test POST /reports
[ ] Perbaiki error jika ada
```

---

### Day 14 — Review Minggu 2

Commit contoh:

```bash
git add .
git commit -m "Complete week 2 API and Git practice"
```

---

## Minggu 3 — Database dan Linux

### Day 15 — Database Concept

Target:

```text
[ ] Paham table
[ ] Paham row dan column
[ ] Paham primary key
[ ] Paham SQL basic
```

---

### Day 16 — SQLite Create Table

Target:

```text
[ ] Membuat app.db
[ ] Membuat table daily_reports
[ ] Menjalankan create table dari Python
```

---

### Day 17 — SQLite Insert dan Select

Target:

```text
[ ] Insert data report
[ ] Select semua report
[ ] Print hasil query
```

---

### Day 18 — Integrasi API + Database

Target:

```text
[ ] POST /reports menyimpan data ke database
[ ] GET /reports membaca data dari database
[ ] GET /reports/{id} membaca data berdasarkan ID
```

---

### Day 19 — Linux Command Basic

Target:

```text
[ ] pwd, ls, cd
[ ] mkdir, touch
[ ] cat, head, tail
[ ] cp, mv, rm
```

---

### Day 20 — Linux Search dan Process

Target:

```text
[ ] grep
[ ] find
[ ] ps aux
[ ] ss -tulpn
[ ] environment variable
```

---

### Day 21 — Review Minggu 3

Commit contoh:

```bash
git add .
git commit -m "Complete week 3 database and Linux practice"
```

---

## Minggu 4 — Docker dan Final Project

### Day 22 — Docker Basic

Target:

```text
[ ] docker --version
[ ] docker run hello-world
[ ] docker ps
[ ] docker images
```

---

### Day 23 — Dockerfile

Target:

```text
[ ] Membuat Dockerfile
[ ] Build image
[ ] Run container
[ ] Expose port 8000
```

---

### Day 24 — Docker Compose

Target:

```text
[ ] Membuat docker-compose.yml
[ ] docker compose up
[ ] docker compose down
[ ] docker compose logs
```

---

### Day 25 — Project Testing

Target:

```text
[ ] Test API via browser
[ ] Test API via curl
[ ] Test create report
[ ] Test get reports
[ ] Test get report by ID
```

---

### Day 26 — README Project

Target:

```text
[ ] Tulis deskripsi project
[ ] Tulis cara install
[ ] Tulis cara run dengan Docker
[ ] Tulis contoh request
[ ] Tulis endpoint list
```

---

### Day 27 — Final Review

Target:

```text
[ ] Repo bersih
[ ] Docker berjalan
[ ] README jelas
[ ] Git history rapi
[ ] Semua checklist Level 1 selesai
```

---

### Day 28 — Finish Level 1

Commit final:

```bash
git add .
git commit -m "Complete level 1 foundation"
git tag v0.1.0
```

Push:

```bash
git push origin main
git push origin v0.1.0
```

---

## Catatan

Tidak wajib selesai tepat 28 hari. Lebih baik lambat tapi paham daripada cepat tapi hanya copy-paste.

Yang paling penting:

```text
Project berjalan, kode dipahami, dan progres tercatat di Git.
```
