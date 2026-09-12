import os

BASE = r"c:\Projects\Kalkulator_Falak"
DOCS = os.path.join(BASE, "docs")
os.makedirs(DOCS, exist_ok=True)

# ============================================================
# PRD.md
# ============================================================
PRD = r"""# PRD — Product Requirements Document
## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember

**Versi Dokumen:** 1.0.0
**Tanggal:** 12 September 2026
**Status:** Aktif
**PIC:** Lembaga Falakiyah NU Wuluhan Jember

---

## 1. Latar Belakang & Tujuan Produk

### 1.1 Latar Belakang

Ilmu falak (astronomi Islam) memerlukan perhitungan matematis yang intensif, terutama fungsi
trigonometri dan konversi satuan sudut (Derajat-Menit-Detik / DMS). Para ahli falak di lingkungan
Lembaga Falakiyah NU Wuluhan Jember membutuhkan alat kalkulator yang:

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
"""

# ============================================================
# DEVPLAN.md
# ============================================================
DEVPLAN = r"""# DEVPLAN — Development Plan
## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember

**Versi:** 1.0.0
**Tanggal:** 12 September 2026
**Status:** Aktif

---

## 1. Gambaran Umum

Rencana pengembangan dibagi dalam **3 Fase** dan **6 Milestone** berurutan.
Setiap fase tidak boleh dilanjutkan sebelum semua item di fase sebelumnya terverifikasi.

```
FASE 1 — Stabilisasi (v1.0.x)
  +-- M0: Hotfix Kritis     (fix logo, fix build)
  +-- M1: Security Fix      (hapus eval, pakai math.js)

FASE 2 — Modernisasi (v1.1.0)
  +-- M2: Offline & Arsitektur  (Tailwind lokal, pisah JS)
  +-- M3: Polish & UX           (ikon, error messages, a11y)
  +-- M4: Release v1.1.0        (build, test, distribusi)

FASE 3 — Pengembangan Fitur (v1.2.0+)
  +-- M5: Riwayat Kalkulasi
  +-- M6: Mode Falak Khusus
```

---

## 2. Struktur Direktori Target (v1.1.0)

```
Kalkulator_Falak/
├── assets/
│   ├── icon.ico              <- ikon aplikasi Windows
│   ├── icon.png              <- ikon 512x512 px
│   └── logo-nu.png           <- logo NU (pindah dari root)
├── docs/
│   ├── PRD.md
│   ├── DEVPLAN.md
│   ├── DEVLOG.md
│   └── ARCHITECTURE.md
├── src/
│   ├── calculator.js         <- logika kalkulator (dipisah dari HTML)
│   ├── preload.js            <- Electron preload script
│   ├── input.css             <- Tailwind source CSS
│   └── output.css            <- Tailwind compiled CSS (generated)
├── index.html
├── main.js
├── package.json
├── tailwind.config.js
├── postcss.config.js
├── README.md
├── CHANGELOG.md
└── SECURITY.md
```

---

## 3. Detail Milestone

---

### MILESTONE 0 — Hotfix Kritis
**Target:** Minggu 1 September 2026
**Branch:** `hotfix/m0-critical`
**Versi Target:** v1.0.1

| # | Tugas | File | Estimasi |
|---|-------|------|----------|
| T0.1 | Buat direktori assets/ | struktur proyek | 5 menit |
| T0.2 | Tambahkan/sediakan logo-nu.png | assets/logo-nu.png | 30 menit |
| T0.3 | Update referensi gambar di HTML | index.html baris 183 | 10 menit |
| T0.4 | Tambahkan semua aset ke files di package.json | package.json | 10 menit |
| T0.5 | Test build installer | - | 1 jam |

**Kriteria Selesai:**
- [ ] Logo NU tampil di header
- [ ] Build installer berhasil
- [ ] Installer memuat semua aset dengan benar

---

### MILESTONE 1 — Security Fix
**Target:** Minggu 2 September 2026
**Branch:** `fix/m1-security`
**Versi Target:** v1.0.2

| # | Tugas | File | Estimasi |
|---|-------|------|----------|
| T1.1 | Download/bundle math.js secara lokal | vendor/math.min.js | 30 menit |
| T1.2 | Refactor parseFormula() untuk math.js | index.html / calculator.js | 4 jam |
| T1.3 | Ganti semua eval() dengan math.evaluate() | index.html | 1 jam |
| T1.4 | Sesuaikan helper DEG agar kompatibel math.js | index.html | 2 jam |
| T1.5 | Test semua fungsi kalkulator | - | 2 jam |
| T1.6 | Test edge cases (NaN, Infinity, DMS) | - | 1 jam |

**Catatan Teknis — math.js:**
```
// Mode DEG dengan math.js:
math.evaluate('sin(30 deg)')       -> 0.5
math.evaluate('asin(0.5) / deg')   -> 30
math.evaluate('log(100, 10)')      -> 2
math.evaluate('sqrt(16)')          -> 4
math.evaluate('2 ^ 10')            -> 1024
```

**Kriteria Selesai:**
- [ ] Tidak ada penggunaan eval() dalam kode
- [ ] Semua uji fungsional lulus
- [ ] Tidak ada regresi fitur

---

### MILESTONE 2 — Offline & Arsitektur
**Target:** Minggu 3 Oktober 2026
**Branch:** `refactor/m2-offline-arch`
**Versi Target:** v1.1.0-alpha

| # | Tugas | File | Estimasi |
|---|-------|------|----------|
| T2.1 | Install tailwindcss, postcss, autoprefixer | package.json | 30 menit |
| T2.2 | Setup tailwind.config.js dan postcss.config.js | config files | 30 menit |
| T2.3 | Buat src/input.css dengan Tailwind directives | src/input.css | 15 menit |
| T2.4 | Build CSS: npx tailwindcss -i src/input.css -o src/output.css | - | 15 menit |
| T2.5 | Update index.html: ganti CDN script dengan local CSS link | index.html | 10 menit |
| T2.6 | Ekstrak semua JS ke src/calculator.js | src/calculator.js | 3 jam |
| T2.7 | Buat src/preload.js | src/preload.js | 1 jam |
| T2.8 | Update main.js untuk sertakan preload | main.js | 20 menit |
| T2.9 | Update package.json files dan scripts | package.json | 20 menit |
| T2.10 | Test aplikasi offline penuh | - | 1 jam |

**npm scripts baru:**
```json
{
  "scripts": {
    "start": "npm run build:css && electron .",
    "build:css": "npx tailwindcss -i ./src/input.css -o ./src/output.css --minify",
    "watch:css": "npx tailwindcss -i ./src/input.css -o ./src/output.css --watch",
    "dist": "npm run build:css && electron-builder --win nsis",
    "dev": "npx concurrently \"npm run watch:css\" \"electron .\""
  }
}
```

**Kriteria Selesai:**
- [ ] Aplikasi berjalan normal tanpa internet
- [ ] JS terpisah dari HTML
- [ ] preload.js aktif
- [ ] Build menghasilkan installer yang berfungsi offline

---

### MILESTONE 3 — Polish & UX
**Target:** Minggu 4 Oktober 2026
**Branch:** `improve/m3-polish-ux`
**Versi Target:** v1.1.0-beta

| # | Tugas | File | Estimasi |
|---|-------|------|----------|
| T3.1 | Buat/desain ikon aplikasi (icon.ico, icon.png) | assets/ | 2 jam |
| T3.2 | Tambahkan ikon di main.js dan package.json | main.js, package.json | 30 menit |
| T3.3 | Perbaiki pesan error: NaN, Infinity, Domain | calculator.js | 1 jam |
| T3.4 | Tambahkan validasi double-operator di input | calculator.js | 1 jam |
| T3.5 | Tambahkan aria-label pada semua tombol | index.html | 1 jam |
| T3.6 | Enkapsulasi semua state dalam IIFE/module | calculator.js | 2 jam |
| T3.7 | Disable DevTools di production build | main.js | 20 menit |
| T3.8 | Tambahkan crash handler di main process | main.js | 1 jam |
| T3.9 | Update copyright di build config | package.json | 10 menit |

**Kriteria Selesai:**
- [ ] Ikon kustom tampil di taskbar dan installer
- [ ] Pesan error informatif untuk semua kasus
- [ ] Semua tombol memiliki aria-label
- [ ] DevTools tidak muncul di production build

---

### MILESTONE 4 — Release v1.1.0
**Target:** Minggu 5 Oktober 2026
**Branch:** `release/v1.1.0`
**Versi Target:** v1.1.0

| # | Tugas | Estimasi |
|---|-------|----------|
| T4.1 | Update versi di package.json ke 1.1.0 | 5 menit |
| T4.2 | Update CHANGELOG.md | 30 menit |
| T4.3 | Full regression test semua fitur | 2 jam |
| T4.4 | Build installer .exe | 30 menit |
| T4.5 | Test install di VM Windows 10 bersih | 1 jam |
| T4.6 | Test install di VM Windows 11 | 30 menit |
| T4.7 | Distribusi installer ke Lembaga Falakiyah | - |

---

### MILESTONE 5 — Riwayat Kalkulasi (v1.2.0)
**Target:** November 2026
**Branch:** `feature/m5-history`

**Deskripsi:**
Panel riwayat kalkulasi yang menampilkan 10 perhitungan terakhir. Pengguna
dapat mengklik item riwayat untuk memuat ulang rumus ke display.

**Desain UI:**
- Panel collapsible di bawah kalkulator utama
- Setiap item: [Formula] --> [Hasil]
- Tombol "Muat" untuk recall, tombol "Hapus Semua"

**Tugas Utama:**
- Implementasi array history max 10 item (LIFO)
- Render panel history dengan toggle show/hide
- Handle klik item untuk load ke formula

---

### MILESTONE 6 — Mode Falak Khusus (v1.3.0)
**Target:** Desember 2026 – Januari 2027
**Branch:** `feature/m6-falak-mode`

**Deskripsi:**
Tab/panel terpisah dengan fungsi kalkulasi falak yang umum digunakan.

**Kandidat Fitur:**
- Konversi waktu lokal ke waktu hakiki (equation of time)
- Perhitungan deklinasi matahari (formula aproksimasi)
- Konversi koordinat (lintang/bujur)
- Perhitungan sudut waktu shalat

**Riset Diperlukan:**
- Formula standar dari kitab falak (Khulasoh, Sullam, dll.)
- Validasi akurasi formula dengan ahli falak NU

---

## 4. Panduan Branching & Commit

### Naming Convention Branch:
```
hotfix/<milestone>-<deskripsi>    (perbaikan darurat)
fix/<milestone>-<deskripsi>       (perbaikan bug)
refactor/<milestone>-<deskripsi>  (refactoring kode)
improve/<milestone>-<deskripsi>   (peningkatan UX/performa)
feature/<milestone>-<deskripsi>   (fitur baru)
release/<versi>                   (merge ke main untuk release)
```

### Format Commit Message (Conventional Commits):
```
<type>(<scope>): <deskripsi singkat>

[opsional: body penjelasan lebih lanjut]
[opsional: BREAKING CHANGE: ...]
```

**Types:** fix | feat | refactor | style | docs | build | chore

**Contoh:**
```
fix(assets): tambahkan logo-nu.png dan update path di index.html
fix(security): ganti eval() dengan math.evaluate() - closes #1
feat(ux): tambahkan pesan error deskriptif untuk NaN dan Infinity
refactor(arch): pisahkan logika JS dari HTML ke calculator.js
build(css): setup Tailwind lokal, hapus CDN dependency
docs: upgrade README.txt ke README.md dengan dokumentasi lengkap
```

---

## 5. Standar Kode

### JavaScript
- Gunakan `const` dan `let`, hindari `var`
- Enkapsulasi semua state dalam IIFE atau ES Module
- Tidak ada penggunaan `eval()` dalam bentuk apapun
- Komentar wajib untuk logika yang tidak trivial
- Gunakan arrow functions untuk callback

### HTML
- Semua elemen interaktif wajib memiliki `aria-label`
- Atribut `alt` wajib pada semua `<img>`
- Gunakan semantic HTML5 `<main>`, `<header>`, `<section>`

### CSS (Tailwind)
- Gunakan class Tailwind untuk semua styling dasar
- Custom CSS `<style>` hanya untuk animasi dan efek khusus

---

## 6. Test Matrix QA

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| Trig DEG | sin(30) | 0.5 |
| Trig RAD | sin(pi/6) | 0.5 |
| Invers DEG | asin(0.5) | 30 |
| DMS ke DD | 90°30'0" | 90.5 |
| DD ke DMS | 90.5 (format DMS) | 90° 30' 0.00" |
| Power | 2^10 | 1024 |
| Log10 | log(100) | 2 |
| Ln | ln(e) | 1 |
| Sqrt | sqrt(16) | 4 |
| ANS | 5+3= lalu ANS*2 | 16 |
| Kurung | (2+3)*4 | 20 |
| Negatif | -5*-3 | 15 |
| Division by zero | 1/0 | Error Infinity |
| Domain error | asin(2) | Domain Error |
| Double minus | 5--3 | 8 |
| Pi | pi*2 | 6.28318... |
"""

