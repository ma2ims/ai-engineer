# 02 — JSON Basic

JSON adalah format data yang paling sering dipakai dalam API, webhook, konfigurasi aplikasi, logging, dan sistem AI.

Target modul ini: learner bisa membaca, membuat, menyimpan, dan memproses JSON menggunakan Python.

---

## Kenapa JSON Penting?

Dalam AI engineering, JSON sering dipakai untuk:

```text
- request body API
- response API
- structured output dari LLM
- konfigurasi agent
- payload webhook
- log workflow
- pertukaran data antar service
```

Alur umum:

```text
Client → JSON request → API → Database → JSON response
```

---

## 1. Bentuk Dasar JSON

```json
{
  "farm_name": "Tobasa Farm",
  "population": 21000,
  "mortality": 35,
  "feed_used_kg": 1250,
  "average_weight": 1.2,
  "is_active": true
}
```

Aturan penting:

```text
- key harus memakai double quote
- string harus memakai double quote
- boolean memakai true / false
- data kosong memakai null
- tidak boleh ada trailing comma di akhir item
```

---

## 2. JSON Object vs Python Dictionary

Python dictionary:

```python
report = {
    "farm_name": "Tobasa Farm",
    "population": 21000,
    "is_active": True,
    "note": None
}
```

JSON:

```json
{
  "farm_name": "Tobasa Farm",
  "population": 21000,
  "is_active": true,
  "note": null
}
```

Perbedaan:

| Python | JSON |
|---|---|
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |
| dictionary | object |
| list | array |

---

## 3. JSON Array

```json
[
  {
    "id": 1,
    "farm_name": "Kandang A",
    "population": 6000
  },
  {
    "id": 2,
    "farm_name": "Kandang B",
    "population": 15000
  }
]
```

Response API list biasanya dibungkus seperti ini:

```json
{
  "data": [
    {
      "id": 1,
      "farm_name": "Kandang A"
    },
    {
      "id": 2,
      "farm_name": "Kandang B"
    }
  ]
}
```

---

## 4. Membaca JSON String di Python

```python
import json

json_text = '{"farm_name": "Tobasa Farm", "population": 21000}'

data = json.loads(json_text)

print(data["farm_name"])
print(data["population"])
```

```text
json.loads() = mengubah JSON string menjadi Python dictionary/list
```

---

## 5. Mengubah Dictionary ke JSON String

```python
import json

report = {
    "farm_name": "Tobasa Farm",
    "population": 21000,
    "mortality": 35
}

json_text = json.dumps(report, indent=2)
print(json_text)
```

```text
json.dumps() = mengubah Python dictionary/list menjadi JSON string
```

---

## 6. Menulis JSON ke File

```python
import json

report = {
    "date": "2026-04-28",
    "farm_name": "Tobasa Farm",
    "population": 21000,
    "mortality": 35,
    "feed_used_kg": 1250,
    "average_weight": 1.2
}

with open("daily_report.json", "w") as file:
    json.dump(report, file, indent=2)
```

---

## 7. Membaca JSON dari File

```python
import json

with open("daily_report.json", "r") as file:
    data = json.load(file)

print(data["farm_name"])
print(data["mortality"])
```

```text
json.load() = membaca JSON dari file
json.dump() = menulis JSON ke file
```

---

## 8. Validasi Manual Field JSON

```python
required_fields = ["date", "farm_name", "population", "mortality"]

report = {
    "date": "2026-04-28",
    "farm_name": "Tobasa Farm",
    "population": 21000,
    "mortality": 35
}

for field in required_fields:
    if field not in report:
        print(f"Missing field: {field}")
```

Di FastAPI nanti, validasi seperti ini akan dibantu oleh Pydantic model.

---

## Mini Exercise

Buat file:

```text
exercises/json_practice.py
```

Tugas:

```text
1. Buat dictionary laporan harian
2. Simpan ke file daily_report.json
3. Baca kembali file tersebut
4. Hitung estimated biomass = population * average_weight
5. Print summary ke terminal
```

Contoh output:

```text
Daily Report Summary
Farm: Tobasa Farm
Population: 21000
Mortality: 35
Feed Used: 1250 kg
Average Weight: 1.2 kg
Estimated Biomass: 25200 kg
```

---

## Contoh Payload untuk API

Payload ini nanti dipakai untuk test endpoint `POST /reports`.

```json
{
  "date": "2026-04-28",
  "farm_name": "Tobasa Farm",
  "population": 21000,
  "mortality": 35,
  "feed_used_kg": 1250,
  "average_weight": 1.2
}
```

---

## Common Error

### JSONDecodeError

Contoh salah:

```json
{
  "farm_name": "Tobasa Farm",
  "population": 21000,
}
```

Masalahnya ada koma terakhir setelah `21000`.

Contoh benar:

```json
{
  "farm_name": "Tobasa Farm",
  "population": 21000
}
```

---

## Checklist

```text
[ ] Paham JSON object
[ ] Paham JSON array
[ ] Paham perbedaan JSON dan Python dictionary
[ ] Bisa memakai json.loads()
[ ] Bisa memakai json.dumps()
[ ] Bisa membaca JSON dari file
[ ] Bisa menulis JSON ke file
[ ] Bisa membuat payload JSON untuk API
```

---

## Next Module

Lanjut ke:

```text
03-api-basic.md
```
