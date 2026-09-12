# 📋 Laporan Analisis Mendalam: Kalkulator Falak

> **Proyek:** Kalkulator Falak
> **Pengembang:** Fuad Baidāwī Al-Fajri  
> **Berdasarkan karya:** Lembaga Falakiyah MWCNU Wuluhan Jember  
> **Tipe:** Aplikasi Desktop Electron (HTML + Vanilla JS)  
> **Tanggal Analisis:** 12 September 2026  
> **Analis:** Antigravity AI

---

## 1. Ringkasan Eksekutif

Proyek ini adalah sebuah **kalkulator ilmiah berbasis Electron** yang dibungkus dari antarmuka HTML/CSS/JS. Tujuannya adalah menyediakan alat bantu hitung ilmu falak (astronomi Islam) dengan fitur konversi DMS (Derajat-Menit-Detik). Secara fungsional, aplikasi sudah cukup lengkap untuk penggunaan dasar, namun terdapat **beberapa masalah kritis** yang perlu segera ditangani terkait keamanan, kelengkapan build, dan ketepatan logika.

---

## 2. Inventaris File

| File | Ukuran | Fungsi |
|---|---|---|
| `index.html` | 32.382 byte | UI + semua logika kalkulator (705 baris) |
| `main.js` | 686 byte | Entry point Electron (BrowserWindow) |
| `package.json` | 799 byte | Konfigurasi npm + Electron Builder |
| `README.txt` | 580 byte | Panduan instalasi singkat |

> [!WARNING]
> **Tidak ada file `Logo NU.png`** dalam direktori proyek. File gambar ini direferensikan di `index.html` baris 183, namun tidak ada di direktori. Jika file ini tidak disertakan, logo akan tampil rusak (broken image) di aplikasi.

---

## 3. Analisis Per File

### 3.1 `main.js` — Electron Entry Point

**Status: ✅ Fungsional, ⚠️ Perlu Perbaikan Keamanan**

```javascript
// Konfigurasi BrowserWindow saat ini
webPreferences: {
  contextIsolation: true,   // ✅ Bagus
  nodeIntegration: false    // ✅ Bagus
}
```

#### Masalah yang Ditemukan:

| # | Masalah | Tingkat | Detail |
|---|---|---|---|
| M1 | **`preload` script tidak ada** | 🔴 Kritis | Tanpa `preload.js`, komunikasi aman antara renderer dan main process tidak bisa dilakukan. Ini praktik terbaik Electron yang wajib ada. |
| M2 | **Tidak ada penanganan crash/error** | 🟡 Sedang | Tidak ada listener untuk `app.on('render-process-gone')` atau `win.webContents.on('crashed')`. |
| M3 | **`icon` tidak dikonfigurasi** | 🟡 Sedang | `BrowserWindow` tidak menyertakan properti `icon`, sehingga menggunakan ikon default Electron. |
| M4 | **Tidak ada `devtools` protection** | 🟠 Rendah | Pada build produksi, DevTools sebaiknya dinonaktifkan. |

---

### 3.2 `package.json` — Konfigurasi Proyek

**Status: ⚠️ Perlu Perbaikan Serius**

#### Masalah yang Ditemukan:

| # | Masalah | Tingkat | Detail |
|---|---|---|---|
| P1 | **`Logo NU.png` tidak ada di `files`** | 🔴 Kritis | Build config hanya menyertakan `index.html` dan `main.js`. File gambar dan aset lain tidak akan masuk ke dalam installer. |
| P2 | **Tidak ada `icon` di build config** | 🟡 Sedang | Properti `icon` tidak didefinisikan di bagian `"win"`. Installer dan aplikasi akan memakai ikon default Electron yang jelek. |
| P3 | **Tidak ada `icon` untuk `nsis`** | 🟡 Sedang | `installerIcon`, `uninstallerIcon`, `installerHeaderIcon` tidak dikonfigurasi. |
| P4 | **Electron versi sangat baru (`^38`)** | 🟠 Rendah | Electron 38 adalah versi yang sangat baru. Perlu dipastikan kompatibilitasnya dengan `electron-builder ^26`. |
| P5 | **Tidak ada `copyright`** | 🟢 Info | Field `"copyright"` tidak ada di bagian `"build"`. Informasi ini muncul di installer dan properties file. |
| P6 | **`perMachine: false`** | 🟢 Info | Instalasi hanya untuk user saat ini. Perlu dipertimbangkan apakah ini sesuai kebutuhan lembaga. |

**Perbaikan yang disarankan untuk `package.json`:**
```json
"files": [
  "index.html",
  "main.js",
  "Logo NU.png",
  "assets/**/*"
],
"win": {
  "target": "nsis",
  "icon": "assets/icon.ico"
},
"build": {
  "copyright": "Copyright © 2026 Lembaga Falakiyah NU Wuluhan Jember"
}
```

