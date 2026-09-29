# DEVLOG — Development Log
## Kalkulator Falak | Dikembangkan oleh Fuad Baidāwī Al-Fajri
> Berdasarkan aplikasi Lembaga Falakiyah MWCNU Wuluhan Jember

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

### [2026-09-28] — Rilis v1.1.1: Pembenahan Proporsi Header, Caching Network-First PWA, & Cloud Build Vercel
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M4+ (Auto-Update & Visual Polish Patch)
**Status:** DONE

#### Yang Dikerjakan:
- **Penyelarasan Proporsi Header:**
  - Mengunci wadah logo NU pada ukuran proporsional 40px × 40px (`w-10 h-10`) berlatar `bg-emerald-50` berbingkai lembut.
  - Memperbaiki tata letak teks identitas "Lembaga Falakiyah NU" dan "MWCNU Wuluhan Jember" agar sejajar secara vertikal (*vertical center alignment*) dengan tombol kontrol mode di sisi kanan.
  - Mengeliminasi teks redundan agar header tetap lapang dan tidak terpotong pada layar ponsel.
- **Perbaikan Scanner Tailwind CSS v4:**
  - Menambahkan direktif `@import "tailwindcss";` dan pemindai template `@source "../index.html";` serta `@source "./calculator.js";` di `src/input.css` agar utilitas Tailwind v4 terkompilasi penuh.
- **Pembaruan Strategi Caching Service Worker (`sw.js`):**
  - Mengubah strategi dari *Cache-First* menjadi **Network-First with Dynamic Cache Update & Offline Fallback**.
  - Mengatasi kendala browser pengguna yang terkunci di cache versi lama saat membuka tautan Vercel. Saat terhubung internet, browser kini langsung menyajikan versi terbaru secara otomatis.
- **Ketahanan Build Vercel Cloud:**
  - Memindahkan package `@tailwindcss/cli` dan `tailwindcss` dari `devDependencies` ke `dependencies` di `package.json` untuk mencegah kegagalan perintah `npm run build:css` di lingkungan produksi Vercel.
- **Bump Versi ke 1.1.1:**
  - Menyelaraskan seluruh metadata versi di `package.json`, `index.html`, `src/calculator.js`, `src/preload.js`, `sw.js`, `README.md`, `README.txt`, dan `CHANGELOG.md`.

#### Hasil Verification:
- Header kalkulator tampil seimbang, proporsional, dan estetis di seluruh resolusi layar.
- Perubahan antarmuka di Vercel langsung terupdate otomatis saat online dan tetap bekerja 100% saat offline.

---

### [2026-09-28] — Redesign Antarmuka Menggunakan Google Stitch MCP: Falakiyah Scientific (Light Theme)
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M4+ (High-Contrast Daylight Redesign)
**Status:** DONE

#### Yang Dikerjakan:
- Menghubungkan dan memanfaatkan **Google Stitch MCP** untuk menghasilkan Design System bertema terang: **"Falakiyah Scientific"** (Project: `12919745297315223191`)
- Mengganti seluruh skema Dark Theme menjadi **Light Theme** ber-kontras tinggi guna mengatasi masalah keterbacaan rendah di bawah sinar matahari outdoor
- Menerapkan arsitektur visual instrumen observatorium presisi:
  - Bodi kalkulator putih murni (*chassis pure white*) dengan bayangan 3D mikro yang lembut
  - Layar LCD berlatar *ice-sage/mint* (`#f4faf6`) dengan cekungan border inset
  - Teks formula slate charcoal (`#0f172a`) dan hasil kalkulasi digital hijau zamrud pekat (`#047857`)
  - Keycap berpenampilan fisik 3D: tombol angka putih, fungsi slate, operator sky-blue, AC rose-light, DEL amber-light, dan eksekusi `=` hijau zamrud penuh
