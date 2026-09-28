# DEVPLAN — Development Plan
## Kalkulator Falak | Dikembangkan oleh Fuad Baidāwī Al-Fajri
> Berdasarkan aplikasi Lembaga Falakiyah MWCNU Wuluhan Jember

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
├── manifest.webmanifest      <- Konfigurasi PWA Mobile
├── sw.js                     <- Service Worker Offline Cache
├── vercel.json               <- Konfigurasi Deployment Vercel
├── package.json
├── tailwind.config.js
├── postcss.config.js
├── DESIGN.md                 <- Spesifikasi Design System 3D & Mobile UX
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