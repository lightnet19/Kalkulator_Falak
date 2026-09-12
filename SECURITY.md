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

### [AKTIF] Penggunaan eval() — Prioritas Tinggi
- **Status:** Akan diperbaiki di v1.0.2 (Milestone 1)
- **Dampak:** Rendah dalam konteks offline desktop, namun tetap merupakan anti-pattern
- **Mitigasi sementara:** Aplikasi berjalan offline dan tidak menerima input dari jaringan
- **Perbaikan:** Ganti dengan math.js (lihat DEVPLAN.md — M1)

---

## Praktik Keamanan yang Diterapkan

- Tidak ada akses jaringan dari renderer process
- Tidak ada penyimpanan data sensitif
- Tidak ada autentikasi atau data pengguna
- Build produksi menonaktifkan DevTools
- `contextIsolation` dan `nodeIntegration` dikonfigurasi dengan benar