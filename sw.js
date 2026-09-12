/**
 * Kalkulator Falak — Service Worker (PWA Offline Cache)
 * 
 * Dikembangkan oleh : Fuad Baidāwī Al-Fajri
 * Berdasarkan aplikasi dari : Lembaga Falakiyah MWCNU Wuluhan Jember
 */

const CACHE_NAME = 'kalkulator-falak-v1.1.0';
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

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request).catch(() => {
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
      });
    })
  );
});
