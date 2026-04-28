# 06 — Linux Command Basic

Linux command adalah pondasi penting untuk bekerja dengan server, Docker, deployment, automation, dan AI infrastructure.

Target modul ini: learner nyaman memakai terminal untuk navigasi folder, menjalankan file, membaca log, mencari file, dan mengecek proses aplikasi.

---

## Kenapa Linux Command Penting untuk AI Engineer?

AI Engineer sering bekerja dengan:

```text
- server Linux
- Docker container
- environment variable
- log aplikasi
- file konfigurasi
- deployment script
- workflow automation
- self-hosted AI stack
```

Banyak pekerjaan AI engineering dilakukan dari terminal.

---

## 1. Cek Lokasi dan Isi Folder

Cek lokasi saat ini:

```bash
pwd
```

Lihat isi folder:

```bash
ls
```

Lihat detail file termasuk hidden file:

```bash
ls -la
```

Contoh:

```bash
cd ai-engineer
pwd
ls -la
```

---

## 2. Navigasi Folder

Masuk folder:

```bash
cd nama-folder
```

Naik satu level:

```bash
cd ..
```

Masuk home directory:

```bash
cd ~
```

Masuk folder project:

```bash
cd ~/workspace/ai-engineer
```

---

## 3. Membuat Folder dan File

Membuat folder:

```bash
mkdir notes
```

Membuat folder bertingkat:

```bash
mkdir -p exercises/linux-practice
```

Membuat file kosong:

```bash
touch notes/linux-notes.md
```

Membuat file dengan isi:

```bash
echo "# Linux Notes" > notes/linux-notes.md
```

Menambahkan isi ke file:

```bash
echo "Belajar command dasar Linux" >> notes/linux-notes.md
```

---

## 4. Membaca Isi File

Baca seluruh file:

```bash
cat notes/linux-notes.md
```

Baca bagian awal file:

```bash
head notes/linux-notes.md
```

Baca bagian akhir file:

```bash
tail notes/linux-notes.md
```

Baca log realtime:

```bash
tail -f app.log
```

---

## 5. Copy, Move, Rename, Delete

Copy file:

```bash
cp notes/linux-notes.md notes/linux-notes-backup.md
```

Rename file:

```bash
mv notes/linux-notes-backup.md notes/linux-backup.md
```

Pindah file ke folder lain:

```bash
mv notes/linux-backup.md exercises/linux-practice/
```

Hapus file:

```bash
rm exercises/linux-practice/linux-backup.md
```

Hapus folder kosong:

```bash
rmdir exercises/linux-practice
```

Hapus folder beserta isi:

```bash
rm -rf exercises/linux-practice
```

Hati-hati:

```text
rm -rf bisa menghapus banyak file tanpa konfirmasi.
Pastikan lokasi folder benar sebelum menjalankan command ini.
```

---

## 6. Cari File dan Teks

Cari file berdasarkan nama:

```bash
find . -name "README.md"
```

Cari file Python:

```bash
find . -name "*.py"
```

Cari teks dalam file:

```bash
grep "FastAPI" README.md
```

Cari teks di semua file dalam folder:

```bash
grep -r "FastAPI" .
```

Cari teks tanpa case sensitive:

```bash
grep -ri "docker" .
```

---

## 7. Melihat Proses dan Port

Lihat proses aktif:

```bash
ps aux
```

Cari proses Python:

```bash
ps aux | grep python
```

Lihat port yang sedang dipakai:

```bash
ss -tulpn
```

Cari port 8000:

```bash
ss -tulpn | grep 8000
```

Kill process:

```bash
kill -9 <PID>
```

Contoh:

```bash
kill -9 12345
```

---

## 8. Environment Variable

Environment variable sering dipakai untuk config aplikasi.

Set sementara:

```bash
export APP_ENV=development
```

Cek value:

```bash
echo $APP_ENV
```

Contoh dipakai di Python:

```python
import os

app_env = os.getenv("APP_ENV", "local")
print(app_env)
```

Catatan:

```text
Environment variable yang dibuat dengan export hanya aktif di terminal session tersebut.
```

---

## 9. Permission Dasar

Lihat permission:

```bash
ls -la
```

Membuat script bisa dieksekusi:

```bash
chmod +x scripts/check.sh
```

Jalankan script:

```bash
./scripts/check.sh
```

---

## 10. Command untuk Project Ini

Dari root repo:

```bash
pwd
ls -la
```

Masuk ke project API:

```bash
cd projects/daily-report-api
```

Lihat file:

```bash
ls -la
find . -maxdepth 2 -type f
```

Cari endpoint API:

```bash
grep -r "@app" app/
```

Jalankan Docker:

```bash
docker compose up --build
```

Stop Docker:

```bash
docker compose down
```

---

## Mini Exercise

Latihan 1:

```text
1. Masuk ke root repo ai-engineer
2. Buat folder notes
3. Buat file notes/linux-practice.md
4. Isi file dengan 5 command Linux yang dipelajari
5. Baca file dengan cat
6. Commit ke Git
```

Latihan 2:

```text
1. Cari semua file README.md di repo
2. Cari kata Docker di seluruh repo
3. Masuk ke projects/daily-report-api
4. Jalankan docker compose up --build
5. Cek port 8000
6. Stop container
```

---

## Common Error

### No such file or directory

Folder/file tidak ditemukan.

Solusi:

```bash
pwd
ls -la
```

Pastikan kamu ada di folder yang benar.

### Permission denied

File belum punya izin execute.

Solusi:

```bash
chmod +x nama-file.sh
```

### Port already in use

Port sedang dipakai proses lain.

Solusi:

```bash
ss -tulpn | grep 8000
kill -9 <PID>
```

---

## Checklist

```text
[ ] Bisa memakai pwd
[ ] Bisa memakai ls dan ls -la
[ ] Bisa navigasi dengan cd
[ ] Bisa membuat folder dengan mkdir
[ ] Bisa membuat file dengan touch/echo
[ ] Bisa membaca file dengan cat/head/tail
[ ] Bisa copy file dengan cp
[ ] Bisa rename/move file dengan mv
[ ] Bisa hapus file/folder dengan rm
[ ] Bisa mencari file dengan find
[ ] Bisa mencari teks dengan grep
[ ] Bisa melihat process dengan ps aux
[ ] Bisa cek port dengan ss
[ ] Bisa memakai environment variable
[ ] Bisa menjalankan script dengan chmod +x
```

---

## Next Module

Lanjut ke:

```text
07-docker-basic.md
```

Docker akan dipakai agar project bisa dijalankan ulang oleh siapa pun setelah clone repo.
