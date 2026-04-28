# Start Here — AI Engineer Learning

Dokumen ini adalah pintu masuk utama untuk mulai belajar dari repository ini.

Repo ini dirancang untuk belajar **AI Engineering secara bertahap**, dimulai dari pondasi engineering sebelum masuk ke LLM, RAG, AI Agent, dan production system.

---

## Cara Memulai

Clone repository:

```bash
git clone https://github.com/ma2ims/ai-engineer.git
cd ai-engineer
```

Cek struktur repo:

```bash
ls -la
```

Mulai dari Level 1:

```bash
cd modules/level-01-foundation
```

Baca file utama:

```bash
cat README.md
```

---

## Urutan Belajar yang Disarankan

```text
1. Python basic
2. JSON basic
3. API basic
4. Git basic
5. Database basic
6. Linux command
7. Docker basic
8. Mini project: Daily Report API
```

Setelah itu lanjut ke:

```text
Level 2 — LLM Application
Level 3 — RAG System
Level 4 — AI Agent Workflow
Level 5 — Production AI System
```

---

## Target Akhir Level 1

Di akhir Level 1, learner harus bisa membangun project sederhana:

```text
Daily Report API
```

Fitur project:

- menerima data laporan harian dalam format JSON
- menyimpan data ke SQLite database
- menampilkan data lewat API
- berjalan dengan Docker
- menggunakan Git untuk versioning

---

## Jalankan Mini Project

Masuk ke folder project:

```bash
cd projects/daily-report-api
```

Jalankan dengan Docker:

```bash
docker compose up --build
```

Buka browser:

```text
http://localhost:8000/docs
```

Cek health endpoint:

```bash
curl http://localhost:8000/health
```

---

## Cara Belajar Harian

Gunakan pola berikut:

```text
Baca konsep → ketik ulang contoh → jalankan → ubah sedikit → error → fix → commit
```

Contoh commit:

```bash
git add .
git commit -m "Learn Python variable and dictionary"
```

---

## Aturan Belajar

1. Jangan hanya copy-paste. Ketik ulang minimal sekali.
2. Setiap selesai topik, buat commit kecil.
3. Jika error, baca pesan error dulu sebelum bertanya.
4. Catat hal yang belum paham di folder `notes/`.
5. Jangan lanjut ke level berikutnya sebelum mini project berjalan.

---

## Checklist Sebelum Naik ke Level 2

```text
[ ] Bisa menjalankan Python script
[ ] Bisa membaca dan menulis JSON
[ ] Bisa membuat endpoint FastAPI
[ ] Bisa mengirim request POST JSON
[ ] Bisa menyimpan data ke SQLite
[ ] Bisa commit dan push dengan Git
[ ] Bisa menjalankan project dengan Docker Compose
[ ] Bisa menjelaskan alur request: Client → API → Database → Response
```

---

## Mindset

AI Engineering bukan hanya tentang memakai AI tools.

AI Engineering adalah kemampuan membangun sistem yang membuat AI bisa bekerja secara nyata, stabil, aman, dan bisa dikembangkan.