# ============================================================
# DEVLOG.md
# ============================================================
DEVLOG = r"""# DEVLOG — Development Log
## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember

Log ini mencatat semua aktivitas pengembangan secara kronologis.
Tambahkan entri baru di ATAS (terbaru di paling atas).

---

## Format Entri

```
### [YYYY-MM-DD] — Judul Aktivitas
**Kontributor:** Nama
**Milestone:** M0 / M1 / dst.
**Status:** IN PROGRESS | DONE | BLOCKED | DITUNDA

#### Yang Dikerjakan:
- ...

#### Temuan / Catatan:
- ...

#### Langkah Berikutnya:
- ...
```

---

## Log Aktivitas

---

### [2026-09-12] — Analisis Mendalam Kode & Pembuatan Dokumen Perencanaan
**Kontributor:** Tim Pengembang (dengan bantuan Antigravity AI)
**Milestone:** Pra-M0 (Perencanaan)
**Status:** DONE

#### Yang Dikerjakan:
- Analisis mendalam seluruh kode: index.html (705 baris), main.js (31 baris), package.json, README.txt
- Identifikasi 2 masalah kritis, 8 masalah sedang, dan 7 masalah kecil
- Pembuatan laporan analisis lengkap dalam format Markdown
- Pembuatan dokumen PRD.md
- Pembuatan dokumen DEVPLAN.md
- Pembuatan dokumen DEVLOG.md (file ini)
- Pembuatan dokumen CHANGELOG.md
- Pembuatan dokumen ARCHITECTURE.md
- Pembuatan dokumen SECURITY.md
- Upgrade README.txt ke README.md
- Pembuatan struktur direktori docs/

#### Temuan Kritis:
1. Penggunaan eval() di index.html baris 600 dan 616 — RISIKO KEAMANAN
2. File logo-nu.png tidak ada di direktori proyek — tampil broken image
3. Tailwind CSS diambil dari CDN — aplikasi gagal tampil offline
4. File aset tidak terdaftar di package.json files — tidak masuk ke installer

#### Langkah Berikutnya:
- Mulai Milestone 0: Hotfix Kritis
  * Sediakan file logo-nu.png di assets/
  * Update referensi path logo di index.html
  * Update package.json files list
  * Test build installer v1.0.1

---

### [2026-09-12] — Inisialisasi Proyek (v1.0.0)
**Kontributor:** Tim Lembaga Falakiyah NU Wuluhan Jember
**Milestone:** -
**Status:** DONE

#### Yang Dikerjakan:
- Setup proyek Electron dari template HTML kalkulator
- Implementasi antarmuka kalkulator 2-baris dengan desain 3D
- Implementasi fungsi trigonometri (sin, cos, tan dan invers)
- Implementasi mode DEG/RAD
- Implementasi input dan konversi DMS
- Implementasi navigasi kursor (kiri/kanan)
- Implementasi keyboard shortcut
- Konfigurasi electron-builder untuk installer Windows NSIS
- Rilis v1.0.0

#### Catatan:
- Desain UI 3D kalkulator dinilai sangat bagus secara visual
- Fungsionalitas dasar sudah berjalan dengan baik
- Masalah keamanan (eval) dan infrastruktur (CDN, aset) perlu ditangani
"""

