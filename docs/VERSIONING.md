# Versioning Guide

Dokumen ini menjelaskan cara menggunakan versioning di repo pembelajaran `ai-engineer`.

Versioning dipakai agar progres belajar, perubahan kode, dan milestone pembelajaran mudah dilacak.

---

## Current Learning Version

```text
v0.1.0 — Level 1 Foundation
```

---

## Version Format

Repo ini memakai format sederhana:

```text
MAJOR.MINOR.PATCH
```

Contoh:

```text
v0.1.0
v0.1.1
v0.2.0
v1.0.0
```

---

## Arti Setiap Angka

| Bagian | Contoh | Arti |
|---|---:|---|
| MAJOR | `1.x.x` | perubahan besar atau learning path sudah lengkap |
| MINOR | `x.2.x` | penambahan level/module/project baru |
| PATCH | `x.x.1` | perbaikan kecil, typo, contoh kode, dokumentasi |

---

## Milestone Version

| Version | Scope | Status |
|---|---|---|
| v0.1.0 | Level 1 Foundation | Active |
| v0.2.0 | Level 2 LLM Application | Planned |
| v0.3.0 | Level 3 RAG System | Planned |
| v0.4.0 | Level 4 AI Agent Workflow | Planned |
| v0.5.0 | Level 5 Production AI System | Planned |
| v1.0.0 | Complete AI Engineer Learning Path | Planned |

---

## Branch Naming

Gunakan branch yang mudah dibaca:

```bash
git checkout -b learning/level-01-foundation
git checkout -b docs/add-docker-guide
git checkout -b project/daily-report-api
git checkout -b fix/api-validation
```

Rekomendasi prefix:

| Prefix | Fungsi |
|---|---|
| `learning/` | progres belajar pribadi |
| `docs/` | update dokumentasi |
| `project/` | project baru |
| `feature/` | fitur baru |
| `fix/` | perbaikan bug |
| `chore/` | maintenance kecil |

---

## Commit Message Convention

Format:

```text
<type>: <short message>
```

Contoh:

```bash
git commit -m "docs: add level 01 roadmap"
git commit -m "feat: add daily report endpoint"
git commit -m "fix: handle missing report id"
git commit -m "chore: update docker compose"
```

Type yang disarankan:

| Type | Fungsi |
|---|---|
| `docs` | dokumentasi |
| `feat` | fitur baru |
| `fix` | bug fix |
| `refactor` | merapikan kode tanpa ubah behavior |
| `test` | test |
| `chore` | maintenance |
| `learning` | catatan atau latihan pembelajaran |

---

## Tagging Version

Saat satu milestone selesai, buat tag:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Lihat tag:

```bash
git tag
```

Checkout ke versi tertentu:

```bash
git checkout v0.1.0
```

---

## Kapan Naik Version?

### PATCH

Naik dari `v0.1.0` ke `v0.1.1` jika:

- typo diperbaiki
- README dirapikan
- contoh command diperbaiki
- bug kecil di project diperbaiki

### MINOR

Naik dari `v0.1.0` ke `v0.2.0` jika:

- level baru ditambahkan
- project baru ditambahkan
- modul pembelajaran baru ditambahkan

### MAJOR

Naik ke `v1.0.0` jika:

- learning path utama lengkap
- project utama setiap level tersedia
- dokumentasi cukup jelas untuk learner lain

---

## Release Note Template

Gunakan format ini di `CHANGELOG.md`:

```md
## v0.1.0 — 2026-04-28

### Added
- Level 1 Foundation documentation
- Daily Report API project
- Docker setup

### Changed
- Updated README structure

### Fixed
- Minor docs cleanup
```

---

## Prinsip Versioning Repo Ini

```text
Small progress is still progress.
Commit often.
Tag important milestones.
Keep the repo readable for future learners.
```
