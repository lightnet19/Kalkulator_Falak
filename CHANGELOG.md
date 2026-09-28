# CHANGELOG
## Kalkulator Falak | Dikembangkan oleh Fuad Baidāwī Al-Fajri
> Berdasarkan aplikasi Lembaga Falakiyah MWCNU Wuluhan Jember

Format berdasarkan [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
dan mengikuti [Semantic Versioning](https://semver.org/).

---

## [1.1.1] — 2026-09-28

### Auto-Update Vercel & PWA Cache Fix
- **PWA Service Worker:** Migrasi strategi caching `sw.js` dari *Cache-First* menjadi **Network-First with Dynamic Cache & Offline Fallback** agar browser pengguna di Vercel selalu otomatis mendapatkan pembaruan antarmuka terbaru secara instan saat online.
- **Kompilasi Vercel Cloud:** Memindahkan `tailwindcss` dan `@tailwindcss/cli` ke `dependencies` di `package.json` untuk menjamin proses build Tailwind v4 di Vercel selalu berhasil 100%.
- **Proporsi Header:** Menyelaraskan proporsi logo NU (40px) dan tipografi nama lembaga dengan kontrol mode di [index.html](file:///c:/Projects/Kalkulator_Falak/index.html).

### Ditambahkan & Dioptimasi
- **Redesign Google Stitch (Falakiyah Scientific Light Theme):**
  - Mengganti seluruh palet Dark Mode menjadi **Light Theme ber-kontras tinggi** untuk mengatasi kendala keterbacaan rendah di bawah pencahayaan sinar matahari langsung.
  - Mengimplementasikan token desain instrumen observatorium presisi: bodi putih bersih (*pure white chassis*), layar LCD digital *recessed ice-sage/mint* (`#f4faf6`), angka formula charcoal pekat (`#0f172a`), dan hasil digital hijau zamrud ber-kontras tajam (`#047857`).
  - Menata ulang sistem keycap 3D tactile: angka putih, fungsi slate, operator sky-blue, aksi AC rose-light, DEL amber-light, dan eksekusi `=` emerald green.
  - Memperbarui `src/input.css`, `index.html`, dan `src/calculator.js` agar seluruh transisi tombol, status DEG/RAD, dan unit DD/DMS selaras dengan palet Light Theme.
  - Memperbarui [DESIGN.md](file:///c:/Projects/Kalkulator_Falak/DESIGN.md) ke Versi 2.0.0 mencakup standar kontras WCAG AAA (15.8:1 pada formula, 7.2:1 pada hasil).
- **Responsivitas Mobile:** Penambahan tag viewport eksplisit (`width=device-width, initial-scale=1.0, maximum-scale=5.0`) di [index.html](file:///c:/Projects/Kalkulator_Falak/index.html).
- **Mobile Touch Handling:** Properti `touch-action: manipulation` dan `-webkit-tap-highlight-color: transparent` pada tombol untuk menghilangkan delay 300ms tap di browser smartphone.
- **Dukungan Layar Sempit & Safe Area:** Media query `< 360px` dan safe-area insets (`env(safe-area-inset-*)`) untuk ponsel modern ber-notch dan taskbar.
- **Haptic Feedback:** Integrasi getaran taktil halus (10ms) menggunakan Web Vibration API saat tombol ditekan pada smartphone Android.
- **Code Review & Quality Hardening:**
  - Memperbaiki class invalid Tailwind `py-0.2` menjadi `py-0.5` pada badge satuan hasil di [index.html](file:///c:/Projects/Kalkulator_Falak/index.html).
  - Menghapus class redundant `relative` pada wadah `.screen-3d` di [index.html](file:///c:/Projects/Kalkulator_Falak/index.html).
  - Menyelaraskan teks versi pada komentar footer [index.html](file:///c:/Projects/Kalkulator_Falak/index.html) dan header [src/calculator.js](file:///c:/Projects/Kalkulator_Falak/src/calculator.js) menjadi `v1.1.0`.
  - Mengisolasi safe-area insets menggunakan `@supports` di [src/input.css](file:///c:/Projects/Kalkulator_Falak/src/input.css) agar tidak bertabrakan dengan class padding Tailwind.
  - Memperketat spesifisitas selector `.grid` menjadi `.calc-card-3d .grid` pada media query layar kecil di [src/input.css](file:///c:/Projects/Kalkulator_Falak/src/input.css).
  - Membersihkan array `funcs` di fungsi `backspace()` [src/calculator.js](file:///c:/Projects/Kalkulator_Falak/src/calculator.js) dari duplikat entri tanpa spasi.
  - Menambahkan catatan SSOT (Single Source of Truth) versi pada [src/calculator.js](file:///c:/Projects/Kalkulator_Falak/src/calculator.js), [src/preload.js](file:///c:/Projects/Kalkulator_Falak/src/preload.js), dan [sw.js](file:///c:/Projects/Kalkulator_Falak/sw.js).
  - Memisahkan purpose `any` dan `maskable` serta menambahkan entri ikon resolusi 192x192 pada [manifest.webmanifest](file:///c:/Projects/Kalkulator_Falak/manifest.webmanifest).
  - Memperbarui [SECURITY.md](file:///c:/Projects/Kalkulator_Falak/SECURITY.md) mencakup penyelesaian migrasi `eval()` dan catatan arsitektur deployment Vercel.

### Direncanakan (v1.2.0 - Fase 3)
- Panel Riwayat Kalkulasi (10 perhitungan terakhir)
- Mode Kalkulasi Falak Khusus (Equation of Time, Deklinasi Matahari)

---

## [1.1.0] — 2026-09-12

### Rilis Stabil Versi 1.1.0
- **Keamanan:** Hapus `eval()` dan migrasi ke evaluator aman `math.evaluate()` dari `mathjs`
- **Dual Target & Vercel:** Dukungan rilis ganda (Windows Desktop App & Web App Vercel via `vercel.json`)
- **PWA (Progressive Web App):** Penambahan `manifest.webmanifest` & `sw.js` (Service Worker) agar web app dapat di-install di smartphone (Android/iOS) dan dipakai 100% offline
- **Aset & Hotfix:** Logo NU (`assets/logo-nu.png`) dan Ikon Aplikasi Windows (`assets/icon.ico`)
- **Offline & Arsitektur:** Bundling Tailwind CSS lokal (`src/output.css`), pemisahan `src/calculator.js`, dan `src/preload.js` dengan API fallback otomatis
- **UX & Polish:** Pesan error ramah pengguna, validasi operator ganda, dan atribut aksesibilitas `aria-label`

---

## [1.1.0-beta] — 2026-09-12

### Polish & Aksesibilitas UI
- Menambahkan ikon aplikasi resmi (`assets/icon.ico` dan `assets/icon.png`)
- Menambahkan atribut `aria-label` pada seluruh tombol interaktif di `index.html` untuk mendukung screen reader
- Menyempurnakan pesan error UI (misal: "Domain Error" untuk `asin(2)` dan "∞ Tak Terhingga" untuk pembagian nol)
- Menambahkan validasi pencegahan operator biner ganda beruntun pada input rumus
- Mengenkapsulasi state logika JavaScript ke dalam IIFE module pattern (`KalkulatorFalak`)
- Mengkonfigurasi informasi hak cipta (`copyright`) di `package.json`

---

## [1.1.0-alpha] — 2026-09-12

### Arsitektur & Offline
- Menginstall Tailwind CSS dan CLI secara lokal, menghapus ketergantungan CDN internet
- Memisahkan seluruh logika JavaScript dari `index.html` ke `src/calculator.js`
- Membuat `src/input.css` dan mengkompilasi stylesheet terkompresi `src/output.css`
- Membuat `src/preload.js` untuk Electron IPC dan mengaktifkan isolasi konteks (`contextIsolation: true`)
- Mengupdate `main.js` untuk memuat preload script dan ikon aplikasi
- Mengatur skrip build di `package.json` (`build:css`, `start`, `dist`)

---

## [1.0.2] — 2026-09-12

### Keamanan & Refactor
- Menghapus fungsi `eval()` sepenuhnya dari aplikasi untuk mencegah potensi eksekusi kode berbahaya
- Menggunakan evaluator aman `math.evaluate()` dari library `mathjs`
- Menambahkan dependensi lokal `vendor/math.min.js` untuk memastikan kalkulator tetap bekerja tanpa koneksi internet
- Mengatur scope kalkulasi khusus untuk fungsi trigonometri DEG/RAD dan konversi derajat, menit, detik (DMS)

---

## [1.0.1] — 2026-09-12

### Diperbaiki
- Menambahkan file logo NU (`assets/logo-nu.png`) untuk memperbaiki broken image pada header aplikasi
- Memperbaiki path logo di `index.html` dari `Logo NU.png` ke `assets/logo-nu.png`
- Mendaftarkan folder `assets/` ke dalam konfigurasi `files` di `package.json` sehingga installer memuat logo dengan benar


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

### Kredit
- Dikembangkan oleh: **Fuad Baidāwī Al-Fajri**
- Berdasarkan aplikasi asal dari: **Lembaga Falakiyah MWCNU Wuluhan Jember**

### Ketergantungan
- Electron ^38.1.0
- electron-builder ^26.0.12
- Tailwind CSS (via CDN — akan diganti di v1.1.0)