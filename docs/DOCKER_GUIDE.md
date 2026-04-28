# Docker Guide

Dokumen ini menjelaskan dasar Docker untuk menjalankan project di repo `ai-engineer` secara konsisten di local machine orang lain.

---

## Kenapa Docker Penting?

Docker membantu memastikan project berjalan dengan environment yang sama, walaupun dijalankan di laptop atau server yang berbeda.

Masalah yang ingin dihindari:

```text
Di laptop saya jalan, di laptop orang lain error.
```

Dengan Docker, dependency, runtime, dan command run bisa distandarkan.

---

## Konsep Dasar Docker

| Istilah | Arti |
|---|---|
| Image | Template aplikasi |
| Container | Instance aplikasi yang sedang berjalan |
| Dockerfile | Instruksi untuk membuat image |
| Docker Compose | Tool untuk menjalankan satu atau banyak service |
| Volume | Penyimpanan data/file dari container |
| Port Mapping | Menghubungkan port container ke host |

---

## Cek Instalasi Docker

```bash
docker --version
docker compose version
```

Tes Docker:

```bash
docker run hello-world
```

---

## Command Dasar

Lihat container aktif:

```bash
docker ps
```

Lihat semua container:

```bash
docker ps -a
```

Lihat images:

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

## Dockerfile Project FastAPI

Contoh struktur:

```text
projects/daily-report-api/
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

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

---

## Docker Compose

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

## Menjalankan Daily Report API

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

---

## Rebuild Saat Dependency Berubah

Jika `requirements.txt` berubah:

```bash
docker compose build --no-cache
docker compose up
```

---

## Troubleshooting

### Port 8000 sudah dipakai

Cek proses:

```bash
ss -tulpn | grep 8000
```

Atau ubah port di `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"
```

Lalu buka:

```text
http://localhost:8001/docs
```

### Container tidak update setelah edit kode

Coba rebuild:

```bash
docker compose down
docker compose up --build
```

### Permission error di Linux

Cek apakah user punya akses Docker:

```bash
groups
```

Jika belum masuk group docker:

```bash
sudo usermod -aG docker $USER
```

Logout/login ulang setelah command tersebut.

---

## Docker Practice

Latihan 1:

```text
1. Jalankan docker run hello-world
2. Jalankan project daily-report-api dengan docker compose
3. Buka /docs
4. Stop container dengan docker compose down
```

Latihan 2:

```text
1. Ubah response /health
2. Jalankan ulang container
3. Cek perubahan di browser atau curl
4. Commit perubahan ke Git
```

---

## Checklist Docker Basic

```text
[ ] Bisa cek versi Docker
[ ] Bisa menjalankan hello-world
[ ] Paham image dan container
[ ] Bisa membaca Dockerfile sederhana
[ ] Bisa menjalankan docker compose up
[ ] Bisa melihat log container
[ ] Bisa stop container
[ ] Bisa rebuild container
[ ] Bisa membuka API dari container lewat localhost
```

---

## Prinsip

```text
Docker bukan tujuan akhir.
Docker adalah alat agar project mudah dijalankan ulang oleh siapa pun.
```
