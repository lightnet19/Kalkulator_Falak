# SECURITY.md — Kebijakan Keamanan
## Kalkulator Falak | Dikembangkan oleh Fuad Baidāwī Al-Fajri

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

**Pengembang:** Fuad Baidāwī Al-Fajri  
**Email:** [email pengembang]

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

### [TERSELESAIKAN] Penggunaan eval() — Prioritas Tinggi
- **Status:** Selesai di v1.1.0
- **Mitigasi:** Evaluasi ekspresi matematika kini menggunakan pustaka sandboxed `math.js` (vendor/math.min.js) dengan context engine yang aman.

### [CATATAN ARSITEKTUR] Vercel Web Deployment (`vercel.json`)
- **Status:** Mitigasi Terkelola
- **Detail:** Penggunaan `outputDirectory: "."` pada `vercel.json` menjaga arsitektur root tetap simpel untuk PWA statis. File sensitif seperti `.env` atau credential tidak boleh diletakkan di root repositori. Jika di masa depan repositori memuat source code privat/server-side, disarankan memisahkan aset publik ke folder `public/` atau `dist/`.

---

## Praktik Keamanan yang Diterapkan

- Evaluasi ekspresi menggunakan math.js engine sandboxed
- Tidak ada akses jaringan berbahaya dari renderer process
- Tidak ada penyimpanan data sensitif
- Tidak ada autentikasi atau data pengguna
- Build produksi menonaktifkan DevTools
- `contextIsolation` dan `nodeIntegration` dikonfigurasi dengan benar