# PRD — Product Requirements Document
## Kalkulator Falak | Dikembangkan oleh Fuad Baidāwī Al-Fajri

**Versi Dokumen:** 1.0.0
**Tanggal:** 12 September 2026
**Status:** Aktif
**Pengembang:** Fuad Baidāwī Al-Fajri  
**PIC / Pembuat Asal:** Lembaga Falakiyah MWCNU Wuluhan Jember

---

## 1. Latar Belakang & Tujuan Produk

### 1.1 Latar Belakang

Ilmu falak (astronomi Islam) memerlukan perhitungan matematis yang intensif, terutama fungsi
trigonometri dan konversi satuan sudut (Derajat-Menit-Detik / DMS). Para ahli falak di lingkungan Lembaga Falakiyah MWCNU Wuluhan Jember membutuhkan alat kalkulator yang:

> Aplikasi ini dikembangkan oleh **Fuad Baidāwī Al-Fajri** sebagai penyempurnaan dari
> aplikasi asal yang dibuat oleh **Lembaga Falakiyah MWCNU Wuluhan Jember**.


- Mudah digunakan tanpa memerlukan koneksi internet
- Mendukung konversi DMS secara langsung
- Dapat dijalankan sebagai aplikasi desktop mandiri di Windows

### 1.2 Tujuan Produk

Menghadirkan **kalkulator ilmiah desktop** yang khusus dirancang untuk kebutuhan ilmu falak,
dapat berjalan **penuh offline** di sistem operasi Windows, dengan antarmuka yang intuitif dan andal.

### 1.3 Visi Jangka Panjang

Menjadi alat bantu hitung standar bagi para mustahiq falak di lingkungan Nahdlatul Ulama,
dengan kemungkinan pengembangan ke platform Android di masa mendatang.

---

## 2. Target Pengguna (User Persona)

### Persona Utama: Ahli Falak

| Atribut | Detail |
|---------|--------|
| **Peran** | Ustaz/Ustazah Falak |
| **Usia** | 25 – 65 tahun |
| **Keahlian Teknologi** | Menengah (terbiasa pakai komputer/laptop) |
| **Kebutuhan Utama** | Menghitung jadwal shalat, arah kiblat, awal bulan |
| **Perangkat** | Laptop/PC Windows 10/11 |
| **Koneksi** | Sering tanpa internet (di pesantren/lapangan) |

### Persona Sekunder: Pelajar Ilmu Falak

| Atribut | Detail |
|---------|--------|
| **Peran** | Santri / Mahasiswa Ilmu Falak |
| **Usia** | 16 – 30 tahun |
| **Keahlian Teknologi** | Menengah hingga tinggi |
| **Kebutuhan Utama** | Berlatih hitungan falak, verifikasi hasil manual |
| **Perangkat** | Laptop Windows 10/11 |

---

## 3. Fitur Produk

### 3.1 Fitur Inti — Must Have (MVP)

| ID | Fitur | Deskripsi | Prioritas |
|----|-------|-----------|-----------|
| F01 | Kalkulator Ilmiah 2-Baris | Display formula + hasil real-time | P0 |
| F02 | Fungsi Trigonometri | sin, cos, tan, sin⁻¹, cos⁻¹, tan⁻¹ | P0 |
| F03 | Mode DEG / RAD | Toggle satuan sudut | P0 |
| F04 | Input DMS | Input Derajat° Menit' Detik" | P0 |
| F05 | Konversi Format Hasil | Toggle hasil DD vs DMS | P0 |
| F06 | Fungsi Matematika Lengkap | log, ln, akar, x², xʸ, π | P0 |
| F07 | Navigasi Kursor | Tombol Kiri/Kanan, Home, End | P0 |
| F08 | Memory ANS | Menyimpan hasil terakhir | P0 |
| F09 | Keyboard Shortcut | Shortkey s/c/t, d/'/", navigasi | P0 |
| F10 | Offline Penuh | Berjalan tanpa internet | P0 |

### 3.2 Fitur Tambahan — Should Have

| ID | Fitur | Deskripsi | Prioritas |
|----|-------|-----------|-----------|
| F11 | Ikon Aplikasi Kustom | Icon .ico branding NU | P1 |
| F12 | Pesan Error Deskriptif | NaN, Infinity, Domain Error | P1 |
| F13 | Validasi Input Real-time | Mencegah double operator | P1 |
| F14 | Riwayat Kalkulasi | History 10 perhitungan terakhir | P1 |

### 3.3 Fitur Masa Depan — Nice to Have

| ID | Fitur | Deskripsi | Prioritas |
|----|-------|-----------|-----------|
| F15 | Mode Kalkulator Khusus Falak | Panel waktu shalat, arah kiblat | P2 |
| F16 | Ekspor Hasil | Export ke PDF/CSV | P2 |
| F17 | Tema Terang/Gelap | Toggle tema warna | P2 |
| F18 | Versi Android (APK) | Port ke Android via Capacitor | P3 |

---

## 4. Persyaratan Non-Fungsional

### 4.1 Performa
- Waktu startup aplikasi: **< 3 detik** di hardware standar
- Latensi evaluasi real-time: **< 50ms** setelah input
- Ukuran installer: **< 150 MB**