---

### 3.3 `index.html` — UI & Logika Kalkulator

**Status: ⚠️⚠️ Perlu Banyak Perbaikan**

#### 🔴 MASALAH KRITIS

---

#### [KRITIS-1] Penggunaan `eval()` — Celah Keamanan

**Lokasi:** Baris 600, 616

```javascript
let res = eval(parsed);  // ← BERBAHAYA
```

Fungsi `eval()` digunakan untuk mengeksekusi rumus yang telah di-parse. Ini adalah **praktik yang sangat berbahaya** karena:
- Rentan terhadap **Code Injection** jika input tidak bersih.
- Meski dalam konteks Electron dengan `nodeIntegration: false`, penggunaan `eval` tetap merupakan anti-pattern.
- Sangat sulit di-debug ketika ada error.

**Solusi yang disarankan:** Gunakan library `math.js` yang sudah memiliki parser ekspresi matematika yang aman, atau implementasikan parser rekursif sendiri.

```javascript
// Alternatif aman menggunakan math.js
import { evaluate } from 'mathjs';
const result = evaluate(expression);
```

---

#### [KRITIS-2] File Aset Gambar Hilang

**Lokasi:** Baris 183

```html
<img src="Logo NU.png" alt="Logo NU" ...>
```

File `Logo NU.png` **tidak ada** dalam direktori proyek. Nama file mengandung spasi yang juga dapat menyebabkan masalah pada beberapa sistem. Sebaiknya gunakan nama file tanpa spasi: `logo-nu.png`.

---

#### 🟡 MASALAH SEDANG

---

#### [SEDANG-1] Semua Logika di Dalam `<script>` HTML

Seluruh ~400 baris JavaScript ditempatkan inline di dalam tag `<script>` di `index.html`. Ini menyulitkan:
- Pemeliharaan dan debugging
- Code splitting
- Unit testing
- Kolaborasi tim

**Solusi:** Pindahkan semua kode JS ke file terpisah, misal `calculator.js`, dan referensikan via `<src>`.

---

#### [SEDANG-2] Penggunaan `CDN Tailwind` di Aplikasi Desktop

**Lokasi:** Baris 7

```html
<script src="https://cdn.tailwindcss.com"></script>
```

Aplikasi Electron yang menggunakan CDN akan **gagal render stylesheet** saat dijalankan **offline** atau tanpa koneksi internet. Padahal aplikasi desktop seharusnya sepenuhnya offline-capable.

**Solusi:** Install Tailwind sebagai dependensi lokal dan build CSS-nya:
```bash
npm install -D tailwindcss
npx tailwindcss -i ./src/input.css -o ./dist/output.css
```
Atau gunakan versi CDN yang sudah di-download dan disimpan secara lokal.

---

#### [SEDANG-3] Bug Logika `appendDMS()` — Regex Kurang Akurat

**Lokasi:** Baris 387

```javascript
let match = beforeCursor.match(
  /(\d+(?:\.\d+)?[°\u00B0\uFFFD]?\d*(?:\.\d+)?[°\u00B0\uFFFD']?\d*(?:\.\d+)?)$/
);
```

Regex ini menggunakan `\uFFFD` (Unicode Replacement Character) sebagai salah satu alternatif simbol derajat. `\uFFFD` adalah karakter pengganti encoding yang tidak seharusnya disamakan dengan simbol derajat `°`. Ini dapat menyebabkan deteksi simbol yang salah pada input tertentu.

---

#### [SEDANG-4] `balanceParentheses()` — Logika Berpotensi Salah

**Lokasi:** Baris 487–519

Fungsi ini mencoba menyeimbangkan tanda kurung secara otomatis, namun logikanya berpotensi menghasilkan ekspresi yang salah. Contoh kasus bermasalah:

```
Input: sin (30 + cos (45)
```

Algoritma akan menutup semua kurung terbuka di akhir, namun tidak menangani kasus di mana kurung penutup muncul terlalu dini. Fungsi ini juga tidak mempertimbangkan konteks fungsi seperti `sin(` vs `(`.

---

#### [SEDANG-5] Regex `parseFormula` Tidak Menangani Semua Edge Case

**Lokasi:** Baris 563

```javascript
p = p.replace(
  /(asin|acos|atan|sin|cos|tan|log|ln|√)(?!\s*\()\s*(-?\s*(?:\d+(?:\.\d+)?|\([^\)]+\)|Math\.PI))/g,
  '$1($2)'
);
```

