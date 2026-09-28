# ARCHITECTURE.md — Dokumentasi Arsitektur
## Kalkulator Falak | Dikembangkan oleh Fuad Baidāwī Al-Fajri
> Berdasarkan aplikasi Lembaga Falakiyah MWCNU Wuluhan Jember

**Versi:** 1.1.0
**Tanggal:** 28 September 2026

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

### ADR-004: Desain Sistem 3D Realistis & Mobile Haptic Feedback (v1.1.0)
**Keputusan:** Mengadopsi estetika physical skeuomorphic 3D (tombol cembung ber-bevel, layar cekung berpendar) dan haptic feedback via Web Vibration API.
**Alasan:** Meningkatkan kepuasan visual serta memberikan kepastian input sentuh (tactile confirmation) saat digunakan pada smartphone di lapangan.
**Trade-off:** Memerlukan CSS styling berlapis (box-shadow ganda, gradient bertingkat) yang didefinisikan secara rapi di `DESIGN.md`.

### ADR-005: Dual-Target Deployment (Desktop Electron + PWA Web App via Vercel)
**Keputusan:** Menyatukan basis kode tunggal (single codebase) untuk menghasilkan Windows Desktop Installer (.exe) dan Web App PWA yang di-deploy ke Vercel.
**Alasan:** Memudahkan pemeliharaan (tidak ada duplikasi kode), pengguna lapangan dapat mengakses via URL ponsel tanpa instalasi manual .exe.
**Trade-off:** Diperlukan isolasi fallback API (`window.falakAPI`) agar kode renderer tidak bergantung eksklusif pada runtime Node.js/Electron.