# Kalkulator Falak
### Lembaga Falakiyah Nahdlatul Ulama — Wuluhan Jember

[![Versi](https://img.shields.io/badge/versi-1.0.0-blue)](CHANGELOG.md)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-lightgrey)](https://www.microsoft.com/windows)
[![Electron](https://img.shields.io/badge/Electron-38.x-47848F?logo=electron)](https://electronjs.org)
[![Lisensi](https://img.shields.io/badge/lisensi-MIT-green)](LICENSE)

---

## Tentang Aplikasi

**Kalkulator Falak** adalah aplikasi desktop kalkulator ilmiah yang dirancang khusus
untuk kebutuhan **ilmu falak** (astronomi Islam). Aplikasi ini berjalan sepenuhnya
**offline** sebagai aplikasi desktop Windows mandiri.

### Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| **Kalkulator 2-Baris** | Display formula di baris 1 + hasil real-time di baris 2 |
| **Trigonometri Lengkap** | sin, cos, tan, sin⁻¹, cos⁻¹, tan⁻¹ |
| **Mode DEG / RAD** | Toggle satuan sudut derajat atau radian |
| **Input DMS** | Input langsung format Derajat° Menit' Detik" |
| **Konversi DD ↔ DMS** | Toggle format hasil antara desimal dan DMS |
| **Fungsi Matematika** | log, ln, √, x², xʸ, π |
| **Navigasi Kursor** | Edit di mana saja dalam formula tanpa menghapus |
| **Memory ANS** | Gunakan hasil terakhir dalam kalkulasi berikutnya |
| **Keyboard Shortcut** | Input cepat via keyboard |
| **Offline Penuh** | Tidak memerlukan koneksi internet |

---

## Cara Menggunakan

### Input Formula
1. Ketik angka dan operator menggunakan tombol di layar atau keyboard
2. Hasil preview tampil otomatis di baris bawah
3. Tekan **=** atau **Enter** untuk menghitung

### Keyboard Shortcut

| Tombol | Fungsi |
|--------|--------|
| `s` | sin |
| `c` | cos |
| `t` | tan |
| `Shift+S` | sin⁻¹ (asin) |
| `Shift+C` | cos⁻¹ (acos) |
| `Shift+T` | tan⁻¹ (atan) |
| `d` | Simbol derajat (°) |
| `'` | Simbol menit (') |
| `"` | Simbol detik (") |
| `ArrowLeft` / `ArrowRight` | Navigasi kursor |
| `Home` / `End` | Awal / Akhir formula |
| `Enter` / `=` | Hitung |
| `Backspace` | Hapus karakter sebelum kursor |
| `Escape` | AC — Reset semua |
| `*` | Operator kali (×) |
| `/` | Operator bagi (÷) |

### Input DMS (Derajat-Menit-Detik)
1. Ketik derajat: `90`
2. Tekan `d` atau tombol **° ' "**: tambah simbol `°` → `90°`
3. Ketik menit: `90°30`
4. Tekan `'` atau tombol **° ' "**: tambah simbol `'` → `90°30'`
5. Ketik detik: `90°30'0`
6. Tekan `"` atau tombol **° ' "**: tambah simbol `"` → `90°30'0"`

### Konversi Format Hasil
- Klik tombol **FORMAT: DD** untuk toggle antara Desimal (DD) dan DMS
- Saat menekan tombol **° ' "** setelah tekan `=`, juga akan toggle format

---

## Instalasi

### Prasyarat
- Windows 10 atau Windows 11 (64-bit)
- [Node.js LTS](https://nodejs.org/) — diperlukan hanya untuk build dari source

### Cara 1: Menggunakan Installer (Direkomendasikan)
1. Download file `Kalkulator Falak Setup 1.x.x.exe` dari folder `dist/`
2. Jalankan installer
3. Ikuti petunjuk instalasi
4. Buka aplikasi dari Desktop atau Start Menu

### Cara 2: Menjalankan dari Source Code

```powershell
# 1. Pastikan Node.js LTS sudah terinstall
node --version

# 2. Clone atau extract proyek ke folder lokal

# 3. Masuk ke direktori proyek
cd Kalkulator_Falak

# 4. Install dependensi
npm install

# 5. Jalankan aplikasi
npm start
```

### Cara 3: Build Installer dari Source

```powershell
# Install dependensi
npm install

# Build installer .exe
npm run dist

# Installer tersedia di:
# dist/Kalkulator Falak Setup 1.x.x.exe
```

---

## Struktur Proyek

```
Kalkulator_Falak/
├── assets/               <- Ikon dan aset gambar
│   ├── icon.ico
│   ├── icon.png
│   └── logo-nu.png
├── docs/                 <- Dokumentasi proyek
│   ├── PRD.md            <- Product Requirements Document
│   ├── DEVPLAN.md        <- Development Plan
│   ├── DEVLOG.md         <- Development Log
│   └── ARCHITECTURE.md  <- Dokumentasi Arsitektur
├── src/                  <- Source code terpisah (v1.1.0+)
│   ├── calculator.js
│   └── preload.js
├── index.html            <- UI utama kalkulator
├── main.js               <- Electron main process
├── package.json          <- Konfigurasi npm & build
├── README.md             <- File ini
├── CHANGELOG.md          <- Riwayat perubahan versi
└── SECURITY.md           <- Kebijakan keamanan
```

---

## Pengembangan

Lihat dokumen berikut untuk informasi pengembangan lebih lanjut:

- [PRD.md](docs/PRD.md) — Product Requirements Document
- [DEVPLAN.md](docs/DEVPLAN.md) — Rencana pengembangan dan milestone
- [DEVLOG.md](docs/DEVLOG.md) — Log aktivitas pengembangan
- [ARCHITECTURE.md](docs/ARCHITECTURE.md) — Dokumentasi arsitektur teknis
- [CHANGELOG.md](CHANGELOG.md) — Riwayat perubahan versi
- [SECURITY.md](SECURITY.md) — Kebijakan keamanan

---


## Kredit & Pengembang

| Peran | Nama / Lembaga |
|-------|----------------|
| **Pengembang Aplikasi** | Fuad Baidāwī Al-Fajri |
| **Pembuat Aplikasi Asal** | Lembaga Falakiyah MWCNU Wuluhan Jember |

Aplikasi ini dikembangkan oleh **Fuad Baidāwī Al-Fajri** sebagai pengembangan dan penyempurnaan
dari aplikasi kalkulator falak yang telah dibuat oleh **Lembaga Falakiyah MWCNU Wuluhan Jember**.

---
## Lisensi

MIT License — Copyright (c) 2026 Fuad Baidāwī Al-Fajri

Berdasarkan karya Lembaga Falakiyah MWCNU Wuluhan Jember.

---

## Kontak

**Lembaga Falakiyah Nahdlatul Ulama**
Wuluhan, Jember, Jawa Timur