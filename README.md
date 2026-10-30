
# Pertemuan 13 - Debugging dan Testing

Nama: Indah Palupi Kusumaningrum
NIM: 2225250212
Kelas: 3F

## Kasus
Program yang diuji adalah program debugging untuk menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | Rata-rata [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | Rata-rata [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | Status nilai 60 | Lulus | Tidak lulus | FAIL |
| T4 | Status nilai 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | Nilai tertinggi [80, 60, 90, 70] | 90 | 0 | FAIL |

## Bug Report

### B01 - Perhitungan Rata-rata
- Gejala: Hasil rata-rata salah.
- Test case: T1 dan T2.
- Lokasi: Fungsi `hitung_rata_rata()`.
- Akar penyebab: Total nilai selalu dibagi 5, bukan jumlah data.
- Perbaikan: Membagi total dengan `len(nilai)` dan menangani data kosong.
- Retest: PASS.

### B02 - Status Kelulusan
- Gejala: Nilai 60 dinyatakan tidak lulus.
- Test case: T3.
- Lokasi: Fungsi `status()`.
- Akar penyebab: Kondisi `nilai > 60` tidak memasukkan nilai batas 60.
- Perbaikan: Mengubah kondisi menjadi `nilai >= 60`.
- Retest: PASS.

### B03 - Nilai Tertinggi
- Gejala: Program menghasilkan nilai tertinggi yang salah.
- Test case: T5.
- Lokasi: Fungsi `nilai_tertinggi()`.
- Akar penyebab: Nilai dibandingkan menggunakan operator `<`, bukan `>`.
- Perbaikan: Memperbaiki operator perbandingan dan inisialisasi nilai tertinggi.
- Retest: PASS.

## Retest

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

## Cara Menjalankan

```bash
python praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah tracing dan testing karena membantu mengetahui letak kesalahan, memahami akar penyebabnya, dan memastikan perbaikan menghasilkan output yang benar.
