/**
 * Kalkulator Falak — Logic Engine (v1.1.0-beta)
 * 
 * Dikembangkan oleh : Fuad Baidāwī Al-Fajri
 * Berdasarkan aplikasi dari : Lembaga Falakiyah MWCNU Wuluhan Jember
 */

const KalkulatorFalak = (function () {
    const DEG_SYM = '\u00B0';

    let formula = '';
    let cursorPos = 0;           
    let isDeg = true;            
    let isDMSOutput = false;     
    let lastAns = 0;
    let lastRawResult = 0;
    let evaluated = false;

    let formulaDisplay;
    let resultDisplay;
    let degRadBtn;
    let formatModeBadge;
    let resultUnitBadge;
    let statusText;

    // Safe API Fallback untuk Browser / Vercel Web App
    window.falakAPI = window.falakAPI || { appVersion: '1.1.0', platform: 'web' };

    window.addEventListener('DOMContentLoaded', () => {
        formulaDisplay = document.getElementById('formulaDisplay');
        resultDisplay = document.getElementById('resultDisplay');
        degRadBtn = document.getElementById('degRadBtn');
        formatModeBadge = document.getElementById('formatModeBadge');
        resultUnitBadge = document.getElementById('resultUnitBadge');
        statusText = document.getElementById('statusText');

        updateDisplay();

        // Registrasi PWA Service Worker (Offline Support di Browser/Mobile)
        if ('serviceWorker' in navigator && window.location.protocol.startsWith('http')) {
            navigator.serviceWorker.register('./sw.js').catch((err) => {
                console.log('SW Registration skipped/failed:', err);
            });
        }
    });

    function toggleDegRad() {
        isDeg = !isDeg;
        if (degRadBtn) {
            degRadBtn.innerText = isDeg ? 'DEG' : 'RAD';
            degRadBtn.className = isDeg 
                ? 'btn-3d px-2 py-0.5 text-[11px] font-bold rounded bg-emerald-950 text-emerald-400 border border-emerald-500/50 hover:bg-emerald-900 transition'
                : 'btn-3d px-2 py-0.5 text-[11px] font-bold rounded bg-sky-950 text-sky-400 border border-sky-500/50 hover:bg-sky-900 transition';
        }
        liveEvaluate();
    }

    function toggleResultFormat() {
        isDMSOutput = !isDMSOutput;
        updateFormatBadges();
        renderResultDisplay(lastRawResult);
    }

    function updateFormatBadges() {
        if (!formatModeBadge || !resultUnitBadge) return;
        if (isDMSOutput) {
            formatModeBadge.innerText = 'DMS';
            resultUnitBadge.innerText = 'DMS';
            resultUnitBadge.className = 'formula-font text-[8px] font-bold px-1.5 py-0.2 rounded bg-amber-950 text-amber-300 border border-amber-500/50';
        } else {
            formatModeBadge.innerText = 'DD';
            resultUnitBadge.innerText = 'DD';
            resultUnitBadge.className = 'formula-font text-[8px] font-bold px-1.5 py-0.2 rounded bg-slate-800 text-sky-300 border border-slate-700';
        }
    }

    // NAVIGASI KURSOR
    function moveCursorLeft() {
        if (evaluated) evaluated = false;
        if (cursorPos > 0) {
            cursorPos--;
            updateDisplay();
        }
    }

    function moveCursorRight() {
        if (evaluated) evaluated = false;
        if (cursorPos < formula.length) {
            cursorPos++;
            updateDisplay();
        }
    }

    // MENYISIPKAN KARAKTER (Dengan Validasi Double Operator)
    function insertAtCursor(text) {
        if (evaluated) {
            evaluated = false;
        }

        const binaryOps = ['+', '×', '÷', '*', '/', '^'];
        const isNewCharOp = binaryOps.includes(text);
        const charBefore = cursorPos > 0 ? formula[cursorPos - 1] : '';

        // Cegah penumpukan operator biner ganda
        if (isNewCharOp && binaryOps.includes(charBefore)) {
            formula = formula.slice(0, cursorPos - 1) + text + formula.slice(cursorPos);
        } else {
            formula = formula.slice(0, cursorPos) + text + formula.slice(cursorPos);
            cursorPos += text.length;
        }

        updateDisplay();
        liveEvaluate();
    }

    // TOMBOL SMART ° ' "
    function appendDMS() {
        if (evaluated) {
            toggleResultFormat();
            return;
        }

        let beforeCursor = formula.slice(0, cursorPos);
        let match = beforeCursor.match(/(\d+(?:\.\d+)?[°\u00B0\uFFFD]?\d*(?:\.\d+)?[°\u00B0\uFFFD']?\d*(?:\.\d+)?)$/);

        let symbol = DEG_SYM;
        if (match) {
            let token = match[1];
            if (!token.includes(DEG_SYM) && !token.includes('°')) {
                symbol = DEG_SYM;
            } else if (!token.includes("'")) {
                symbol = "'";
            } else if (!token.includes('"')) {
                symbol = '"';
            }
        }
        insertAtCursor(symbol);
    }

    function clearAll() {
        formula = '';
        cursorPos = 0;
        evaluated = false;
        lastRawResult = 0;
        if (resultDisplay) resultDisplay.innerText = '0';
        if (statusText) statusText.innerText = 'READY';
        updateDisplay();
    }

    function backspace() {
        if (evaluated) {
            evaluated = false;
        }
        if (cursorPos > 0) {
            const funcs = ['asin ', 'acos ', 'atan ', 'sin ', 'cos ', 'tan ', 'log ', 'ln ', 'asin', 'acos', 'atan', 'sin', 'cos', 'tan', 'log', 'ln', 'ANS'];
            let beforeCursor = formula.slice(0, cursorPos);
            let matchedLen = 1;
            
            for (let f of funcs) {
                if (beforeCursor.endsWith(f)) {
                    matchedLen = f.length;
                    break;
                }
            }
            
            formula = formula.slice(0, cursorPos - matchedLen) + formula.slice(cursorPos);
            cursorPos -= matchedLen;
            updateDisplay();
            liveEvaluate();
        }
    }

    function escapeHtml(str) {
        return str
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    /* Rendering Visual dengan Spasi Tambahan pada Operator Matematika */
    function formatFormulaForDisplay(str) {
        let escaped = escapeHtml(str);
        let formatted = escaped
            .replace(/[\u00B0°\uFFFD]/g, '&deg;')
            .replace(/[\u00D7×]/g, ' &times; ')
            .replace(/[\u00F7÷]/g, ' &divide; ')
            .replace(/\+/g, ' + ')
            .replace(/([\d&deg;'"]|\))(-)/g, '$1 - ')
            .replace(/[\u03C0π]/g, '&pi;')
            .replace(/asin/g, 'sin<sup class="text-[0.65em] -top-1">-1</sup>')
            .replace(/acos/g, 'cos<sup class="text-[0.65em] -top-1">-1</sup>')
            .replace(/atan/g, 'tan<sup class="text-[0.65em] -top-1">-1</sup>');

        return formatted.replace(/\s+/g, ' ');
    }

    function updateDisplay() {
        if (!formulaDisplay) return;

        let before = formatFormulaForDisplay(formula.slice(0, cursorPos));
        let after = formatFormulaForDisplay(formula.slice(cursorPos));
        
        let cursorHtml = '<span id="activeCaret" class="custom-caret"></span>';
        
        formulaDisplay.innerHTML = before + cursorHtml + after;

        setTimeout(() => {
            const caret = document.getElementById('activeCaret');
            if (caret) {
                caret.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
            }
        }, 10);
    }

    // Auto Balancing Tanda Kurung Otomatis
    function balanceParentheses(expr) {
        let result = '';
        let openCount = 0;
        
        for (let i = 0; i < expr.length; i++) {
            let char = expr[i];
            if (char === '(') {
                openCount++;
                result += char;
            } else if (char === ')') {
                openCount--;
                result += char;
                let nextChar = expr.slice(i + 1).trim()[0];
                if (['*', '/', '+', '-', '^', '×', '÷'].includes(nextChar) && openCount > 0) {
                    while (openCount > 0) {
                        result += ')';
                        openCount--;
                    }
                }
            } else {
                result += char;
            }
        }
        
        while (openCount > 0) {
            result += ')';
            openCount--;
        }
        
        return result;
    }

    // Evaluator Matematika Aman dengan math.js
    function evaluateFormulaSafely(expr) {
        let p = expr;

        // Normalisasi simbol derajat, kali, bagi, pi, petik
        p = p.replace(/[\u00B0°\uFFFD]/g, '°');
        p = p.replace(/[\u00D7×]/g, '*');
        p = p.replace(/[\u00F7÷]/g, '/');
        p = p.replace(/[\u03C0π]/g, 'pi');
        p = p.replace(/[’′]/g, "'").replace(/[”″]/g, '"');

        // 1. Konversi double minus '--' menjadi '-(-'
        p = p.replace(/--/g, '-(-');

        // 2. Keseimbangan tanda kurung otomatis
        p = balanceParentheses(p);

        p = p.replace(/sin[-^]?1|sin⁻¹/gi, 'asin')
             .replace(/cos[-^]?1|cos⁻¹/gi, 'acos')
             .replace(/tan[-^]?1|tan⁻¹/gi, 'atan');

        p = p.replace(/(\d+(?:\.\d+)?)°\s*(\d+(?:\.\d+)?)['°]\s*(\d+(?:\.\d+)?)["°]?/g, (m, d, min, sec) => {
            let dec = parseFloat(d) + parseFloat(min) / 60 + parseFloat(sec) / 3600;
            return `(${dec})`;
        });

        p = p.replace(/(\d+(?:\.\d+)?)°\s*(\d+(?:\.\d+)?)['°]?/g, (m, d, min) => {
            let dec = parseFloat(d) + parseFloat(min) / 60;
            return `(${dec})`;
        });

        p = p.replace(/(\d+(?:\.\d+)?)°/g, (m, d) => {
            return `(${d})`;
        });

        p = p.replace(/ANS/g, `(${lastAns})`);

        p = p.replace(/\)\s*\(/g, ')*(');
        p = p.replace(/\)\s*(\d|\()/g, ')*$1');
        p = p.replace(/(\d)\s*\(/g, '$1*(');

        p = p.replace(/(asin|acos|atan|sin|cos|tan|log|ln|√)(?!\s*\()\s*(-?\s*(?:\d+(?:\.\d+)?|\([^\)]+\)|pi|PI))/g, '$1($2)');

        p = p.replace(/√\s*\(/g, 'sqrt(');

        // Definisikan Scope untuk Trigonometri & Fungsi Tambahan
        const scope = {
            ANS: lastAns,
            ans: lastAns,
            pi: Math.PI,
            PI: Math.PI,
            e: Math.E,
            log: (x) => Math.log10(x),
            ln: (x) => Math.log(x),
            sqrt: (x) => Math.sqrt(x),
            sin: isDeg ? (x) => Math.sin((x * Math.PI) / 180) : (x) => Math.sin(x),
            cos: isDeg ? (x) => Math.cos((x * Math.PI) / 180) : (x) => Math.cos(x),
            tan: isDeg ? (x) => Math.tan((x * Math.PI) / 180) : (x) => Math.tan(x),
            asin: isDeg ? (x) => (Math.asin(x) * 180) / Math.PI : (x) => Math.asin(x),
            acos: isDeg ? (x) => (Math.acos(x) * 180) / Math.PI : (x) => Math.acos(x),
            atan: isDeg ? (x) => (Math.atan(x) * 180) / Math.PI : (x) => Math.atan(x)
        };

        return math.evaluate(p, scope);
    }

    function liveEvaluate() {
        if (!formula.trim()) {
            if (resultDisplay) resultDisplay.innerText = '0';
            if (statusText) statusText.innerText = 'READY';
            return;
        }

        try {
            let res = evaluateFormulaSafely(formula);
            if (typeof res === 'number' && !isNaN(res) && isFinite(res)) {
                lastRawResult = res;
                renderResultDisplay(res);
                if (statusText) statusText.innerText = 'PREVIEW';
            }
        } catch (e) {
            // Abaikan error parsial saat mengetik
        }
    }

    function calculate() {
        if (!formula.trim()) return;

        try {
            let res = evaluateFormulaSafely(formula);

            if (typeof res === 'number') {
                if (isNaN(res)) {
                    if (resultDisplay) resultDisplay.innerText = 'Domain Error';
                    if (statusText) statusText.innerText = 'ERROR';
                } else if (!isFinite(res)) {
                    if (resultDisplay) resultDisplay.innerText = '∞ Tak Terhingga';
                    if (statusText) statusText.innerText = 'ERROR';
                } else {
                    lastAns = res;
                    lastRawResult = res;
                    renderResultDisplay(res);
                    if (statusText) statusText.innerText = 'RESULT';
                    evaluated = true;
                }
            } else {
                if (resultDisplay) resultDisplay.innerText = 'Error';
                if (statusText) statusText.innerText = 'ERROR';
            }
        } catch (e) {
            if (resultDisplay) resultDisplay.innerText = 'Syntax Error';
            if (statusText) statusText.innerText = 'ERROR';
        }
    }

    function renderResultDisplay(val) {
        if (!resultDisplay) return;

        if (typeof val !== 'number' || isNaN(val) || !isFinite(val)) {
            resultDisplay.innerText = isNaN(val) ? 'Domain Error' : (!isFinite(val) ? '∞ Tak Terhingga' : '0');
            return;
        }

        if (isDMSOutput) {
            let absVal = Math.abs(val);
            let deg = Math.floor(absVal);
            let minFloat = (absVal - deg) * 60;
            let min = Math.floor(minFloat);
            let sec = ((minFloat - min) * 60).toFixed(2);

            if (parseFloat(sec) >= 60) {
                sec = '0.00';
                min += 1;
            }
            if (min >= 60) {
                min = 0;
                deg += 1;
            }

            let sign = val < 0 ? '-' : '';
            resultDisplay.innerHTML = `${sign}${deg}&deg; ${min}' ${sec}"`;
        } else {
            if (Number.isInteger(val)) {
                resultDisplay.innerText = val.toString();
            } else {
                let formatted = val.toFixed(12).replace(/\.?0+$/, "");
                resultDisplay.innerText = formatted;
            }
        }
    }

    // Support Input Keyboard & Shortkeys
    document.addEventListener('keydown', function(event) {
        const key = event.key;

        // Shortkeys Trigonometri
        if (key === 's') { event.preventDefault(); insertAtCursor('sin '); }
        else if (key === 'S') { event.preventDefault(); insertAtCursor('asin '); }
        else if (key === 'c') { event.preventDefault(); insertAtCursor('cos '); }
        else if (key === 'C') { event.preventDefault(); insertAtCursor('acos '); }
        else if (key === 't') { event.preventDefault(); insertAtCursor('tan '); }
        else if (key === 'T') { event.preventDefault(); insertAtCursor('atan '); }
        
        // Shortkeys DMS Khusus: Derajat (d), Menit ('), Detik (")
        else if (key === 'd' || key === 'D') { event.preventDefault(); insertAtCursor(DEG_SYM); }
        else if (key === "'") { event.preventDefault(); insertAtCursor("'"); }
        else if (key === '"') { event.preventDefault(); insertAtCursor('"'); }
        
        // Navigasi & Karakter Umum
        else if (key === 'ArrowLeft') { event.preventDefault(); moveCursorLeft(); }
        else if (key === 'ArrowRight') { event.preventDefault(); moveCursorRight(); }
        else if (key === 'Home') { event.preventDefault(); cursorPos = 0; updateDisplay(); }
        else if (key === 'End') { event.preventDefault(); cursorPos = formula.length; updateDisplay(); }
        else if (/[0-9]/.test(key)) insertAtCursor(key);
        else if (key === '.') insertAtCursor('.');
        else if (key === '+') insertAtCursor('+');
        else if (key === '-') insertAtCursor('-');
        else if (key === '*') { event.preventDefault(); insertAtCursor('\u00D7'); }
        else if (key === '/') { event.preventDefault(); insertAtCursor('\u00F7'); }
        else if (key === '(') insertAtCursor('(');
        else if (key === ')') insertAtCursor(')');
        else if (key === '^') insertAtCursor('^');
        else if (key === 'Enter' || key === '=') { event.preventDefault(); calculate(); }
        else if (key === 'Backspace') backspace();
        else if (key === 'Escape') clearAll();
    });

    // Expose Global Public Functions for Inline Onclick Handlers
    window.toggleDegRad = toggleDegRad;
    window.toggleResultFormat = toggleResultFormat;
    window.moveCursorLeft = moveCursorLeft;
    window.moveCursorRight = moveCursorRight;
    window.insertAtCursor = insertAtCursor;
    window.appendDMS = appendDMS;
    window.clearAll = clearAll;
    window.backspace = backspace;
    window.calculate = calculate;

    return {
        toggleDegRad,
        toggleResultFormat,
        moveCursorLeft,
        moveCursorRight,
        insertAtCursor,
        appendDMS,
        clearAll,
        backspace,
        calculate
    };
})();
