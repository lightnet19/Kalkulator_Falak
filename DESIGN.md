# DESIGN.md — Sistem Desain Kalkulator Falak

> **Kalkulator Falak** — Lembaga Falakiyah NU Wuluhan Jember  
> Dikembangkan oleh: Fuad Baidāwī Al-Fajri  
> Versi Dokumen: 1.0.0 | Diperbarui: September 2026

---

## Daftar Isi

1. [Filosofi Desain](#1-filosofi-desain)
2. [Palet Warna](#2-palet-warna)
3. [Tipografi](#3-tipografi)
4. [Sistem Tombol 3D](#4-sistem-tombol-3d)
5. [Komponen UI](#5-komponen-ui)
6. [Layout & Grid](#6-layout--grid)
7. [Responsivitas Mobile](#7-responsivitas-mobile)
8. [Aksesibilitas](#8-aksesibilitas)
9. [Animasi & Transisi](#9-animasi--transisi)
10. [Panduan Pengembangan](#10-panduan-pengembangan)

---

## 1. Filosofi Desain

Kalkulator Falak menggunakan pendekatan **3D Skeuomorphic Dark-Mode** — meniru tampilan kalkulator saintifik fisik dengan nuansa premium dan elegan.

### Prinsip Inti

| Prinsip | Penerapan |
|---|---|
| **Skeuomorphic** | Tombol memiliki kedalaman 3D nyata via `box-shadow` berlapis |
| **Dark Mode First** | Latar belakang gelap (`#0f172a`) melindungi mata saat digunakan lama |
| **Hierarki Visual** | Warna tombol membedakan fungsi: merah (AC), kuning (DEL), hijau (=) |
| **Mobile-First** | Ukuran tombol dan font dioptimalkan untuk sentuh layar kecil |
| **Presisi** | Tampilan dua baris (formula + hasil) menghindari ambiguitas kalkulasi |

### Identitas Visual

- **Tema Warna Utama:** Hijau Emerald (`#059669`) — identitas Nahdlatul Ulama
- **Aksen Sekunder:** Biru Sky (`#38bdf8`) — fungsi saintifik / navigasi
- **Aksen Tersier:** Amber (`#f59e0b`) — peringatan / DEL / DMS format

---

## 2. Palet Warna

### 2.1 Warna Latar & Struktur

```
Latar Body (Gradient):
  radial-gradient(circle at center, #cbd5e1 → #94a3b8)
  [Slate-300 → Slate-400]

Bodi Kalkulator (Gradient):
  linear-gradient(165deg, #1e293b → #0f172a → #020617)
  [Slate-800 → Slate-900 → Gray-950]

Layar Display:
  #030712 (Gray-950 ultra-gelap)

Border Utama:
  #334155 (Slate-700) — sisi kiri/atas
  #020617 (Gray-950) — sisi bawah (efek ketebalan 3D)
```

### 2.2 Token Warna Tombol

| Kelompok | Background | Teks | Border | Shadow |
|---|---|---|---|---|
| **Fungsi** `.btn-func` | `#334155 → #1e293b` | `#38bdf8` sky-400 | `#475569` | `#0f172a` |
| **Angka** `.btn-num` | `#1e293b → #0f172a` | `#f8fafc` white | `#334155` | `#020617` |
| **Operator** `.btn-op` | `#0369a1 → #075985` | `#ffffff` | `#0284c7` | `#0c4a6e` |
| **Sama Dengan** `.btn-equals` | `#10b981 → #059669` | `#ffffff` | `#34d399` | `#065f46` |
| **AC (Clear)** `.btn-action` | `#ef4444 → #dc2626` | `#ffffff` | `#f87171` | `#991b1b` |
| **DEL** `.btn-del` | `#f59e0b → #d97706` | `#ffffff` | `#fbbf24` | `#92400e` |
| **Navigasi** `.btn-nav` | `#0284c7 → #0369a1` | `#e0f2fe` | `#38bdf8` | `#075985` |
| **DMS** `.btn-dms` | `#0284c7 → #075985` | `#f0f9ff` | `#38bdf8` | `#0c4a6e` |

### 2.3 Warna Teks & Status

```
Teks Utama:         #f8fafc  (Slate-50)
Teks Sekunder:      #cbd5e1  (Slate-300)
Teks Redup:         #64748b  (Slate-500)
Teks Emerald:       #34d399  (Emerald-400) — hasil kalkulator
Teks Sky:           #38bdf8  (Sky-400) — fungsi trig
Teks Amber:         #fbbf24  (Amber-400) — DMS / peringatan
Teks Header NU:     #6ee7b7  (Emerald-300) — nama lembaga
```

### 2.4 Warna Indikator Status

| Status | Label | Warna |
|---|---|---|
| Siap | `READY` | `#64748b` Slate-500 |
| Preview | `PREVIEW` | `#38bdf8` Sky-400 |
| Hasil | `RESULT` | `#34d399` Emerald-400 |
| Error | `ERROR` | `#f87171` Red-400 |

---

## 3. Tipografi

### 3.1 Font Stack

```css
/* Font Tubuh & UI Umum */
font-family: system-ui, -apple-system, sans-serif;

/* Font Display Formula & Hasil (.formula-font, .result-font) */
font-family: Arial, Helvetica, sans-serif;
```

> **Alasan:** Arial memberikan keterbacaan maksimal untuk angka dan simbol matematika di semua platform, termasuk Android dan iOS, tanpa perlu memuat font eksternal.

### 3.2 Skala Ukuran Font

| Elemen | Mobile (< 640px) | Desktop (>= 640px) | Class Tailwind |
|---|---|---|---|
| Nama Lembaga | `12px` | `14px` | `text-xs sm:text-sm` |
| Sub-judul | `10px` | `11px` | `text-[10px] sm:text-[11px]` |
| Formula (baris 1) | `16px` | `18px` | `text-base sm:text-lg` |
| Hasil (baris 2) | `24px` | `30px` | `text-2xl sm:text-3xl` |
| Label tombol | `12px` | `12px` | `text-xs` |
| Shortkey info | `10px` | `10px` | `text-[10px]` |
| Badge status | `8px` | `8px` | `text-[8px]` |
| Badge format | `9px` | `9px` | `text-[9px]` |

### 3.3 Bobot Font

```
font-bold   → Label tombol, judul, badge aktif
font-medium → Sub-judul, teks navigasi
font-normal → Display formula, teks bantu
```

---

## 4. Sistem Tombol 3D

### 4.1 Anatomi Tombol

Setiap tombol memiliki 4 lapisan visual yang menciptakan ilusi kedalaman 3D:

```
+---------------------------------------------+  <- border-top terang = refleksi cahaya
|  ░░░░░░ Label Tombol ░░░░░░░░░░░░░░░░░░░░  |  <- background gradient (atas lebih terang)
|                                             |
+---------------------------------------------+
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  <- box-shadow bawah (gelap) = ketebalan
```

```css
/* Template Umum Tombol 3D */
.btn-3d {
  position: relative;
  transition: all 0.05s ease-in-out;
  user-select: none;
}

/* Efek Tekan */
.btn-3d:active {
  transform: translateY(2px);
  box-shadow: 0 0.5px 0 currentColor,
              inset 0 1.5px 3px rgba(0,0,0,0.4);
}
```

### 4.2 Varian Tombol & Penggunaan

| Varian | Fungsi & Posisi |
|---|---|
| `btn-func` | sin, cos, tan, asin, acos, atan, log, ln, sqrt, xy, x2, ANS, (, ) |
| `btn-num` | 0–9, titik desimal (.) |
| `btn-op` | ÷, ×, −, + |
| `btn-equals` | = (Hitung), span 2 kolom |
| `btn-action` | AC (Bersihkan Semua) |
| `btn-del` | DEL (Hapus Karakter) |
| `btn-nav` | Kiri, Kanan (Navigasi Kursor) |
| `btn-dms` | ° ' " / DMS-Conv |

### 4.3 Ukuran & Padding Tombol

```css
/* Padding tombol grid */
py-2   → atas bawah 8px (0.5rem)

/* Padding tombol kecil (badge header) */
px-2 py-0.5  → kiri-kanan 8px, atas-bawah 2px

/* Padding navigasi kursor */
px-3 py-0.5  → kiri-kanan 12px, atas-bawah 2px
```

> **Mobile Touch Target:** Tombol grid `py-2` + `text-xs` menghasilkan tinggi efektif ~36–40px, mendekati standar minimum 44px Android/iOS.

---

## 5. Komponen UI

### 5.1 Bodi Kalkulator `.calc-card-3d`

```
+------------------------------------------+  <- border-top terang (highlight)
|  HEADER: Logo + Nama | Judul + Badge     |
|------------------------------------------|
|  LAYAR 2-BARIS (screen-3d)               |
|  +--------------------------------------+ |
|  | Baris 1: Formula / Rumus            | |
|  |                                      | |
|  |                  Baris 2: Hasil     | |
|  +--------------------------------------+ |
|------------------------------------------|
|  NAVIGASI KURSOR: Kiri | Kanan           |
|------------------------------------------|
|  GRID TOMBOL 5 x 7                       |
|  Row 1: AC  DEL  (   )   div             |
|  Row 2: sin cos tan xy   mul             |
|  Row 3: sin-1 cos-1 tan-1 sqrt minus     |
|  Row 4: log  7   8   9   plus            |
|  Row 5: ln   4   5   6   x2             |
|  Row 6: dms  1   2   3   ANS            |
|  Row 7: pi   0   .   [= span 2 kolom]  |
|------------------------------------------|
|  FOOTER: Tips & Shortkey Info            |
+------------------------------------------+  <- border-bottom tebal (kedalaman)
```

**Properti Kunci:**
```css
max-width: 28rem (448px)   /* max-w-md */
border-radius: 1rem         /* rounded-2xl */
padding: 1rem               /* p-4 */
gap antar seksi: 10px       /* space-y-2.5 */
```

### 5.2 Layar Display `.screen-3d`

```css
/* Layar cekung (inset shadow) meniru LCD fisik */
height: 7rem (112px)   /* h-28 */
padding: 8px 12px       /* py-2 px-3 */
border-radius: 0.75rem  /* rounded-xl */

/* Shadow inset untuk efek cekungan */
box-shadow:
  inset 0 6px 12px rgba(0,0,0,0.85),
  inset 0 1px 3px rgba(0,0,0,0.7),
  0 1px 0 rgba(255,255,255,0.05);
```

**Layout Dua Baris:**
- **Baris 1** (atas): Formula/rumus — font `text-base sm:text-lg`, scroll horizontal
- **Baris 2** (bawah): Hasil numerik — font `text-2xl sm:text-3xl`, rata kanan

### 5.3 Badge & Indikator

```
[DEG]       → bg-emerald-950, text-emerald-400 (aktif) | bg-sky-950, text-sky-400 (RAD)
[FORMAT:DD] → bg-amber-950, text-amber-400
[DD]        → bg-slate-800, text-sky-300 (DD) | bg-amber-950, text-amber-300 (DMS)
[READY]     → text-slate-500, font-size 9px, uppercase
```

### 5.4 Kursor Animasi `.custom-caret`

```css
width: 2.5px
height: 1.25rem
background: #34d399 (emerald-400)
box-shadow: 0 0 8px #34d399   /* Efek glow */
animation: caret-blink 0.8s infinite

@keyframes caret-blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.15; }
}
```

---

## 6. Layout & Grid

### 6.1 Layout Halaman

```
body
└── flex items-center justify-center  (Tengah vertikal & horizontal)
    └── .calc-card-3d  max-w-md w-full
        padding: p-2 sm:p-4  (Mobile: 8px | Desktop: 16px)
```

### 6.2 Grid Tombol — 5 Kolom

```css
display: grid;
grid-template-columns: repeat(5, 1fr);
gap: 6px;       /* gap-1.5 */
font-size: 12px; /* text-xs */
```

**Pengecualian kolom:**
- Tombol `=` menggunakan `col-span-2` (mengisi 2 kolom terakhir di Row 7)

### 6.3 Header Layout

```
flex items-center justify-between
├── Kiri: flex gap-2 (Logo + Nama Lembaga 2 baris)
└── Kanan: flex-col items-end (Judul + flex badge row)
```

### 6.4 Bar Navigasi Kursor

```
flex items-center justify-between
├── Label: "Navigasi Kursor:"
└── flex gap-1.5 (Tombol Kiri | Kanan)
```

---

## 7. Responsivitas Mobile

### 7.1 Breakpoint yang Digunakan

Proyek ini menggunakan **Tailwind CSS v4** dengan breakpoint default:

| Breakpoint | Lebar | Kelas |
|---|---|---|
| *(default)* | `< 640px` | (tanpa prefix) |
| `sm` | `>= 640px` | `sm:` |

> Kalkulator dirancang untuk tampil optimal di **satu breakpoint utama** (`sm`) karena lebar maksimum `max-w-md` (448px) sudah responsif di semua layar.

### 7.2 Penyesuaian Antar Breakpoint

| Elemen | Mobile < 640px | Desktop >= 640px |
|---|---|---|
| Logo | `w-11 h-11` (44px) | `w-12 h-12` (48px) |
| Nama Lembaga | `text-xs` (12px) | `text-sm` (14px) |
| Formula | `text-base` (16px) | `text-lg` (18px) |
| Hasil | `text-2xl` (24px) | `text-3xl` (30px) |
| Padding Body | `p-2` (8px) | `p-4` (16px) |
| Gap Logo–Teks | `gap-2` (8px) | `gap-2.5` (10px) |

### 7.3 Fitur Mobile-Friendly yang Sudah Diterapkan

- `max-w-md w-full` — Kalkulator menyesuaikan lebar layar sempit
- `overflow-x-auto` + `no-scrollbar` — Formula panjang dapat di-scroll horizontal tanpa scrollbar
- `user-select: none` pada `.btn-3d` — Mencegah seleksi teks saat tap cepat
- `aria-label` pada semua tombol — Kompatibel dengan screen reader mobile
- `meta apple-mobile-web-app-capable` — Dapat dipasang sebagai PWA di iOS
- `manifest.webmanifest` + `sw.js` — Dukungan PWA & offline mode

### 7.4 Rekomendasi Peningkatan Mobile

```html
<!-- 1. Pastikan meta viewport eksplisit ada di <head> -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

```css
/* 2. Hilangkan delay 300ms tap di browser mobile lama */
.btn-3d {
  touch-action: manipulation;
}

/* 3. Untuk layar sangat kecil < 360px */
@media (max-width: 359px) {
  .grid { gap: 4px; }  /* gap-1 */
}
```

```js
// 4. Opsional: Haptic feedback saat tombol ditekan (Android)
button.addEventListener('click', () => {
  if (navigator.vibrate) navigator.vibrate(10);
});
```

---

## 8. Aksesibilitas

### 8.1 Atribut ARIA

Semua tombol memiliki `aria-label` deskriptif dalam Bahasa Indonesia:

```html
aria-label="Bersihkan Seluruh Input (AC)"
aria-label="Hapus Karakter Terakhir (DEL)"
aria-label="Fungsi Sinus"
aria-label="Fungsi Invers Sinus (ArcSin)"
aria-label="Geser Kursor ke Kiri"
aria-label="Hitung Hasil (Sama Dengan)"
aria-label="Toggle Satuan Sudut (DEG atau RAD)"
```

### 8.2 Kontras Warna

| Kombinasi | Rasio Kontras | Status |
|---|---|---|
| Teks putih di `btn-equals` (#059669) | ~4.5:1 | AA |
| Teks emerald (#34d399) di layar hitam | ~9:1 | AAA |
| Teks sky (#38bdf8) di bg gelap | ~6:1 | AA |
| Label tombol putih di merah (#dc2626) | ~4.5:1 | AA |

### 8.3 Shortkey Keyboard Lengkap

| Key | Fungsi |
|---|---|
| `0–9`, `.` | Input angka/desimal |
| `+`, `-`, `*`, `/` | Operator (/ dan * dinormalisasi ke ÷ dan ×) |
| `s` / `S` | sin / asin |
| `c` / `C` | cos / acos |
| `t` / `T` | tan / atan |
| `d` / `D` | Simbol derajat (°) |
| `'` | Simbol menit |
| `"` | Simbol detik |
| `ArrowLeft` / `ArrowRight` | Navigasi kursor kiri/kanan |
| `Home` / `End` | Awal / Akhir formula |
| `Enter` atau `=` | Hitung |
| `Backspace` | Hapus karakter terakhir (smart: hapus fungsi utuh) |
| `Escape` | AC — Reset seluruhnya |

---

## 9. Animasi & Transisi

### 9.1 Tombol Press

```css
/* Durasi sangat cepat untuk respons instan */
transition: all 0.05s ease-in-out;

/* Efek tekan: turun 2px + shadow menyusut */
.btn-3d:active {
  transform: translateY(2px);
  box-shadow: 0 0.5px 0 currentColor,
              inset 0 1.5px 3px rgba(0,0,0,0.4);
}
```

### 9.2 Kursor Kedip

```css
@keyframes caret-blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.15; }
}
/* Durasi 0.8s — natural seperti kursor teks fisik */
.custom-caret {
  animation: caret-blink 0.8s infinite;
}
```

### 9.3 Hover State

```css
/* Semua tombol: background sedikit lebih terang saat hover */
/* Dikontrol via Tailwind hover: utility di masing-masing class */
.btn-func:hover  { background: linear-gradient(180deg, #475569 0%, #334155 100%); }
.btn-num:hover   { background: linear-gradient(180deg, #334155 0%, #1e293b 100%); }
.btn-op:hover    { background: linear-gradient(180deg, #075985 0%, #0369a1 100%); }
/* ... dan seterusnya sesuai pola */
```

### 9.4 Scroll Kursor Otomatis

```js
// Kursor otomatis scroll ke posisi aktif setelah setiap input
caret.scrollIntoView({
  inline: 'center',
  block: 'nearest',
  behavior: 'smooth'
});
```

---

## 10. Panduan Pengembangan

### 10.1 Struktur File

```
Kalkulator_Falak/
├── index.html            <- Markup utama + struktur UI
├── src/
│   ├── calculator.js     <- Logic engine (IIFE module pattern)
│   ├── input.css         <- Sumber CSS (Tailwind + custom classes)
│   └── output.css        <- CSS hasil build (JANGAN edit manual)
├── assets/
│   ├── icon.ico / .png   <- Ikon aplikasi (Electron + PWA)
│   └── logo-nu.png       <- Logo NU untuk header
├── vendor/
│   └── math.min.js       <- mathjs (library kalkulasi)
├── main.js               <- Electron main process
├── sw.js                 <- Service Worker (PWA offline)
├── manifest.webmanifest  <- PWA manifest
├── CHANGELOG.md          <- Riwayat perubahan versi
├── DESIGN.md             <- Dokumen sistem desain ini
└── README.md             <- Panduan umum pengguna
```

### 10.2 Cara Build CSS

```bash
# Development — watch mode (otomatis rebuild saat file berubah)
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch

# Production — minified
npm run build:css

# Jalankan aplikasi Electron
npm start
```

> **Penting:** Jangan pernah mengedit `src/output.css` secara manual.  
> Selalu edit `src/input.css` lalu jalankan build.

### 10.3 Menambah Varian Tombol Baru

1. Definisikan class di `src/input.css` mengikuti pola yang ada:

```css
.btn-namaVarian {
    background: linear-gradient(180deg, #WARNA_ATAS 0%, #WARNA_BAWAH 100%);
    color: #WARNA_TEKS;
    border: 1px solid #WARNA_BORDER;
    border-top-color: #WARNA_BORDER_TERANG;
    box-shadow: 0 2.5px 0 #WARNA_SHADOW, 0 3px 5px rgba(0,0,0,0.25),
                inset 0 1px 0 rgba(255,255,255,0.18);
}
.btn-namaVarian:hover {
    background: linear-gradient(180deg, #WARNA_BAWAH 0%, #WARNA_LEBIH_GELAP 100%);
}
```

2. Tambahkan `class="btn-3d btn-namaVarian"` pada elemen `<button>` di HTML.
3. Sertakan `aria-label` deskriptif.
4. Jalankan `npm run build:css`.

### 10.4 Menambah Fungsi Matematika Baru

Edit `src/calculator.js` pada bagian `scope` di fungsi `evaluateFormulaSafely()`:

```js
const scope = {
    // ... fungsi yang sudah ada ...
    namaFungsi: (x) => Math.namaFungsi(x),  // Tambahkan di sini
};
```

Lalu:
1. Tambahkan tombol HTML di `index.html` (gunakan `onclick="insertAtCursor('namaFungsi ')"`)
2. Daftarkan shortkey di event listener `keydown` jika diperlukan

### 10.5 Checklist QA Desain

Sebelum rilis, verifikasi hal-hal berikut:

- [ ] Semua tombol memiliki `aria-label` dalam Bahasa Indonesia
- [ ] Hover state terlihat jelas di semua varian tombol
- [ ] Efek tekan (`:active`) berfungsi di desktop dan layar sentuh mobile
- [ ] Kursor otomatis scroll saat formula melampaui lebar layar
- [ ] Badge DEG/RAD dan FORMAT:DD/DMS berubah visual sesuai state
- [ ] Status text (READY/PREVIEW/RESULT/ERROR) tampil sesuai kondisi
- [ ] Tampilan DMS (° ' ") terbaca jelas di `resultDisplay`
- [ ] PWA dapat diinstall di browser mobile (Android/iOS)
- [ ] Offline mode berfungsi setelah pertama kali diakses (via Service Worker)
- [ ] Tidak ada console error di Electron maupun browser
- [ ] Tampilan responsif di lebar 320px s.d. 768px

---

## Catatan Versi Dokumen

| Versi | Tanggal | Perubahan |
|---|---|---|
| 1.0.0 | September 2026 | Dokumen awal — mencakup semua komponen v1.1.0-beta |

---

*Dokumen ini adalah referensi utama sistem desain Kalkulator Falak.*  
*Setiap perubahan visual pada `input.css` atau `index.html` sebaiknya diikuti pembaruan dokumen ini.*