- Regex ini mencoba menambahkan tanda kurung otomatis pada fungsi yang tidak diikuti `(`. Namun pola `[^\)]+` tidak menangani kurung bersarang seperti `sin (cos (30))`.
- Urutan replacement `asin` vs `sin` di baris 537–539 berpotensi konflik jika tidak di-handle dengan benar (namun dalam kode ini sudah cukup aman karena `asin` diproses lebih dulu).

---

#### [SEDANG-6] Tidak Ada Penanganan `Infinity` dan `NaN` Secara Eksplisit

**Lokasi:** Baris 618

```javascript
if (typeof res === 'number' && !isNaN(res) && isFinite(res)) {
```

Kondisi ini sudah menolak `NaN` dan `Infinity`, namun tidak memberikan pesan yang informatif kepada pengguna. Misalnya:
- `tan(90)` → hasil `Infinity` → hanya tampil "Error" generik
- `asin(2)` → hasil `NaN` → hanya tampil "Error" generik

**Solusi:** Berikan pesan error yang lebih deskriptif:
```javascript
if (!isFinite(res)) resultDisplay.innerText = '∞ (Tak Terhingga)';
else if (isNaN(res)) resultDisplay.innerText = 'Domain Error';
```

---

#### 🟠 MASALAH KECIL / SARAN PENINGKATAN

---

#### [KECIL-1] Tidak Ada Keyboard Shortcut untuk `AC` dan `DEL`

Shortkey keyboard sudah ada untuk fungsi trigonometri, navigasi, dan DMS, namun `AC` (Escape ✅ sudah ada) dan `DEL` (Backspace ✅ sudah ada). Ini sebenarnya sudah ditangani dengan baik.

---

#### [KECIL-2] `innerText` vs `textContent`

Di beberapa tempat digunakan `innerText` untuk menampilkan teks biasa, padahal `textContent` lebih efisien karena tidak memicu reflow CSS. Meski efeknya minimal, ini adalah best practice.

---

#### [KECIL-3] Tidak Ada Validasi Input Ganda Operator

Pengguna dapat memasukkan ekspresi seperti `++ 5` atau `÷÷5` tanpa validasi. Meski `liveEvaluate` akan diam (silent error), lebih baik ada umpan balik visual.

---

#### [KECIL-4] `window.onload` vs `DOMContentLoaded`

**Lokasi:** Baris 320

```javascript
window.onload = function() {
    updateDisplay();
};
```

Untuk halaman HTML statis, `DOMContentLoaded` lebih tepat dan lebih cepat dari `window.onload` karena tidak menunggu semua aset (gambar, CSS eksternal) selesai dimuat.

---

#### [KECIL-5] Variabel Global Tanpa Enkapsulasi

Semua variabel state (`formula`, `cursorPos`, `isDeg`, dll.) dan fungsi (`insertAtCursor`, `clearAll`, dll.) adalah variabel dan fungsi global. Ini rentan terhadap konflik nama jika proyek berkembang.

**Solusi:** Bungkus dalam satu objek atau gunakan module pattern:
```javascript
const Calculator = (() => {
  let formula = '';
  let cursorPos = 0;
  // ... semua state dan fungsi di sini
  return { insertAtCursor, clearAll, calculate, /* ... */ };
})();
```

---

#### [KECIL-6] `formatFormulaForDisplay` — Escape HTML Sebelum Inject `innerHTML`

**Lokasi:** Baris 436–460

Fungsi `escapeHtml` sudah ada dan dipanggil terlebih dahulu, namun setelah itu string HTML literal langsung di-concat dan di-inject ke `innerHTML`. Ini aman selama `escapeHtml` benar-benar membersihkan semua karakter berbahaya, namun tetap perlu diperhatikan jika ada perubahan di masa mendatang.

---

#### [KECIL-7] Tidak Ada `aria-label` pada Tombol

Tombol-tombol kalkulator tidak memiliki atribut `aria-label` yang cukup deskriptif untuk aksesibilitas (screen reader). Contoh: tombol `÷` hanya berisi entitas HTML `&divide;` tanpa label teks yang dapat dibaca.

```html
<!-- Sebaiknya tambahkan: -->
<button aria-label="Bagi" ...>&divide;</button>
```

---

### 3.4 `README.txt` — Dokumentasi

**Status: ⚠️ Kurang Lengkap**

| # | Masalah | Detail |
|---|---|---|
| R1 | **Tidak ada screenshot** | Tidak ada gambaran visual aplikasi |
| R2 | **Tidak menjelaskan fitur** | Tidak ada deskripsi fitur-fitur yang tersedia |
| R3 | **Format `.txt` kurang profesional** | Sebaiknya gunakan `README.md` untuk mendukung Markdown rendering di GitHub/GitLab |
| R4 | **Tidak ada persyaratan sistem** | Versi Windows minimum tidak disebutkan |
| R5 | **Tidak ada instruksi menjalankan untuk dev** | Tidak ada `npm start` untuk mode development |

