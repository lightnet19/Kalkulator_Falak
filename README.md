# Kalkulator Falak 2-Baris
### Lembaga Falakiyah Nahdlatul Ulama — Wuluhan Jember

[![Versi](https://img.shields.io/badge/versi-1.1.0-blue)](CHANGELOG.md)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Web%20%7C%20PWA-emerald)](https://github.com/lightnet19/Kalkulator_Falak)
[![Deploy](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)](https://vercel.com)
[![Lisensi](https://img.shields.io/badge/lisensi-MIT-green)](LICENSE)

---

## Tentang Aplikasi

**Kalkulator Falak** adalah aplikasi kalkulator ilmiah 2-baris yang dirancang khusus untuk kebutuhan perhitungan **ilmu falak** (astronomi Islam). 
Aplikasi ini bersifat **Dual-Target**:
1. **Windows Desktop App** (Electron .exe installer) untuk penggunaan desktop offline.
2. **Web App & PWA** (Deployable ke Vercel / Netlify / PWA) yang dapat dipasang di smartphone (Android/iOS) dan dibuka 100% offline.

Aplikasi dikembangkan oleh **Fuad Baiḍāwī Al-Fajri**, berdasarkan karya asli **Lembaga Falakiyah MWCNU Wuluhan Jember**.

---

## Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| **Kalkulator 2-Baris** | Display formula di baris 1 + hasil real-time di baris 2 |
| **Trigonometri Lengkap** | sin, cos, tan, sin⁻¹, cos⁻¹, tan⁻¹ (dengan mode DEG/RAD) |
| **Input & Konversi DMS** | Support Derajat° Menit' Detik" dan konversi otomatis DD ↔ DMS |
| **Fungsi Matematika** | log (log10), ln, √, x², xʸ, π |
| **Evaluasi Aman** | Menggunakan `mathjs` (`math.evaluate()`) tanpa `eval()` |
| **Keamanan & Aksesibilitas** | Full `aria-label` WCAG & isolasi konteks Electron IPC |
| **Support PWA Offline** | Tambahkan ke Home Screen HP (Android/iOS) & jalankan 100% offline |
| **Dual-Target Desktop & Web** | Kompatibel penuh untuk installer Windows (.exe) dan deployment Vercel |

---

## Cara Deploy ke Vercel (Web App)

Aplikasi ini sudah dilengkapi dengan konfigurasi Zero-Config Vercel (`vercel.json`).

### Opsi 1: Via Dashboard Vercel (1-Click Deploy)
1. Buka [Vercel Dashboard](https://vercel.com/new).
2. Import repositori **`lightnet19/Kalkulator_Falak`**.
3. Vercel akan otomatis mendeteksi perintah build `npm run build:css`.
4. Klik **Deploy**!

### Opsi 2: Via Vercel CLI
```bash
npm install -g vercel
vercel
```

---

## Panduan PWA (Instalasi di Smartphone / Tablet)

Saat membuka aplikasi Web di browser smartphone:
1. **Android (Chrome):** Ketuk menu titik tiga (⋮) → **Tambahkan ke Layar Utama (Add to Home Screen)** / **Install App**.
2. **iOS (Safari):** Ketuk tombol Share (↑) → **Add to Home Screen**.
3. Aplikasi akan terpasang di HP dan dapat dibuka kapan saja tanpa koneksi internet.

---

## Cara Menjalankan Secara Lokal (Pengembang)

### Prasyarat
- Node.js (v18+)
- npm

### Langkah-langkah
```bash
# 1. Clone repositori
git clone https://github.com/lightnet19/Kalkulator_Falak.git
cd Kalkulator_Falak

# 2. Install dependensi
npm install

# 3. Jalankan aplikasi desktop (Electron)
npm start

# 4. Kompilasi stylesheet Tailwind CSS
npm run build:css

# 5. Build installer Windows NSIS (.exe)
npm run dist
```

---

## Struktur Direktori

```
Kalkulator_Falak/
├── assets/
│   ├── icon.ico              <- Ikon aplikasi Windows (.ico)
│   ├── icon.png              <- Ikon PWA 512x512 px
│   └── logo-nu.png           <- Logo Nahdlatul Ulama
├── docs/
│   ├── PRD.md
│   ├── DEVPLAN.md
│   ├── DEVLOG.md
│   ├── ARCHITECTURE.md
│   └── SECURITY.md
├── src/
│   ├── calculator.js         <- Engine logika kalkulator (IIFE)
│   ├── preload.js            <- Electron IPC preload script
│   ├── input.css             <- Source Tailwind CSS
│   └── output.css            <- Minified compiled CSS
├── vendor/
│   └── math.min.js           <- Library evaluator matematika offline
├── index.html                <- Main UI
├── main.js                   <- Electron main process
├── manifest.webmanifest      <- PWA Manifest configuration
├── sw.js                     <- PWA Service Worker offline cache
├── vercel.json               <- Vercel deployment configuration
├── tailwind.config.js        <- Tailwind CSS configuration
├── postcss.config.js         <- PostCSS configuration
├── package.json
├── CHANGELOG.md
└── README.md
```

---

## Kredit & Pengembang

- **Dikembangkan Oleh:** **Fuad Baiḍāwī Al-Fajri**
- **Berdasarkan Karya Asal:** **Lembaga Falakiyah MWCNU Wuluhan Jember**
- **Lisensi:** MIT License