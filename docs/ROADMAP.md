# AI Engineer Learning Roadmap

Roadmap ini dibuat untuk belajar AI Engineering dari dasar sampai production-ready system.

Fokus utama:

```text
Foundation → LLM Application → RAG → Agent Workflow → Production AI System
```

Repo ini tidak hanya berisi teori, tetapi diarahkan untuk menghasilkan project yang bisa dijalankan, dibaca, dan dikembangkan oleh learner lain.

---

## Level 1 — Foundation

Tujuan: memahami pondasi engineering sebelum masuk ke aplikasi AI.

Materi:

- Python basic
- JSON basic
- API basic
- Git basic
- Database basic
- Linux command
- Docker basic

Project:

```text
projects/daily-report-api
```

Skill yang harus dikuasai:

```text
[ ] Membuat script Python sederhana
[ ] Membaca dan menulis JSON
[ ] Membuat API dengan FastAPI
[ ] Menerima request body dalam format JSON
[ ] Mengembalikan response JSON
[ ] Menyimpan data ke SQLite
[ ] Menggunakan Git branch, commit, dan push
[ ] Menjalankan aplikasi dengan Docker Compose
[ ] Menjelaskan alur Client → API → Database → Response
```

Output portfolio:

```text
Daily Report API
```

---

## Level 2 — LLM Application

Tujuan: membuat aplikasi sederhana yang terhubung ke Large Language Model secara terkontrol.

Materi:

- LLM API basic
- prompt template
- system prompt
- user prompt
- structured output JSON
- chat history
- error handling
- token and cost logging
- simple model routing

Project:

```text
projects/llm-chat-api
```

Skill yang harus dikuasai:

```text
[ ] Mengirim prompt ke LLM API
[ ] Membuat prompt template
[ ] Menghasilkan response JSON terstruktur
[ ] Menyimpan chat history
[ ] Menangani error dari API model
[ ] Mencatat token usage dan cost sederhana
```

Output portfolio:

```text
LLM Chat API
```

---

## Level 3 — RAG System

Tujuan: membuat AI bisa menjawab berdasarkan dokumen atau knowledge base.

Materi:

- document ingestion
- text chunking
- embedding
- vector database
- semantic search
- retrieval
- source citation
- context injection ke prompt

Project:

```text
projects/rag-knowledge-api
```

Skill yang harus dikuasai:

```text
[ ] Upload dokumen
[ ] Memecah dokumen menjadi chunks
[ ] Membuat embedding
[ ] Menyimpan embedding ke vector database
[ ] Mengambil context paling relevan
[ ] Menjawab berdasarkan source
[ ] Mengurangi hallucination dengan retrieval context
```

Output portfolio:

```text
SOP Question Answering API
```

---

## Level 4 — AI Agent Workflow

Tujuan: membuat AI tidak hanya menjawab, tetapi bisa menjalankan langkah kerja.

Materi:

- tool calling
- function calling
- workflow orchestration
- task routing
- memory
- approval flow
- retry and fallback
- workflow logging

Project:

```text
projects/ai-agent-workflow
```

Skill yang harus dikuasai:

```text
[ ] Agent bisa memilih tool
[ ] Agent bisa mengambil data dari API/database
[ ] Agent bisa membuat summary
[ ] Agent bisa menjalankan workflow multi-step
[ ] Agent bisa meminta approval untuk action berisiko
[ ] Agent bisa mencatat hasil eksekusi workflow
```

Output portfolio:

```text
Daily Operations Assistant
```

---

## Level 5 — Production AI System

Tujuan: menjalankan sistem AI dengan standar production.

Materi:

- deployment
- CI/CD
- monitoring
- logging
- evaluation
- prompt versioning
- model fallback
- security
- access control
- cost control

Project:

```text
projects/production-ai-assistant
```

Skill yang harus dikuasai:

```text
[ ] Deploy API ke server/cloud
[ ] Membuat log request dan response
[ ] Membuat evaluation dataset
[ ] Memantau latency dan error
[ ] Mengatur fallback model
[ ] Mengamankan API key dan environment variable
[ ] Menyusun basic LLMOps workflow
```

Output portfolio:

```text
Production AI Assistant System
```

---

## Rekomendasi Durasi

```text
Level 1: 2–4 minggu
Level 2: 2–4 minggu
Level 3: 3–6 minggu
Level 4: 4–8 minggu
Level 5: ongoing
```

Durasi bisa lebih cepat atau lambat. Yang penting setiap level menghasilkan project yang berjalan.

---

## Pola Belajar Harian

```text
30% baca konsep
70% praktik langsung
```

Rutinitas:

```text
1. Baca satu konsep
2. Ketik ulang contoh kode
3. Jalankan kode
4. Ubah sedikit kodenya
5. Baca error jika muncul
6. Fix error
7. Commit perubahan
8. Tulis catatan singkat
```

---

## Completion Rule

Sebuah level dianggap selesai jika:

```text
[ ] Project berjalan lokal
[ ] Project berjalan dengan Docker
[ ] README project jelas
[ ] Kode sudah di-commit ke Git
[ ] Learner bisa menjelaskan fungsi setiap file
[ ] Learner bisa menjelaskan alur data dari input sampai output
```

---

## Output Portfolio Setelah Semua Level

```text
1. Daily Report API
2. LLM Chat API
3. SOP RAG Assistant
4. AI Agent Workflow
5. Production AI Assistant System
```

Dengan lima project ini, learner punya bukti praktik yang cukup kuat untuk menunjukkan kemampuan sebagai AI Engineer pemula sampai intermediate.