# ============================================================
# CHANGELOG.md
# ============================================================
CHANGELOG = r"""# CHANGELOG
## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember

Format berdasarkan [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
dan mengikuti [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Direncanakan (M0 — Hotfix Kritis)
- Menambahkan file logo NU (logo-nu.png) ke direktori assets/
- Memperbaiki referensi path logo di index.html
- Mendaftarkan semua aset ke `files` di package.json
- Build installer v1.0.1

### Direncanakan (M1 — Security Fix)
- Mengganti `eval()` dengan `math.evaluate()` dari library math.js
- Refactor `parseFormula()` untuk kompatibel dengan math.js API
- Menambahkan math.js sebagai dependensi lokal (tidak via CDN)

### Direncanakan (M2 — Offline & Arsitektur)
- Install dan bundle Tailwind CSS secara lokal (hapus CDN dependency)
- Ekstrak semua JavaScript dari index.html ke src/calculator.js
- Buat src/preload.js untuk Electron IPC
- Update main.js dengan preload dan crash handler

### Direncanakan (M3 — Polish & UX)
- Tambahkan ikon aplikasi kustom (.ico) branding NU
- Perbaiki pesan error menjadi lebih deskriptif (NaN, Infinity, Domain Error)
- Tambahkan validasi mencegah double operator
- Tambahkan aria-label pada semua tombol untuk aksesibilitas
- Enkapsulasi variabel global dalam module pattern
- Nonaktifkan DevTools di production build

---

## [1.0.0] — 2026-09-12

### Ditambahkan
- Antarmuka kalkulator ilmiah 2-baris dengan desain 3D realistis
- Fungsi trigonometri: sin, cos, tan
- Fungsi trigonometri invers: sin⁻¹ (asin), cos⁻¹ (acos), tan⁻¹ (atan)
- Toggle mode DEG / RAD untuk satuan sudut
- Input DMS (Derajat° Menit' Detik") langsung di display
- Tombol DMS Smart yang otomatis menentukan simbol berikutnya (°, ', ")
- Konversi format hasil: Desimal (DD) ↔ DMS
- Fungsi matematika: log (log10), ln, akar (√), pangkat (xʸ), kuadrat (x²)
- Konstanta π (pi)
- Navigasi kursor dua arah (Kiri ◄ / Kanan ►)
- Memory ANS untuk menyimpan hasil terakhir
- Keyboard shortcut lengkap:
  - s/c/t → sin/cos/tan
  - Shift+S/C/T → asin/acos/atan
  - d → derajat (°), ' → menit, " → detik
  - ArrowLeft/Right → navigasi kursor
  - Home/End → awal/akhir formula
  - Enter/= → hitung
  - Backspace → hapus
  - Escape → AC (reset)
- Auto-balancing tanda kurung
- Live preview hasil saat mengetik
- Evaluasi setelah tekan = tetap mempertahankan formula untuk diedit
- Animasi kursor berkedip (custom caret)
- Packaging Electron sebagai aplikasi desktop Windows
- Installer NSIS via electron-builder

### Ketergantungan
- Electron ^38.1.0
- electron-builder ^26.0.12
- Tailwind CSS (via CDN — akan diganti di v1.1.0)
"""