---

## 4. Ringkasan Masalah & Prioritas

| Prioritas | Jumlah | Masalah Utama |
|---|---|---|
| 🔴 Kritis | 2 | `eval()` tidak aman, `Logo NU.png` hilang |
| 🟡 Sedang | 8 | CDN Tailwind offline, logika regex, aset tidak di-bundle |
| 🟠 Kecil | 7 | Variabel global, aksesibilitas, pesan error |
| 🟢 Info | 3 | README, copyright, ikon installer |

---

## 5. Rekomendasi Perbaikan Berurutan

### Tahap 1 — Perbaikan Kritis (Segera)
1. **Tambahkan `Logo NU.png`** ke direktori proyek dan sesuaikan path di `index.html` menjadi `logo-nu.png`.
2. **Daftarkan aset gambar** di `package.json` bagian `"files"`.
3. **Ganti `eval()`** dengan library `math.js` yang aman.

### Tahap 2 — Perbaikan Infrastruktur
4. **Download Tailwind CSS** secara lokal atau gunakan PostCSS build agar aplikasi bisa jalan offline.
5. **Pisahkan JavaScript** dari `index.html` ke file `calculator.js` terpisah.
6. **Tambahkan `preload.js`** untuk Electron.
7. **Tambahkan ikon aplikasi** (`icon.ico`) dan referensikan di `package.json` dan `main.js`.

### Tahap 3 — Perbaikan Kualitas Kode
8. **Enkapsulasi state** dalam module/closure pattern.
9. **Perbaiki pesan error** menjadi lebih informatif (NaN, Infinity).
10. **Tambahkan `aria-label`** pada tombol-tombol kalkulator.
11. **Upgrade `README.txt`** ke `README.md` dengan fitur lengkap dan screenshot.

---

## 6. Contoh Kode Perbaikan Utama

### Mengganti `eval()` dengan `math.js`

```html
<!-- Tambahkan di <head> -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/13.1.1/math.min.js"></script>
```

```javascript
// Ganti liveEvaluate() menjadi:
function liveEvaluate() {
    if (!formula.trim()) { /* ... */ return; }
    try {
        let parsed = parseFormula(formula);
        let res = math.evaluate(parsed); // ← Aman!
        // ...
    } catch (e) { /* abaikan error parsial */ }
}
```

### `package.json` yang Diperbaiki

```json
{
  "name": "kalkulator-falak",
  "version": "1.0.0",
  "description": "Kalkulator Falak Lembaga Falakiyah NU Wuluhan Jember",
  "main": "main.js",
  "author": "Lembaga Falakiyah NU Wuluhan Jember",
  "license": "MIT",
  "scripts": {
    "start": "electron .",
    "dist": "electron-builder --win nsis"
  },
  "devDependencies": {
    "electron": "^38.1.0",
    "electron-builder": "^26.0.12"
  },
  "build": {
    "appId": "id.nu.wuluhan.kalkulatorfalak",
    "productName": "Kalkulator Falak",
    "copyright": "Copyright © 2026 Lembaga Falakiyah NU Wuluhan Jember",
    "files": [
      "index.html",
      "main.js",
      "logo-nu.png",
      "assets/**/*"
    ],
    "win": {
      "target": "nsis",
      "icon": "assets/icon.ico"
    },
    "nsis": {
      "oneClick": false,
      "perMachine": false,
      "allowToChangeInstallationDirectory": true,
      "createDesktopShortcut": true,
      "createStartMenuShortcut": true,
      "installerIcon": "assets/icon.ico",
      "uninstallerIcon": "assets/icon.ico"
    }
  }
}
```

---

## 7. Penilaian Akhir

| Aspek | Nilai | Catatan |
|---|---|---|
| **Fungsi Inti** | 7/10 | Kalkulator berfungsi dengan baik untuk kasus umum |
| **Keamanan** | 4/10 | Penggunaan `eval()` adalah risiko serius |
| **Kualitas Kode** | 5/10 | Semua logika campur aduk di satu file, variabel global |
| **Build/Deploy** | 4/10 | Aset gambar tidak di-bundle, Tailwind dari CDN |
| **Dokumentasi** | 3/10 | README sangat minim, tidak ada komentar inline yang cukup |
| **Aksesibilitas** | 3/10 | Tidak ada `aria-label`, tidak ada dukungan screen reader |
| **Desain UI** | 8/10 | Visual 3D kalkulator sangat bagus dan profesional |

> **Rekomendasi Utama:** Perbaiki masalah kritis (aset hilang + `eval`) terlebih dahulu sebelum mendistribusikan installer ke pengguna.
