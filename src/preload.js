/**
 * Kalkulator Falak — Electron Preload Script
 * 
 * Dikembangkan oleh : Fuad Baidāwī Al-Fajri
 * Berdasarkan aplikasi dari : Lembaga Falakiyah MWCNU Wuluhan Jember
 */

const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('falakAPI', {
    appVersion: '1.1.0',
    platform: process.platform
});