# ============================================================
# ARCHITECTURE.md
# ============================================================
ARCHITECTURE = r"""# ARCHITECTURE.md — Dokumentasi Arsitektur
## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember

**Versi:** 1.0.0
**Tanggal:** 12 September 2026

---

## 1. Gambaran Umum Arsitektur

Aplikasi Kalkulator Falak adalah aplikasi **desktop berbasis Electron** yang membungkus
antarmuka HTML/CSS/JavaScript. Arsitektur terdiri dari dua lapisan utama:

```
+------------------------------------------+
|          Electron Shell (Node.js)        |
|  +------------------------------------+  |
|  |        Main Process (main.js)      |  |
|  |  - BrowserWindow management       |  |
|  |  - App lifecycle                  |  |
|  |  - IPC handler (preload.js)       |  |
|  +----------------+-------------------+  |
|                   | IPC               |  |
|  +----------------v-------------------+  |
|  |     Renderer Process (Chromium)    |  |
|  |  +------------------------------+  |  |
|  |  |        index.html            |  |  |
|  |  |  +------------------------+  |  |  |
|  |  |  |    calculator.js       |  |  |  |
|  |  |  |  - State management    |  |  |  |
|  |  |  |  - Expression parsing  |  |  |  |
|  |  |  |  - Display rendering   |  |  |  |
|  |  |  |  - Keyboard handling   |  |  |  |
|  |  |  +------------------------+  |  |  |
|  |  +------------------------------+  |  |
|  +------------------------------------+  |
+------------------------------------------+
```

---

## 2. Komponen Utama

### 2.1 Main Process (`main.js`)

**Tanggung jawab:**
- Membuat dan mengelola BrowserWindow
- Menangani siklus hidup aplikasi (ready, activate, window-all-closed)
- Menyediakan preload script untuk IPC yang aman

**Konfigurasi BrowserWindow:**
```javascript
{
  width: 430, height: 760,
  minWidth: 380, minHeight: 650,
  autoHideMenuBar: true,
  webPreferences: {
    contextIsolation: true,    // keamanan: aktif
    nodeIntegration: false,    // keamanan: tidak aktif
    preload: path.join(__dirname, 'src/preload.js')
  }
}
```

### 2.2 Renderer Process (`index.html` + `src/calculator.js`)

**Tanggung jawab:**
- Menampilkan antarmuka kalkulator
- Menangani input pengguna (tombol + keyboard)
- Memparse dan mengevaluasi ekspresi matematika
- Merender hasil ke display

**State Utama:**
| Variabel | Tipe | Deskripsi |
|----------|------|-----------|
| formula | string | Ekspresi matematika yang sedang diinput |
| cursorPos | number | Posisi kursor dalam string formula |
| isDeg | boolean | Mode sudut: true=DEG, false=RAD |
| isDMSOutput | boolean | Format output: true=DMS, false=DD |
| lastAns | number | Hasil kalkulasi terakhir (untuk ANS) |
| lastRawResult | number | Nilai numerik terakhir |
| evaluated | boolean | Apakah = baru saja ditekan |

### 2.3 Expression Parser

**Alur Parsing:**
```
Input Formula (string)
      |
      v
[parseFormula()]
  1. Normalisasi simbol (°, ×, ÷, π)
  2. Konversi double minus (--)
  3. Auto-balance kurung
  4. Normalisasi fungsi invers (sin-1 → asin)
  5. Konversi DMS ke Desimal
  6. Substitusi ANS
  7. Konversi operator (^ → **)
  8. Tambah perkalian implisit
  9. Tambah kurung fungsi otomatis
  10. Map fungsi ke math.js API (target v1.1.0)
      |
      v
[math.evaluate()] / [eval()] — (saat ini)
      |
      v
Nilai Numerik (number)
      |
      v
[renderResultDisplay()]
  - Format DD atau DMS
  - Tampilkan di resultDisplay
```

---

## 3. Alur Data

### Alur Input Tombol:
```
User klik tombol
    |
    v
onclick="insertAtCursor('sin ')"
    |
    v
insertAtCursor(text)
    |-- Update formula string
    |-- Update cursorPos
    |-- updateDisplay()      --> Render formula di Baris 1
    +-- liveEvaluate()       --> Preview hasil di Baris 2
```

### Alur Keyboard:
```
document.keydown event
    |
    v
Switch key:
  's' → insertAtCursor('sin ')
  'S' → insertAtCursor('asin ')
  'Enter' / '=' → calculate()
  'Backspace' → backspace()
  'ArrowLeft' → moveCursorLeft()
  ... dst.
```

### Alur Kalkulasi Final (tombol =):
```
calculate()
    |
    v
parseFormula(formula)
    |
    v
math.evaluate(parsed)  [target: v1.1.0]
    |
    v
isFinite && !isNaN?
  YES → lastAns = res
        lastRawResult = res
        renderResultDisplay(res)
        evaluated = true
        status = "RESULT"
  NO  → tampilkan pesan error yang sesuai
```

---

## 4. Keamanan

### Prinsip Utama:
- **contextIsolation: true** — renderer tidak bisa langsung akses Node.js API
- **nodeIntegration: false** — `require()` tidak tersedia di renderer
- **preload.js** — satu-satunya jembatan aman antara main dan renderer via IPC
- **Tidak ada eval()** (target v1.1.0) — ekspresi dievaluasi via math.js

### Batas Kepercayaan:
```
[Trusted: Main Process]   [Sandboxed: Renderer]
       main.js          |      index.html
      preload.js        |     calculator.js
  (Node.js penuh)       | (Web APIs + contextBridge)
```

---

## 5. Build & Distribusi

### Build Pipeline:
```
npm run dist
    |
    v
[npm run build:css]          <- Compile Tailwind (target v1.1.0)
    |
    v
[electron-builder --win nsis]
    |
    v
Package files:
  - index.html
  - main.js
  - src/calculator.js
  - src/preload.js
  - src/output.css
  - assets/ (logo, icon)
  - vendor/ (math.js)
  + Electron Chromium runtime (~100MB)
    |
    v
dist/Kalkulator Falak Setup 1.x.x.exe  (NSIS Installer)
```

---

## 6. Keputusan Arsitektur (ADR)

### ADR-001: Electron sebagai Platform Desktop
**Keputusan:** Menggunakan Electron
**Alasan:** Tim familiar dengan HTML/JS, kode HTML sudah ada, time-to-market cepat
**Trade-off:** Ukuran installer besar (~100MB), konsumsi RAM lebih tinggi dari native app

### ADR-002: Ganti eval() dengan math.js (Target v1.1.0)
**Keputusan:** Menggunakan math.js sebagai expression parser
**Alasan:** eval() adalah risiko keamanan meski dalam konteks terbatas
**Trade-off:** Perlu refactor parseFormula(), tambah ~500KB dependency

### ADR-003: Bundle Tailwind Secara Lokal (Target v1.1.0)
**Keputusan:** Build Tailwind CSS secara lokal saat development
**Alasan:** Aplikasi desktop harus offline-capable penuh
**Trade-off:** Tambah langkah build di workflow development
"""

