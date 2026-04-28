# AI Engineer Learning Roadmap

Dokumen ini adalah panduan belajar bertahap untuk membangun pondasi sebagai AI Engineer.

## Tujuan Utama

Belajar AI Engineering bukan dimulai dari membuat model besar dari nol. Untuk tahap awal, fokusnya adalah memahami fondasi software engineering yang dibutuhkan agar bisa membangun aplikasi AI nyata.

Fondasi utama:

1. Python basic
2. JSON
3. API
4. Git & GitHub
5. Database
6. Linux command
7. Docker

Setelah fondasi ini kuat, baru masuk ke LLM application, RAG, agent workflow, dan production AI system.

---

## Level 1 — Foundation

Target:

- Bisa membuat script Python sederhana
- Bisa membuat API sederhana
- Bisa menerima dan mengirim data JSON
- Bisa menyimpan data ke database
- Bisa memakai Git untuk versioning
- Bisa menjalankan project dengan Docker

Output akhir:

```text
Daily Report API
```

API sederhana untuk mencatat laporan harian, menyimpan data ke SQLite, dan dijalankan dengan Docker.

---

## Level 2 — LLM Application

Target:

- Menghubungkan aplikasi ke LLM API
- Membuat prompt template
- Mengatur structured output JSON
- Membuat chat history
- Mencatat token/cost sederhana

Output akhir:

```text
LLM Assistant API
```

API sederhana yang menerima pertanyaan, mengirim ke LLM, lalu mengembalikan jawaban terstruktur.

---

## Level 3 — RAG System

Target:

- Memahami document ingestion
- Memahami chunking
- Membuat embedding
- Menyimpan vector ke database
- Melakukan retrieval berdasarkan pertanyaan

Output akhir:

```text
Document Q&A API
```

User bisa upload/catat dokumen, lalu bertanya berdasarkan isi dokumen tersebut.

---

## Level 4 — Agent Workflow

Target:

- Memahami tool calling
- Membuat workflow multi-step
- Menyimpan memory sederhana
- Membuat human approval untuk action penting

Output akhir:

```text
Operational AI Agent
```

Agent sederhana yang bisa membaca data, menganalisis, membuat ringkasan, dan menjalankan action terbatas.

---

## Level 5 — Production AI System

Target:

- Logging
- Monitoring
- Evaluation
- Error handling
- Security basic
- Deployment flow

Output akhir:

```text
Production-ready AI service
```

Sistem AI yang lebih siap dipakai, mudah dipantau, dan mudah diperbaiki.

---

## Cara Menggunakan Repo Ini

1. Clone repository

```bash
git clone https://github.com/ma2ims/ai-engineer.git
cd ai-engineer
```

2. Mulai dari Level 1

```bash
cd level-01-foundation
```

3. Baca README level

```bash
cat README.md
```

4. Jalankan mini project

```bash
cd mini-project-daily-report-api
docker compose up --build
```

5. Commit progress belajar

```bash
git add .
git commit -m "Complete level 01 exercise"
```

---

## Prinsip Belajar

```text
Jangan hanya baca.
Ketik ulang kode.
Jalankan.
Rusakkan sedikit.
Perbaiki error.
Commit.
Ulangi.
```

Skill engineering tumbuh dari praktik, bukan dari membaca teori saja.
