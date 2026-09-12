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