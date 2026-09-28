/**
 * Kalkulator Falak — Service Worker (PWA Offline Cache)
 * 
 * Dikembangkan oleh : Fuad Baidāwī Al-Fajri
 * Berdasarkan aplikasi dari : Lembaga Falakiyah MWCNU Wuluhan Jember
 */

// Bump versi cache ke v1.1.1 (Falakiyah Scientific Light Theme)
const CACHE_NAME = 'kalkulator-falak-v1.1.1';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './src/output.css',
  './src/calculator.js',
  './vendor/math.min.js',
  './assets/logo-nu.png',
  './assets/icon.png',
  './assets/icon.ico',
  './manifest.webmanifest'
];

// 1. Install Event: Pre-cache aset penting & langsung aktifkan SW baru
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

// 2. Activate Event: Hapus seluruh cache versi lama dan klaim kontrol klien
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[SW] Menghapus cache usang:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// 3. Fetch Event: Strategi Network-First untuk auto-update dari Vercel saat online,
// dengan fallback aman ke Cache lokal saat offline (100% PWA compliant)
self.addEventListener('fetch', (event) => {
  // Hanya intercept request GET
  if (event.request.method !== 'GET') return;

  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        // Jika berhasil mengambil dari server (Vercel), simpan salinannya ke cache
        if (networkResponse && networkResponse.status === 200) {
          const responseClone = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
        }
        return networkResponse;
      })
      .catch(() => {
        // Jika offline / network gagal, sajikan dari cache
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          if (event.request.mode === 'navigate') {
            return caches.match('./index.html');
          }
        });
      })
  );
});
