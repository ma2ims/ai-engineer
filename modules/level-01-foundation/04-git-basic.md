# 04 — Git Basic

Git adalah alat untuk mencatat perubahan kode dan dokumentasi.

Target modul ini: learner bisa memakai Git untuk clone repo, membuat branch, commit progress, push ke GitHub, dan memahami versioning dasar.

---

## Kenapa Git Penting untuk AI Engineer?

AI Engineer tetap bekerja seperti software engineer.

Git dipakai untuk:

```text
- menyimpan histori perubahan kode
- membuat branch eksperimen
- rollback jika ada error
- review perubahan
- kolaborasi dengan tim
- deployment dari repository
```

Dalam repo ini, Git juga dipakai untuk mencatat progress belajar.

---

## 1. Konsep Dasar Git

| Istilah | Arti |
|---|---|
| Repository | Folder project yang dilacak Git |
| Working Directory | Area kerja saat ini |
| Staging Area | Area sebelum commit |
| Commit | Snapshot perubahan |
| Branch | Jalur kerja terpisah |
| Remote | Repository online seperti GitHub |
| Pull | Mengambil update dari remote |
| Push | Mengirim update ke remote |

Alur dasar:

```text
edit file → git add → git commit → git push
```

---

## 2. Setup Awal Git

Cek Git:

```bash
git --version
```

Set nama:

```bash
git config --global user.name "Nama Kamu"
```

Set email:

```bash
git config --global user.email "email@example.com"
```

Cek config:

```bash
git config --list
```

---

## 3. Clone Repository

```bash
git clone https://github.com/ma2ims/ai-engineer.git
cd ai-engineer
```

Cek status:

```bash
git status
```

---

## 4. Branch untuk Belajar

Jangan langsung eksperimen di `main`.

Buat branch belajar:

```bash
git checkout -b learning/level-01-foundation
```

Lihat branch:

```bash
git branch
```

Pindah ke main:

```bash
git checkout main
```

Kembali ke branch belajar:

```bash
git checkout learning/level-01-foundation
```

---

## 5. Commit Pertama

Buat folder catatan pribadi:

```bash
mkdir -p notes
```

Buat file:

```bash
echo "# My AI Engineer Notes" > notes/my-notes.md
```

Cek status:

```bash
git status
```

Masukkan ke staging:

```bash
git add notes/my-notes.md
```

Commit:

```bash
git commit -m "learning: add first learning note"
```

---

## 6. Push ke GitHub

```bash
git push origin learning/level-01-foundation
```

Jika branch belum ada di remote, command ini akan membuat branch remote baru.

---

## 7. Pull Update dari Main

Sebelum belajar, biasakan update dulu:

```bash
git checkout main
git pull origin main
```

Jika sedang di branch belajar dan ingin mengambil update dari main:

```bash
git checkout learning/level-01-foundation
git merge main
```

---

## 8. Melihat Perubahan

Cek file berubah:

```bash
git status
```

Lihat detail perubahan:

```bash
git diff
```

Lihat histori commit:

```bash
git log --oneline
```

---

## 9. Commit Message yang Rapi

Kurang baik:

```bash
git commit -m "update"
git commit -m "fix"
git commit -m "belajar"
```

Lebih baik:

```bash
git commit -m "learning: practice python loop"
git commit -m "docs: add json basic notes"
git commit -m "feat: add report endpoint"
git commit -m "fix: handle report not found"
```

Rekomendasi prefix:

| Prefix | Fungsi |
|---|---|
| `learning` | progress belajar |
| `docs` | dokumentasi |
| `feat` | fitur baru |
| `fix` | perbaikan bug |
| `refactor` | merapikan kode |
| `chore` | maintenance |

---

## 10. Undo Perubahan Aman

Batalkan perubahan satu file yang belum di-commit:

```bash
git restore nama-file.md
```

Batalkan staging:

```bash
git restore --staged nama-file.md
```

Lihat commit terakhir:

```bash
git log --oneline -5
```

---

## 11. Tag Version

Setelah milestone selesai:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Lihat tag:

```bash
git tag
```

Tag membantu menandai versi belajar tertentu.

---

## 12. Git Practice untuk Repo Ini

Latihan 1:

```text
1. Clone repo ai-engineer
2. Buat branch learning/my-progress
3. Buat notes/my-notes.md
4. Commit perubahan
5. Push branch
```

Latihan 2:

```text
1. Buka modules/level-01-foundation/01-python-basic.md
2. Tambahkan catatan pribadi di notes/python-summary.md
3. Commit dengan message learning: add python summary
4. Lihat histori dengan git log --oneline
```

Latihan 3:

```text
1. Jalankan project daily-report-api
2. Ubah response /health
3. Commit dengan message feat: update health response
4. Push ke branch belajar
```

---

## Common Error

### fatal: not a git repository

Artinya kamu belum berada di folder repo.

Cek lokasi:

```bash
pwd
ls
```

Masuk ke folder repo:

```bash
cd ai-engineer
```

### remote origin already exists

Remote sudah terdaftar.

Cek remote:

```bash
git remote -v
```

### rejected because remote contains work

Ambil update dulu:

```bash
git pull origin main
```

---

## Checklist

```text
[ ] Bisa clone repo
[ ] Bisa cek git status
[ ] Bisa membuat branch
[ ] Bisa add file ke staging
[ ] Bisa commit perubahan
[ ] Bisa push branch ke GitHub
[ ] Bisa pull update dari main
[ ] Bisa melihat git diff
[ ] Bisa melihat git log
[ ] Bisa membuat tag version
```

---

## Next Module

Lanjut ke:

```text
05-database-basic.md
```

Di modul database, data API tidak lagi disimpan sementara di memory, tetapi disimpan ke SQLite.
