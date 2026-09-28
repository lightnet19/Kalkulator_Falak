/**
 * Kalkulator Falak — Electron Preload Script
 * 
 * Dikembangkan oleh : Fuad Baidāwī Al-Fajri
 * Berdasarkan aplikasi dari : Lembaga Falakiyah MWCNU Wuluhan Jember
 */

const { contextBridge, ipcRenderer } = require('electron');

// CATATAN: 'appVersion' diselaraskan secara manual dengan "version" di package.json (Single Source of Truth)
contextBridge.exposeInMainWorld('falakAPI', {
    appVersion: '1.1.1',
    platform: process.platform
});