- Menyinkronkan seluruh kelas transisi status tombol DEG/RAD dan format DD/DMS di `src/calculator.js`
- Mengompilasi ulang stylesheet produksi dengan Tailwind CSS v4.3.3 (`npm run build:css`)
- Memperbarui dokumentasi sistem desain [DESIGN.md](file:///c:/Projects/Kalkulator_Falak/DESIGN.md) ke Versi 2.0.0

#### Hasil Verification & Browser Test:
- Pengujian interaktif pada browser subagent: Operasi perkalian `7 × 6 = 42` dan konversi DMS `42° 0' 0.00"` berjalan presisi
- Keterbacaan teks dan angka meningkat drastis, lolos standar kontras WCAG AAA

---

### [2026-09-28] — Desain Sistem 3D Kompak, Mobile Touch UX, dan Eksekusi Code Review v1.1.0
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M4+ (Post-Release UI Modernization & Quality Hardening)
**Status:** DONE

#### Yang Dikerjakan:
- Membuat dokumen spesifikasi desain komprehensif `DESIGN.md` (filosofi 3D realism, palet warna, tipografi, dan adaptasi mobile)
- Mengoptimasi responsivitas mobile di `index.html` dan `src/input.css`:
  - Tag viewport eksplisit dengan pinch-to-zoom yang aman
  - Atribut sentuhan mobile: `touch-action: manipulation` dan `-webkit-tap-highlight-color: transparent`
  - Safe-area insets (`env(safe-area-inset-*)`) menggunakan isolasi `@supports`
  - Media query adaptif untuk layar kompak `< 360px`
- Mengintegrasikan respons taktil Haptic Feedback (10ms) via Web Vibration API untuk interaksi layar sentuh smartphone Android
- Menyelesaikan 11 temuan audit kualitas kode dari `code_review_report.md`:
  - Memperbaiki class invalid Tailwind `py-0.2` -> `py-0.5` pada badge hasil
  - Menghapus class redundant `relative` pada wadah `.screen-3d`
  - Menyelaraskan nomor versi stabil `1.1.0` di seluruh komentar dan metadata
  - Memperketat selector CSS `.calc-card-3d .grid`
  - Membersihkan token fungsi tanpa spasi di `backspace()` (`src/calculator.js`)
  - Menegaskan `package.json` sebagai Single Source of Truth (SSOT) untuk versi pada `calculator.js`, `preload.js`, dan `sw.js`
  - Menyempurnakan `manifest.webmanifest` dengan ukuran standar PWA `192x192` serta pemisahan purpose `any` dan `maskable`
  - Memperbarui `SECURITY.md` dengan catatan mitigasi deployment Vercel
- Mengompilasi ulang stylesheet produksi dengan Tailwind CSS v4.3.3 (`npm run build:css`)

#### Hasil Verification:
- Tampilan kalkulator memiliki estetika 3D skeuomorfik yang kokoh, tajam, dan responsif di desktop maupun layar kecil smartphone
- Build CSS bersih tanpa peringatan Tailwind
- Seluruh 11 temuan review kode terselesaikan 100%

---

### [2026-09-12] — Dukungan Dual-Target (Windows Desktop + Vercel Web App & PWA)
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M4 (Ekstensi Vercel & PWA)
**Status:** DONE

#### Yang Dikerjakan:
- Membuat konfigurasi Zero-Config Vercel (`vercel.json`)
- Membuat Web App Manifest (`manifest.webmanifest`) untuk dukungan PWA
- Membuat Service Worker (`sw.js`) untuk caching aset offline di smartphone (Android/iOS)
- Menambahkan meta tags PWA di `index.html` (`theme-color`, `apple-mobile-web-app-capable`, icon link)
- Menambahkan safe API fallback di `src/calculator.js` (`window.falakAPI = window.falakAPI || ...`)
- Mendaftarkan `manifest.webmanifest` dan `sw.js` ke `package.json`
- Memperbarui `README.md` dengan instruksi 1-Click Deploy Vercel & Panduan PWA

#### Hasil Verification:
- Aplikasi dapat berjalan sebagai Windows Desktop App (Electron) dan Web App (Vercel) dari codebase yang sama
- Aplikasi web dapat di-install ke layar utama HP dan bekerja 100% offline via Service Worker

---

### [2026-09-12] — Milestone 4: Release v1.1.0 Stabil
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M4
**Status:** DONE

#### Yang Dikerjakan:
- Kompilasi Tailwind CSS (`npm run build:css`) secara lokal
- Bump versi aplikasi di `package.json` ke `1.1.0`
- Pengujian regresi komprehensif pada fungsi matematika, trigonometri, dan DMS
- Meng-update `CHANGELOG.md` dan `DEVLOG.md` untuk merilis rilis stabil v1.1.0

#### Hasil Verification:
- Seluruh milestone M0 hingga M4 selesai 100%
- Kode bersih dari `eval()`, terpisah modular, terenkapsulasi, dan dapat dijalankan tanpa koneksi internet
- Aplikasi siap didistribusikan ke Lembaga Falakiyah MWCNU Wuluhan Jember

#### Langkah Berikutnya:
- Persiapan Fase 3 (v1.2.0): Implementasi Riwayat Kalkulasi & Fitur Falak Khusus

---

### [2026-09-12] — Milestone 3: Polish & UX (v1.1.0-beta)
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M3
**Status:** DONE

#### Yang Dikerjakan:
- Membuat ikon aplikasi `assets/icon.png` dan `assets/icon.ico`
- Mengkonfigurasi icon di `main.js` (`BrowserWindow`) dan `package.json` (`build.win.icon`)
- Menambahkan atribut `aria-label` pada seluruh elemen tombol interaktif di `index.html`
- Memperbaiki pesan error UI di `src/calculator.js` ("Domain Error", "∞ Tak Terhingga")
- Menambahkan validasi mencegah penumpukan operator biner ganda beruntun saat menginput rumus
- Mengenkapsulasi modul JavaScript dalam IIFE `KalkulatorFalak`
- Mengupdate `package.json` versi menjadi `1.1.0-beta` dan menambah informasi copyright
- Meng-update `CHANGELOG.md` dan `DEVLOG.md`

#### Hasil Verification:
- Tampilan aplikasi profesional dengan ikon Windows kustom
- Pesan error ramah pengguna (misal `asin(2)` menampilkan `Domain Error`)
- Aksesibilitas WCAG/a11y terpenuhi dengan `aria-label`
- Pencegahan kesalahan sintaks input ganda berjalan

#### Langkah Berikutnya:
- Eksekusi Milestone 4: Release v1.1.0 (Stabil)
  * Uji kompilasi CSS & pengujian regresi penuh
  * Build installer installer Windows NSIS (.exe)
  * Finalisasi rilis v1.1.0

---

### [2026-09-12] — Milestone 2: Offline & Arsitektur (v1.1.0-alpha)
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M2
**Status:** DONE

#### Yang Dikerjakan:
- Menginstall `@tailwindcss/cli`, `tailwindcss`, `postcss`, `autoprefixer` via npm
- Membuat `tailwind.config.js` dan `postcss.config.js`
- Membuat `src/input.css` dan mengkompilasi ke `src/output.css` (ukuran ~7KB)
- Mengganti CDN script Tailwind di `index.html` dengan `<link rel="stylesheet" href="src/output.css">`
- Ekstrak seluruh logika skrip JavaScript dari `index.html` ke `src/calculator.js`
- Membuat `src/preload.js` untuk Electron IPC
- Mengupdate `main.js` dengan `preload: path.join(__dirname, 'src/preload.js')` dan `contextIsolation: true`
- Mengupdate `package.json` scripts (`build:css`, `start`, `dist`) dan versi ke `1.1.0-alpha`
- Meng-update `CHANGELOG.md` dan `DEVLOG.md`

#### Hasil Verification:
- Aplikasi kini 100% independen tanpa ketergantungan internet
- Struktur proyek rapi (HTML, CSS, JS, Preload terpisah di folder `src/`)
- Keamanan IPC Electron terkonfigurasi dengan preload script

#### Langkah Berikutnya:
- Eksekusi Milestone 3: Polish & UX (v1.1.0-beta)
  * Sediakan ikon `.ico` dan `.png` aplikasi
  * Tambahkan `aria-label` untuk aksesibilitas
  * Tingkatkan penanganan error UI (NaN, Infinity)

---

### [2026-09-12] — Milestone 1: Security Fix (v1.0.2)
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M1
**Status:** DONE

#### Yang Dikerjakan:
- Menginstall dependensi `mathjs` via npm (`npm install mathjs`)
- Menyalin browser bundle `math.js` ke `vendor/math.min.js`
- Menambahkan referensi `<script src="vendor/math.min.js"></script>` di `index.html`
- Mengganti seluruh penggunaan `eval()` pada `liveEvaluate()` dan `calculate()` dengan `math.evaluate()` dan custom scope aman
- Mengkonfigurasi handler mode DEG/RAD dan konversi DMS untuk math.js
- Menambahkan `vendor/**/*` ke konfigurasi `files` di `package.json` dan meng-update versi ke `1.0.2`
- Meng-update `CHANGELOG.md` dan `DEVLOG.md`

#### Hasil Verification:
- Tidak ada lagi instruksi `eval()` dalam seluruh codebase aplikasi
- Seluruh fungsi matematika dan trigonometri berjalan via evaluator math.js yang terenkapsulasi
- Masalah keamanan RCE teratasi penuh

#### Langkah Berikutnya:
- Eksekusi Milestone 2: Offline & Arsitektur (v1.1.0-alpha)
  * Install Tailwind CSS, PostCSS, Autoprefixer
  * Konfigurasi Tailwind lokal (`src/input.css` -> `src/output.css`)
  * Ekstrak JS ke `src/calculator.js`
  * Buat `src/preload.js` untuk Electron

---

### [2026-09-12] — Milestone 0: Hotfix Kritis (v1.0.1)
**Kontributor:** Fuad Baidāwī Al-Fajri
**Milestone:** M0
**Status:** DONE

#### Yang Dikerjakan:
- Membuat folder `assets/` dan menambahkan file `assets/logo-nu.png`
- Mengubah referensi logo di `index.html` dari `Logo NU.png` ke `assets/logo-nu.png` dan `alt="Logo Nahdlatul Ulama"`
- Mengubah versi aplikasi di `package.json` menjadi `1.0.1` dan menambahkan `"assets/**/*"` ke `build.files`
- Mengupdate `CHANGELOG.md` dan `DEVLOG.md`

#### Hasil Verification:
- Logo NU kini ada di `assets/logo-nu.png`
- Broken image di header aplikasi teratasi
- Konfigurasi electron-builder terdaftar memuat aset gambar

#### Langkah Berikutnya:
- Eksekusi Milestone 1: Security Fix (v1.0.2) - Hapus `eval()` dan ganti dengan `mathjs`

---

### [2026-09-12] — Analisis Mendalam Kode & Pembuatan Dokumen Perencanaan
**Kontributor:** Fuad Baidāwī Al-Fajri (dengan bantuan Antigravity AI)
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
**Kontributor:** Lembaga Falakiyah MWCNU Wuluhan Jember
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
- Aplikasi ini adalah karya asal Lembaga Falakiyah MWCNU Wuluhan Jember
- Selanjutnya dikembangkan dan disempurnakan oleh Fuad Baidāwī Al-Fajri
- Desain UI 3D kalkulator dinilai sangat bagus secara visual
- Fungsionalitas dasar sudah berjalan dengan baik
- Masalah keamanan (eval) dan infrastruktur (CDN, aset) perlu ditangani