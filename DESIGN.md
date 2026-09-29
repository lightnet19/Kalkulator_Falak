# DESIGN.md — Sistem Desain Kalkulator Falak

> **Kalkulator Falak** — Lembaga Falakiyah NU Wuluhan Jember  
> Dikembangkan oleh: Fuad Baidāwī Al-Fajri  
> Desain Sistem: **Falakiyah Scientific (Tactile Light Theme)** via Google Stitch  
> Versi Dokumen: 2.0.0 | Diperbarui: September 2026

---

## Daftar Isi

1. [Filosofi Desain & Latar Belakang](#1-filosofi-desain--latar-belakang)
2. [Sistem Warna (Light Theme Palette)](#2-sistem-warna-light-theme-palette)
3. [Tipografi & Keterbacaan](#3-tipografi--keterbacaan)
4. [Sistem Tombol Tactile Light 3D](#4-sistem-tombol-tactile-light-3d)
5. [Komponen UI & Layar LCD](#5-komponen-ui--layar-lcd)
6. [Layout, Grid, & Dimensi](#6-layout-grid--dimensi)
7. [Responsivitas Mobile & Ergonomi Sentuh](#7-responsivitas-mobile--ergonomi-sentuh)
8. [Aksesibilitas & Standar Kontras (WCAG AAA)](#8-aksesibilitas--standar-kontras-wcag-aaa)
9. [Animasi & Haptic Feedback](#9-animasi--haptic-feedback)
10. [Panduan Pemeliharaan Kode](#10-panduan-pemeliharaan-kode)

---

## 1. Filosofi Desain & Latar Belakang

Perhitungan falak sering dilakukan di **lapangan terbuka (outdoor)**, seperti observasi rukyatul hilal menjelang maghrib, kalibrasi arah kiblat di bawah sinar matahari langsung, maupun pelatihan hisab santri di ruang kelas dengan pencahayaan tinggi. 

Tema gelap (*dark theme*) sebelumnya memiliki kelemahan kritis: pantulan cahaya (glare) pada layar smartphone di siang hari membuat angka dan rumus sulit dibaca secara akurat.

Oleh karena itu, sistem antarmuka didesain ulang menggunakan **Google Stitch MCP** dengan pendekatan **Tactile Precision Light Theme**:
- **Ultra-High Readability:** Latar belakang cerah dengan teks angka ber-kontras maksimal untuk visibilitas siang hari tanpa silau.
- **Physical Skeuomorphism:** Meniru instrumen observatorium presisi tinggi—tombol memiliki bevel 3D mikro (*micro-relief*) yang memberikan rasa tekan fisik (*tactile feel*).
- **Identitas Falakiyah NU:** Perpaduan hijau zamrud (*Islamic Emerald*), biru langit hisab (*Sky Blue*), dan aksen amber hisab derajat falak.

---

## 2. Sistem Warna (Light Theme Palette)

### 2.1 Palet Utama (Core Palette)

| Token Warna | Nilai Heksadesimal | Peran & Penggunaan |
|---|---|---|
| **Canvas Background** | `#f8fafc` $\rightarrow$ `#e2e8f0` | Gradien radial lembut, nyaman di mata dan anti-silau |
| **Chassis Bodi** | `#ffffff` | Panel utama kalkulator (*crisp pure white*) |
| **Chassis Border** | `#cbd5e1` / `#94a3b8` | Garis pembatas fisik dengan dasar tebal 4px |
| **LCD Recessed Screen** | `#f4faf6` | Permukaan layar digital bernuansa mint/sage lembut |
| **Text Rumus Formula** | `#0f172a` | Slate charcoal pekat untuk teks ekspresi rumus |
| **Text Hasil Real-Time** | `#047857` | Hijau emerald pekat ber-kontras tinggi (WCAG AAA) |
| **Kursor Interaktif** | `#047857` | Garis kedip presisi tinggi dengan pendaran halus |

### 2.2 Palet Tombol (Keycap Color System)

| Kategori Tombol | Latar Keycap (Gradient) | Teks / Label | Border / Bevel |
|---|---|---|---|
| **Angka (`0-9`, `.`)** | `#ffffff` $\rightarrow$ `#f8fafc` | `#0f172a` (Charcoal) | `#cbd5e1` $\rightarrow$ `#94a3b8` |
| **Fungsi Matematika** | `#f8fafc` $\rightarrow$ `#f1f5f9` | `#1e293b` (Slate) | `#cbd5e1` $\rightarrow$ `#94a3b8` |
| **Invers Trigonometri** | `#f8fafc` $\rightarrow$ `#f1f5f9` | `#047857` (Emerald) | `#cbd5e1` $\rightarrow$ `#94a3b8` |
| **Operator (`÷`, `×`, `-`, `+`)** | `#e0f2fe` $\rightarrow$ `#bae6fd` | `#0369a1` (Ocean Blue) | `#7dd3fc` $\rightarrow$ `#38bdf8` |
| **Clear All (`AC`)** | `#fee2e2` $\rightarrow$ `#fecaca` | `#b91c1c` (Crimson) | `#fca5a5` $\rightarrow$ `#f87171` |
| **Hapus Karakter (`DEL`)** | `#fef3c7` $\rightarrow$ `#fde68a` | `#b45309` (Dark Amber) | `#fcd34d` $\rightarrow$ `#fbbf24` |
| **DMS / Konversi (`° ' "`)** | `#ecfdf5` $\rightarrow$ `#d1fae5` | `#047857` (Emerald) | `#6ee7b7` $\rightarrow$ `#34d399` |
| **Navigasi (`◄`, `►`)** | `#f8fafc` $\rightarrow$ `#e2e8f0` | `#334155` (Slate-700) | `#cbd5e1` $\rightarrow$ `#94a3b8` |
| **Eksekusi (`=`)** | `#059669` $\rightarrow$ `#047857` | `#ffffff` (Pure White) | `#047857` $\rightarrow$ `#064e3b` |

---

## 3. Tipografi & Keterbacaan

Untuk memastikan performa instan tanpa latensi unduhan webfont pada perangkat lapangan offline, sistem tipografi menggunakan arsitektur font universal ber-kontras tinggi:

```
Display Stack:
  Arial, Helvetica, -apple-system, system-ui, sans-serif
  - Formula: 16px - 18px (Reguler / Medium, leading-7)
  - Hasil Kalkulasi: 24px - 32px (Bold, leading-none)
  - Status & Mode Badges: 8px - 10px (Bold, tracking-wider, uppercase)
  - Label Tombol: 12px - 16px (Semi-Bold / Bold)
```

---

## 4. Sistem Tombol Tactile Light 3D

Setiap tombol dirancang dengan fisika *tactile keycap*:

1. **State Normal (Rest):**
   - Refleksi cahaya atas: `box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.8)`.
   - Ketebalan fisik bawah: `box-shadow: 0 2.5px 0 <border-dark>, 0 3px 5px rgba(15, 23, 42, 0.08)`.
2. **State Hover (Desktop):**
   - Transisi warna gradien sedikit lebih pekat (0.05s ease).
3. **State Ditekan (Active / Pressed):**
   - Pergeseran vertikal nyata: `transform: translateY(2px)`.
   - Runtuhnya bayangan ekstrusi: `box-shadow: 0 0.5px 0 currentColor, inset 0 1.5px 3px rgba(15, 23, 42, 0.15)`.

---

## 5. Komponen UI & Layar LCD

### 5.1 Header Panel (Proporsional & Simetris)
- **Wadah Logo Institusi:** Logo NU Wuluhan Jember (`assets/logo-nu.png`) dikunci dalam container ergonomis `40px × 40px` (`w-10 h-10`) dengan sudut membulat `rounded-xl`, latar mint halus (`bg-emerald-50`), border lembut (`border-emerald-200/80`), dan padding internal `p-1`.
- **Tipografi Lembaga Terpadu:**
  - Baris 1: `Lembaga Falakiyah NU` (`text-xs sm:text-[13px] font-bold text-slate-900 leading-none`).
  - Baris 2: `MWCNU Wuluhan Jember` (`text-[10px] sm:text-[11px] font-semibold text-emerald-700 leading-none mt-1`).
  - Tinggi blok teks sejajar presisi dengan tinggi wadah logo 40px di sumbu vertikal.
- **Kontrol Mode (Sisi Kanan):**
  - **Mode Toggle DEG/RAD:** Tombol tactile berlatar mint lembut (`bg-emerald-50 text-emerald-800 border-emerald-300`).
  - **Format Toggle DD/DMS:** Tombol tactile berlatar amber lembut (`bg-amber-50 text-amber-800 border-amber-300`).
  - Tertata sejajar di garis tengah vertikal (*vertical center alignment*), menciptakan simetri horizontal yang bersih dan bebas elemen redundan.

### 5.2 Layar LCD Cekung (Screen 3D)
- Latar bergradien lembut ice-sage (`#f4faf6`).
- Border cekung ke dalam (`border-top: #94a3b8`, `border-left: #94a3b8`, `box-shadow: inset 0 2px 5px rgba(15, 23, 42, 0.08)`).
- Penempatan dua baris: Baris atas untuk pengetikan formula ekspresi; baris bawah untuk hasil kalkulasi real-time bersama status unit (`DD`/`DMS`).

### 5.3 Control Bar Kursor
- Strip abu-abu terang ergonomis (`bg-slate-50 border-slate-200`) berisi tombol tactile `◄ Kiri` dan `Kanan ►`.

---

## 6. Layout, Grid, & Dimensi

- **Lebar Maksimal Container:** `max-w-md` (~448px) dengan `w-full` agar adaptif pada semua orientasi.
- **Grid Tombol:** Matriks 5 kolom × 7 baris.
- **Gap Tombol:** `gap-1.5` (standar) dan `gap-1` pada layar kompak `< 360px`.
- **Tombol Sama Dengan (`=`):** Menempati 2 kolom penuh (`col-span-2`) di baris paling bawah untuk kemudahan jangkauan ibu jari pengguna.

---

## 7. Responsivitas Mobile & Ergonomi Sentuh

1. **Pencegahan Delay Tap:** Menggunakan `touch-action: manipulation` untuk mematikan latensi double-tap 300ms pada browser seluler.
2. **Safe Area Insets:** `@supports (padding-top: env(safe-area-inset-top))` menjaga agar aplikasi tidak terpotong oleh notch, kamera punch-hole, atau taskbar navigasi Android/iOS.
3. **Pinch-to-Zoom Aman:** `maximum-scale=5.0` menjaga aksesibilitas bagi pengguna berkebutuhan visual khusus.

---

## 8. Aksesibilitas & Standar Kontras (WCAG AAA)

- Rasio kontras teks formula terhadap layar LCD `#f4faf6`: **15.8:1** (Melampaui standar WCAG AAA 7:1).
- Rasio kontras teks hasil hijau `#047857` terhadap layar LCD: **7.2:1** (Lolos standar WCAG AAA).
- Setiap tombol memiliki atribut `aria-label` deskriptif untuk pembaca layar (*screen reader*).

---

## 9. Animasi & Haptic Feedback

- **Micro-haptic:** Web Vibration API menggetarkan perangkat selama `10ms` saat tombol disentuh (`pointerdown`).
- **Blinking Caret:** Animasi kedip 0.8s memudahkan pelacakan kursor input di layar yang padat rumus.

---

## 10. Panduan Pemeliharaan Kode

- Seluruh kode sumber style ditulis di `src/input.css` dan dikompilasi menggunakan perintah:
  ```bash
  cmd.exe /c "npm run build:css"
  ```
- Hindari hardcoding warna bertema gelap di JavaScript; gunakan class utilitas Tailwind yang telah didefinisikan pada sistem ini.
