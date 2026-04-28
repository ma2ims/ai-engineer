# 01 — Python Basic

Python dipakai sebagai bahasa utama untuk scripting, backend API, data processing, automation, dan AI engineering.

Target modul ini: bisa membaca dan menulis kode Python dasar.

---

## Materi Inti

```text
- variable
- data type
- list
- dictionary
- condition
- loop
- function
- error handling
- file handling
```

---

## 1. Variable dan Data Type

```python
farm_name = "Tobasa Farm"
population = 21000
average_weight = 1.2
is_active = True

print(farm_name)
print(population)
print(average_weight)
print(is_active)
```

Tipe data dasar:

```text
str   = teks
int   = angka bulat
float = angka desimal
bool  = True / False
list  = kumpulan data
dict  = data key-value
```

---

## 2. List

```python
farms = ["Kandang A", "Kandang B", "Kandang C"]

farms.append("Kandang D")

for farm in farms:
    print(farm)
```

Latihan:

```text
Buat list berisi 5 nama kandang.
Tampilkan semua nama kandang menggunakan loop.
```

---

## 3. Dictionary

Dictionary mirip dengan JSON dan sangat sering dipakai di API.

```python
report = {
    "farm_name": "Tobasa Farm",
    "population": 21000,
    "mortality": 35,
    "feed_used_kg": 1250,
    "average_weight": 1.2
}

print(report["farm_name"])
print(report["mortality"])
```

Latihan:

```text
Buat dictionary data laporan harian dengan field:
- date
- farm_name
- population
- mortality
- feed_used_kg
- average_weight
```

---

## 4. Condition

```python
mortality = 120
limit = 100

if mortality > limit:
    print("Warning: mortality is high")
else:
    print("Mortality is normal")
```

Latihan:

```text
Jika FCR lebih dari 1.7, tampilkan "Need review".
Jika tidak, tampilkan "Still normal".
```

---

## 5. Loop

```python
daily_feed = [100, 120, 130, 150]

total_feed = 0

for feed in daily_feed:
    total_feed = total_feed + feed

print(total_feed)
```

Latihan:

```text
Buat list mortalitas harian selama 7 hari.
Hitung total mortalitas.
```

---

## 6. Function

```python
def calculate_depletion(dead_chicken, initial_population):
    return dead_chicken / initial_population * 100

result = calculate_depletion(35, 21000)
print(result)
```

Latihan:

```text
Buat function untuk menghitung:
- depletion
- total feed
- estimated biomass
```

---

## 7. Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Latihan:

```text
Buat function pembagian.
Jika pembagi 0, tampilkan pesan error yang jelas.
```

---

## 8. File Handling

Menulis file:

```python
with open("daily-report.txt", "w") as file:
    file.write("Daily report created")
```

Membaca file:

```python
with open("daily-report.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## Mini Exercise

Buat file `practice_report.py` yang:

```text
1. Menyimpan data laporan harian dalam dictionary
2. Menghitung depletion percentage
3. Menghitung estimated biomass
4. Menampilkan summary ke terminal
```

Contoh output:

```text
Farm: Tobasa Farm
Population: 21000
Mortality: 35
Depletion: 0.17%
Estimated Biomass: 25200 kg
```

---

## Checklist

```text
[ ] Bisa membuat variable
[ ] Bisa menggunakan list
[ ] Bisa menggunakan dictionary
[ ] Bisa membuat if/else
[ ] Bisa menggunakan loop
[ ] Bisa membuat function
[ ] Bisa menangani error sederhana
[ ] Bisa membaca dan menulis file
```
