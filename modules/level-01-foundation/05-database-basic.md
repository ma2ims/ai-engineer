# 05 — Database Basic

Database adalah tempat menyimpan data secara permanen.

Target modul ini: learner memahami konsep database dasar, SQL dasar, dan bisa memakai SQLite dari Python.

---

## Kenapa Database Penting untuk AI Engineer?

Sistem AI hampir selalu membutuhkan penyimpanan data.

Contoh penggunaan database:

```text
- menyimpan user
- menyimpan chat history
- menyimpan dokumen
- menyimpan log AI request dan response
- menyimpan hasil analisis
- menyimpan konfigurasi agent
- menyimpan workflow run history
```

Tanpa database, data akan hilang saat aplikasi berhenti.

---

## 1. Jenis Database

Untuk awal, pahami dua kategori besar:

| Jenis | Contoh | Cocok untuk |
|---|---|---|
| Relational Database | SQLite, PostgreSQL, MySQL | data terstruktur |
| NoSQL / Document DB | MongoDB, Firebase | data fleksibel/document |

Untuk Level 1, fokus ke:

```text
SQLite + SQL basic
```

SQLite cocok untuk belajar karena tidak perlu server database terpisah.

---

## 2. Konsep Dasar Relational Database

| Istilah | Arti |
|---|---|
| Table | tempat menyimpan data |
| Column | field/atribut data |
| Row | satu baris data |
| Primary Key | ID unik setiap row |
| SQL | bahasa query database |
| Query | perintah ke database |

Contoh table `daily_reports`:

| id | date | farm_name | mortality | feed_used_kg |
|---:|---|---|---:|---:|
| 1 | 2026-04-28 | Tobasa Farm | 35 | 1250 |
| 2 | 2026-04-29 | Tobasa Farm | 40 | 1300 |

---

## 3. SQL Dasar

### CREATE TABLE

```sql
CREATE TABLE daily_reports (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date TEXT NOT NULL,
  farm_name TEXT NOT NULL,
  population INTEGER NOT NULL,
  mortality INTEGER NOT NULL,
  feed_used_kg REAL NOT NULL,
  average_weight REAL NOT NULL
);
```

### INSERT

```sql
INSERT INTO daily_reports (
  date,
  farm_name,
  population,
  mortality,
  feed_used_kg,
  average_weight
) VALUES (
  '2026-04-28',
  'Tobasa Farm',
  21000,
  35,
  1250,
  1.2
);
```

### SELECT

```sql
SELECT * FROM daily_reports;
```

### SELECT by ID

```sql
SELECT * FROM daily_reports WHERE id = 1;
```

### UPDATE

```sql
UPDATE daily_reports
SET mortality = 40
WHERE id = 1;
```

### DELETE

```sql
DELETE FROM daily_reports
WHERE id = 1;
```

---

## 4. SQLite dari Python

Python punya module bawaan untuk SQLite:

```python
import sqlite3
```

Buat file:

```text
create_database.py
```

Isi:

```python
import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS daily_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    farm_name TEXT NOT NULL,
    population INTEGER NOT NULL,
    mortality INTEGER NOT NULL,
    feed_used_kg REAL NOT NULL,
    average_weight REAL NOT NULL
)
""")

connection.commit()
connection.close()

print("Database and table created")
```

Jalankan:

```bash
python create_database.py
```

---

## 5. Insert Data dengan Python

Buat file:

```text
insert_report.py
```

Isi:

```python
import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO daily_reports (
    date,
    farm_name,
    population,
    mortality,
    feed_used_kg,
    average_weight
) VALUES (?, ?, ?, ?, ?, ?)
""", (
    "2026-04-28",
    "Tobasa Farm",
    21000,
    35,
    1250,
    1.2
))

connection.commit()
connection.close()

print("Report inserted")
```

Kenapa pakai `?`?

```text
Agar lebih aman daripada memasukkan value langsung ke string SQL.
Ini membantu menghindari SQL injection.
```

---

## 6. Read Data dengan Python

Buat file:

```text
read_reports.py
```

Isi:

```python
import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM daily_reports")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
```

---

## 7. Read Data by ID

```python
import sqlite3

report_id = 1

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM daily_reports WHERE id = ?", (report_id,))
row = cursor.fetchone()

if row is None:
    print("Report not found")
else:
    print(row)

connection.close()
```

Catatan penting:

```text
(report_id,) memakai koma karena Python perlu tuple.
```

---

## 8. Update Data

```python
import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("""
UPDATE daily_reports
SET mortality = ?
WHERE id = ?
""", (40, 1))

connection.commit()
connection.close()

print("Report updated")
```

---

## 9. Delete Data

```python
import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM daily_reports WHERE id = ?", (1,))

connection.commit()
connection.close()

print("Report deleted")
```

---

## 10. Hubungan Database dengan API

Di project `daily-report-api`, alurnya akan seperti ini:

```text
POST /reports
    ↓
Pydantic validate JSON
    ↓
Insert data ke SQLite
    ↓
Return JSON response
```

Untuk GET:

```text
GET /reports
    ↓
SELECT data dari SQLite
    ↓
Convert row ke dictionary
    ↓
Return JSON response
```

---

## Mini Exercise

Buat folder latihan:

```text
exercises/database-practice/
```

Buat file:

```text
create_table.py
insert_report.py
read_reports.py
read_report_by_id.py
update_report.py
delete_report.py
```

Requirement:

```text
[ ] Bisa membuat table daily_reports
[ ] Bisa insert satu report
[ ] Bisa membaca semua report
[ ] Bisa membaca report by ID
[ ] Bisa update mortality
[ ] Bisa delete report
```

---

## Common Error

### no such table: daily_reports

Table belum dibuat.

Solusi:

```bash
python create_database.py
```

### database is locked

Biasanya connection belum ditutup atau ada proses lain yang masih memakai database.

Solusi:

```text
- pastikan connection.close() dipanggil
- stop server/API yang sedang berjalan
- jalankan ulang script
```

### Incorrect number of bindings supplied

Jumlah `?` tidak sama dengan jumlah value.

Cek:

```python
cursor.execute("SELECT * FROM daily_reports WHERE id = ?", (report_id,))
```

---

## Checklist

```text
[ ] Paham table, row, column
[ ] Paham primary key
[ ] Bisa CREATE TABLE
[ ] Bisa INSERT
[ ] Bisa SELECT
[ ] Bisa SELECT by ID
[ ] Bisa UPDATE
[ ] Bisa DELETE
[ ] Bisa menggunakan sqlite3 dari Python
[ ] Paham alur API → Database → JSON response
```

---

## Next Module

Lanjut ke:

```text
06-linux-command.md
```

Linux command akan dipakai untuk navigasi project, menjalankan script, membaca file, dan debugging.