# ============================================================
# SECURITY.md
# ============================================================
SECURITY = r"""# SECURITY.md — Kebijakan Keamanan
## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember

---

## Kebijakan Keamanan

### Versi yang Didukung

| Versi | Didukung |
|-------|----------|
| 1.1.x | Ya (setelah rilis) |
| 1.0.x | Terbatas (patch kritis saja) |
| < 1.0 | Tidak |

---

## Melaporkan Kerentanan

Jika Anda menemukan kerentanan keamanan dalam aplikasi ini, mohon **jangan** buat
GitHub Issue yang bersifat publik. Laporkan secara langsung kepada tim melalui:

**Email:** [email lembaga falakiyah]

Kami akan merespons dalam **5 hari kerja** dan memberikan pembaruan dalam **30 hari**.

---

## Konfigurasi Keamanan Electron

Aplikasi ini menggunakan konfigurasi keamanan Electron berikut:

```javascript
webPreferences: {
  contextIsolation: true,     // WAJIB: isolasi konteks aktif
  nodeIntegration: false,     // WAJIB: Node.js tidak tersedia di renderer
  preload: './src/preload.js' // Jembatan aman via contextBridge
}
```

---

## Masalah Keamanan yang Diketahui

### [AKTIF] Penggunaan eval() — Prioritas Tinggi
- **Status:** Akan diperbaiki di v1.0.2 (Milestone 1)
- **Dampak:** Rendah dalam konteks offline desktop, namun tetap merupakan anti-pattern
- **Mitigasi sementara:** Aplikasi berjalan offline dan tidak menerima input dari jaringan
- **Perbaikan:** Ganti dengan math.js (lihat DEVPLAN.md — M1)

---

## Praktik Keamanan yang Diterapkan

- Tidak ada akses jaringan dari renderer process
- Tidak ada penyimpanan data sensitif
- Tidak ada autentikasi atau data pengguna
- Build produksi menonaktifkan DevTools
- `contextIsolation` dan `nodeIntegration` dikonfigurasi dengan benar
"""

# ============================================================
# README.md (baru — menggantikan README.txt)
# ============================================================
README = r"""# Kalkulator Falak
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

## Lisensi

MIT License — Copyright (c) 2026 Lembaga Falakiyah NU Wuluhan Jember

---

## Kontak

**Lembaga Falakiyah Nahdlatul Ulama**
Wuluhan, Jember, Jawa Timur
"""

# Write all files
files = {
    os.path.join(DOCS, "PRD.md"): PRD,
    os.path.join(DOCS, "DEVPLAN.md"): DEVPLAN,
    os.path.join(DOCS, "DEVLOG.md"): DEVLOG,
    os.path.join(DOCS, "ARCHITECTURE.md"): ARCHITECTURE,
    os.path.join(BASE, "CHANGELOG.md"): CHANGELOG,
    os.path.join(BASE, "SECURITY.md"): SECURITY,
    os.path.join(BASE, "README.md"): README,
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"CREATED: {path}")

print("\nSemua dokumen berhasil dibuat!")
