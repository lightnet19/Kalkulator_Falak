/**
 * Kalkulator Falak — Electron Main Process
 * 
 * Dikembangkan oleh : Fuad Baidāwī Al-Fajri
 * Berdasarkan aplikasi dari : Lembaga Falakiyah MWCNU Wuluhan Jember
 */

const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 430,
    height: 760,
    minWidth: 380,
    minHeight: 650,
    autoHideMenuBar: true,
    resizable: true,
    title: 'Kalkulator Falak - Lembaga Falakiyah NU Wuluhan Jember',
    icon: path.join(__dirname, 'assets/icon.ico'),
    webPreferences: {
      preload: path.join(__dirname, 'src/preload.js'),
      contextIsolation: true,
      nodeIntegration: false
    }
  });

  win.loadFile(path.join(__dirname, 'index.html'));
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
