# Git Workflow Guide

Dokumen ini menjelaskan cara memakai Git di repo `ai-engineer` untuk belajar secara rapi, aman, dan mudah diikuti oleh orang lain.

---

## Tujuan Git Workflow

Git digunakan untuk:

- mencatat progres belajar
- menyimpan histori perubahan kode
- membuat branch eksperimen
- rollback jika terjadi error
- membiasakan workflow software engineering
- membuat repo mudah di-clone dan dipelajari learner lain

---

## Setup Awal

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

Cek konfigurasi:

```bash
git config --list
```

---

## Clone Repository

```bash
git clone https://github.com/ma2ims/ai-engineer.git
cd ai-engineer
```

Cek status:

```bash
git status
```

---

## Branch Utama

Branch utama repo:

```text
main
```

Aturan:

- `main` harus tetap rapi
- hindari eksperimen langsung di `main`
- buat branch baru untuk belajar atau perubahan besar

---

## Membuat Branch Belajar

Contoh:

```bash
git checkout -b learning/level-01-foundation
```

Cek branch aktif:

```bash
git branch
```

Pindah ke branch lain:

```bash
git checkout main
```

---

## Workflow Harian

Setiap selesai latihan kecil:

```bash
git status
git add .
git commit -m "learning: practice python dictionary"
```

Push branch ke GitHub:

```bash
git push origin learning/level-01-foundation
```

---

## Commit yang Baik

Commit sebaiknya kecil dan jelas.

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
git commit -m "feat: add create report endpoint"
git commit -m "fix: return 404 when report not found"
```

---

## Commit Type

| Type | Contoh |
|---|---|
| `docs` | `docs: add docker guide` |
| `learning` | `learning: practice sql select query` |
| `feat` | `feat: add report API endpoint` |
| `fix` | `fix: handle database connection error` |
| `refactor` | `refactor: split database helper` |
| `chore` | `chore: update gitignore` |
| `test` | `test: add health check test` |

---

## Pull Update dari Remote

Sebelum mulai kerja, biasakan:

```bash
git checkout main
git pull origin main
```

Kalau sedang di branch belajar:

```bash
git checkout learning/level-01-foundation
git merge main
```

---

## Melihat Perubahan

Cek file yang berubah:

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

## Undo Perubahan

Batalkan perubahan file yang belum di-commit:

```bash
git checkout -- nama-file
```

Batalkan semua perubahan yang belum di-commit:

```bash
git restore .
```

Hapus file dari staging:

```bash
git restore --staged nama-file
```

---

## Pull Request Workflow

Jika ingin belajar workflow profesional:

1. Buat branch baru
2. Commit perubahan
3. Push branch
4. Buat Pull Request ke `main`
5. Review perubahan
6. Merge jika sudah aman

Command:

```bash
git checkout -b docs/update-level-01
git add .
git commit -m "docs: update level 01 checklist"
git push origin docs/update-level-01
```

---

## Tag Versi

Saat milestone selesai:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Lihat semua tag:

```bash
git tag
```

---

## Git Practice untuk Learner

Latihan 1:

```text
1. Clone repo
2. Buat branch learning/my-first-branch
3. Buat file notes/my-note.md
4. Commit file tersebut
5. Push branch ke GitHub
```

Latihan 2:

```text
1. Ubah README project
2. Cek git diff
3. Commit perubahan
4. Lihat histori dengan git log --oneline
```

---

## Checklist Git Basic

```text
[ ] Bisa clone repo
[ ] Bisa cek git status
[ ] Bisa membuat branch
[ ] Bisa commit perubahan
[ ] Bisa push branch
[ ] Bisa pull update dari main
[ ] Bisa melihat git diff
[ ] Bisa melihat git log
[ ] Bisa membuat tag version
```

---

## Prinsip

```text
Commit kecil lebih baik daripada commit besar yang membingungkan.
Branch adalah tempat aman untuk eksperimen.
README yang jelas membuat repo mudah dipelajari orang lain.
```