### 4.2 Keamanan
- **Tidak boleh menggunakan `eval()`** untuk eksekusi ekspresi matematika
- `contextIsolation: true`, `nodeIntegration: false` wajib dipertahankan
- Tidak ada akses ke filesystem atau jaringan dari renderer process

### 4.3 Kompatibilitas
- **Sistem Operasi:** Windows 10 (64-bit) dan Windows 11
- **Arsitektur:** x64 utama, arm64 opsional
- **Resolusi Minimum:** 1024×768

### 4.4 Aksesibilitas
- Semua tombol memiliki `aria-label` yang deskriptif
- Kontras warna memenuhi WCAG 2.1 Level AA
- Navigasi keyboard penuh

### 4.5 Keandalan
- Semua aset (gambar, CSS, JS) tersimpan lokal
- Tidak ada dependensi eksternal runtime

---

## 5. Batasan Produk (Out of Scope)

- Bukan kalkulator jadwal shalat otomatis (memerlukan data lokasi GPS)
- Bukan aplikasi web yang di-hosting di server
- Tidak mendukung Windows 7/8/8.1 (EOL)
- Tidak ada fitur sinkronisasi cloud

---

## 6. Alur Pengguna (User Flow Utama)

```
[Buka Aplikasi]
      |
      v
[Tampil Display Kosong — READY]
      |
      +-- [Tekan Tombol / Keyboard]
      |         |
      |         v
      |   [Formula Tampil di Baris 1]
      |   [Hasil Preview di Baris 2 — Status: PREVIEW]
      |         |
      |         +-- [Tekan =]
      |         |       |
      |         |       v
      |         |   [Status: RESULT]
      |         |   [ANS diperbarui]
      |         |   [Edit rumus masih bisa tanpa hapus]
      |         |
      |         +-- [Tekan AC]
      |                 |
      |                 v
      |             [Reset total — READY]
      |
      +-- [Toggle DEG/RAD] --> [Hitung ulang otomatis]
      +-- [Toggle Format DD/DMS] --> [Format hasil berubah]
```

---

## 7. Kriteria Penerimaan (Acceptance Criteria)

| ID | Kriteria | Cara Verifikasi |
|----|----------|-----------------|
| AC01 | Aplikasi berjalan tanpa internet | Matikan WiFi, buka aplikasi — harus normal |
| AC02 | sin(30) dalam DEG = 0.5 | Input dan verifikasi hasil |
| AC03 | 90°30'0" terkonversi = 90.5 | Input DMS dan cek DD |
| AC04 | Installer dapat diinstall & uninstall bersih | Test di VM Windows bersih |
| AC05 | Logo NU tampil di header | Visual check |
| AC06 | Shortkey keyboard berfungsi | Test semua shortkey terdokumentasi |
| AC07 | ANS menyimpan hasil terakhir | Hitung 5+3=8, lalu ANS×2=16 |
| AC08 | Pesan error informatif | Coba 1÷0, asin(2) |

---

## 8. Stack Teknologi

### Stack Saat Ini (v1.0.0)

| Komponen | Teknologi | Status |
|----------|-----------|--------|
| Desktop Shell | Electron ^38.1.0 | OK |
| UI Styling | Tailwind CSS via CDN | MASALAH (offline) |
| Expression Parser | JavaScript eval() | MASALAH (keamanan) |
| Logika Kalkulator | Vanilla JS inline di HTML | MASALAH (maintainability) |
| Build Tool | electron-builder ^26.0.12 | OK |

### Stack Target (v1.1.0)

| Komponen | Teknologi | Status |
|----------|-----------|--------|
| Desktop Shell | Electron ^38.1.0 | - |
| UI Styling | Tailwind CSS (local build) | Target |
| Expression Parser | math.js ^13.x | Target |
| Logika Kalkulator | Vanilla JS (file terpisah) | Target |
| Build Tool | electron-builder ^26.0.12 | - |

---

## 9. Risiko & Mitigasi

| Risiko | Dampak | Kemungkinan | Mitigasi |
|--------|--------|-------------|----------|
| eval() dieksploitasi | Tinggi | Rendah | Ganti dengan math.js |
| CDN Tailwind tidak tersedia offline | Tinggi | Sedang | Bundle Tailwind lokal |
| File aset hilang saat build | Tinggi | Sudah terjadi | Fix package.json files list |
| Electron + builder tidak kompatibel | Sedang | Rendah | Test build CI |
| Formula falak tidak akurat | Tinggi | Rendah | Validasi dengan ahli falak |

---

## 10. Timeline & Milestone

| Milestone | Target | Deskripsi |
|-----------|--------|-----------|
| M0 — Hotfix Kritis | Minggu 1 (Sep 2026) | Fix logo hilang, fix package.json |
| M1 — Security Fix | Minggu 2 (Sep 2026) | Ganti eval() dengan math.js |
| M2 — Offline Fix | Minggu 3 (Okt 2026) | Bundle Tailwind lokal, pisahkan JS |
| M3 — Polish | Minggu 4 (Okt 2026) | Error messages, validasi, ikon |
| M4 — Release v1.1.0 | Minggu 5 (Okt 2026) | Build, test, distribusi installer |
| M5 — Riwayat Kalkulasi | Nov 2026 | History kalkulasi |
| M6 — Mode Falak | Des 2026 – Jan 2027 | Panel khusus falak |