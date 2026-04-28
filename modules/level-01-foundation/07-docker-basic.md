# 07 — Docker Basic

Docker adalah alat untuk menjalankan aplikasi dalam environment yang konsisten.

Target modul ini: learner paham konsep Docker, bisa membaca Dockerfile, menjalankan project dengan Docker Compose, melihat log, dan menghentikan container.

---

## Kenapa Docker Penting untuk AI Engineer?

AI Engineer sering bekerja dengan banyak service:

```text
- API backend
- database
- vector database
- LLM proxy
- workflow engine
- local model server
- monitoring tools
```

Tanpa Docker, setup bisa berbeda-beda di setiap laptop/server.

Masalah umum:

```text
Di laptop saya jalan, di laptop orang lain error.
```

Docker membantu membuat environment lebih konsisten.

---

## 1. Konsep Dasar Docker

| Istilah | Arti |
|---|---|
| Image | template aplikasi |
| Container | aplikasi yang sedang berjalan dari image |
| Dockerfile | instruksi untuk membuat image |
| Docker Compose | tool untuk menjalankan satu atau banyak service |
| Volume | penyimpanan data/file dari host ke container |
| Port Mapping | menghubungkan port container ke port laptop/server |

Analogi sederhana:

```text
Dockerfile → resep
Image      → hasil masakan siap pakai
Container  → masakan yang sedang disajikan/dijalankan
```

---

## 2. Cek Instalasi Docker

```bash
docker --version
docker compose version
```

Tes Docker:

```bash
docker run hello-world
```

Jika berhasil, Docker siap dipakai.

---

## 3. Command Docker Dasar

Lihat container aktif:

```bash
docker ps
```

Lihat semua container:

```bash
docker ps -a
```

Lihat image:

```bash
docker images
```

Stop container:

```bash
docker stop <container_id_or_name>
```

Hapus container:

```bash
docker rm <container_id_or_name>
```

Hapus image:

```bash
docker rmi <image_id_or_name>
```

---

## 4. Menjalankan Container Sederhana

Jalankan Nginx:

```bash
docker run -p 8080:80 nginx
```

Buka browser:

```text
http://localhost:8080
```

Penjelasan port:

```text
8080 = port di laptop/host
80   = port di dalam container
```

Stop dengan `CTRL + C`, atau cek container lalu stop:

```bash
docker ps
docker stop <container_id>
```

---

## 5. Struktur Docker Project FastAPI

Contoh struktur:

```text
projects/daily-report-api/
├── app/
│   ├── main.py
│   ├── database.py
│   └── models.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 6. Dockerfile FastAPI

Contoh `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Penjelasan:

```text
FROM        = base image
WORKDIR     = folder kerja di container
COPY        = copy file dari host ke container
RUN         = menjalankan command saat build image
EXPOSE      = dokumentasi port aplikasi
CMD         = command default saat container dijalankan
```

---

## 7. Build dan Run Manual

Masuk ke folder project:

```bash
cd projects/daily-report-api
```

Build image:

```bash
docker build -t daily-report-api .
```

Run container:

```bash
docker run -p 8000:8000 daily-report-api
```

Buka:

```text
http://localhost:8000/docs
```

---

## 8. Docker Compose

Docker Compose membuat command lebih singkat dan rapi.

Contoh `docker-compose.yml`:

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      APP_ENV: development
```

Jalankan:

```bash
docker compose up --build
```

Jalankan di background:

```bash
docker compose up -d --build
```

Lihat log:

```bash
docker compose logs -f
```

Stop:

```bash
docker compose down
```

---

## 9. Menjalankan Project Daily Report API

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

Stop project:

```bash
docker compose down
```

---

## 10. Rebuild Saat Dependency Berubah

Jika `requirements.txt` berubah, rebuild image:

```bash
docker compose down
docker compose build --no-cache
docker compose up
```

---

## 11. Volume

Volume membantu file di host terbaca oleh container.

Contoh:

```yaml
volumes:
  - .:/app
```

Artinya:

```text
folder project di laptop disambungkan ke folder /app di container
```

Manfaat:

```text
- perubahan kode bisa langsung terbaca
- cocok untuk development
- tidak perlu rebuild setiap edit file tertentu
```

---

## 12. Environment Variable di Docker Compose

Contoh:

```yaml
environment:
  APP_ENV: development
  DATABASE_NAME: app.db
```

Di Python:

```python
import os

app_env = os.getenv("APP_ENV", "local")
database_name = os.getenv("DATABASE_NAME", "app.db")
```

Untuk data sensitif, jangan hardcode di repo. Gunakan `.env` dan sediakan `.env.example`.

---

## 13. Troubleshooting

### Port 8000 sudah dipakai

Cek port:

```bash
ss -tulpn | grep 8000
```

Solusi cepat: ubah port host di `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"
```

Buka:

```text
http://localhost:8001/docs
```

### Container tidak update

```bash
docker compose down
docker compose up --build
```

### Docker permission denied di Linux

Cek group:

```bash
groups
```

Tambahkan user ke group docker:

```bash
sudo usermod -aG docker $USER
```

Logout/login ulang setelah menjalankan command tersebut.

### ModuleNotFoundError di container

Kemungkinan dependency belum masuk `requirements.txt` atau image belum di-rebuild.

```bash
docker compose build --no-cache
```

---

## Mini Exercise

Latihan 1:

```text
1. Jalankan docker run hello-world
2. Jalankan docker run -p 8080:80 nginx
3. Buka localhost:8080
4. Stop container Nginx
```

Latihan 2:

```text
1. Masuk ke projects/daily-report-api
2. Jalankan docker compose up --build
3. Buka /docs
4. Test /health
5. Stop dengan docker compose down
```

Latihan 3:

```text
1. Ubah response endpoint /health
2. Jalankan ulang Docker Compose
3. Cek perubahan
4. Commit dengan message: learning: practice docker compose
```

---

## Checklist

```text
[ ] Paham image dan container
[ ] Paham fungsi Dockerfile
[ ] Paham fungsi docker-compose.yml
[ ] Bisa menjalankan docker run hello-world
[ ] Bisa menjalankan container dengan port mapping
[ ] Bisa build image manual
[ ] Bisa run container manual
[ ] Bisa menjalankan docker compose up --build
[ ] Bisa melihat log container
[ ] Bisa stop container
[ ] Bisa rebuild container
[ ] Bisa membuka API dari container melalui localhost
```

---

## Final Review Level 1

Setelah modul ini selesai, kembali ke:

```text
modules/level-01-foundation/README.md
```

Pastikan final checklist Level 1 sudah terpenuhi sebelum lanjut ke Level 2.

---

## Next Level

Lanjut ke:

```text
Level 2 — LLM Application
```

Di Level 2, Docker akan membantu menjalankan API yang terhubung ke LLM service, database, dan logging system.
