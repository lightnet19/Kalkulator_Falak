import os, json, re

BASE = r"c:\Projects\Kalkulator_Falak"
DOCS = os.path.join(BASE, "docs")

DEVELOPER = "Fuad Baid\u0101w\u012b Al-Fajri"
ORIGINAL_ORG = "Lembaga Falakiyah MWCNU Wuluhan Jember"
CREDIT_LINE = f"Dikembangkan oleh **{DEVELOPER}**, berdasarkan aplikasi yang dibuat oleh {ORIGINAL_ORG}."

results = []

# ─────────────────────────────────────────────────────────────────────────────
# 1. package.json — update "author" field
# ─────────────────────────────────────────────────────────────────────────────
pkg_path = os.path.join(BASE, "package.json")
with open(pkg_path, "r", encoding="utf-8") as f:
    pkg = json.load(f)

pkg["author"] = {
    "name": DEVELOPER,
    "role": "Pengembang Aplikasi"
}
pkg["description"] = (
    f"Kalkulator Falak - dikembangkan oleh {DEVELOPER}, "
    f"berdasarkan aplikasi {ORIGINAL_ORG}"
)
# Tambahkan field contributors
pkg["contributors"] = [
    {
        "name": ORIGINAL_ORG,
        "role": "Pembuat Aplikasi Asal"
    }
]

with open(pkg_path, "w", encoding="utf-8") as f:
    json.dump(pkg, f, indent=2, ensure_ascii=False)
results.append(f"UPDATED: {pkg_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 2. index.html — tambahkan meta author + komentar di <head>
# ─────────────────────────────────────────────────────────────────────────────
html_path = os.path.join(BASE, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Tambahkan meta author setelah <meta charset=...>
meta_author = (
    f'    <meta name="author" content="{DEVELOPER}">\n'
    f'    <meta name="description" content="Kalkulator Falak — dikembangkan oleh {DEVELOPER}, '
    f'berdasarkan aplikasi {ORIGINAL_ORG}">\n'
)
html = html.replace(
    '    <meta charset="UTF-8">\n',
    f'    <meta charset="UTF-8">\n{meta_author}'
)

# Tambahkan komentar kredit di atas </body>
credit_comment = (
    f'\n    <!-- ═══════════════════════════════════════════════════════════\n'
    f'         Kalkulator Falak\n'
    f'         Dikembangkan oleh : {DEVELOPER}\n'
    f'         Berdasarkan aplikasi dari : {ORIGINAL_ORG}\n'
    f'         Versi : 1.0.0\n'
    f'         ═══════════════════════════════════════════════════════════ -->\n'
)
html = html.replace('</body>', credit_comment + '</body>')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
results.append(f"UPDATED: {html_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 3. README.md — tambahkan section Kredit & Pengembang
# ─────────────────────────────────────────────────────────────────────────────
readme_path = os.path.join(BASE, "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

kredit_section = f"""
## Kredit & Pengembang

| Peran | Nama / Lembaga |
|-------|----------------|
| **Pengembang Aplikasi** | {DEVELOPER} |
| **Pembuat Aplikasi Asal** | {ORIGINAL_ORG} |

Aplikasi ini dikembangkan oleh **{DEVELOPER}** sebagai pengembangan dan penyempurnaan
dari aplikasi kalkulator falak yang telah dibuat oleh **{ORIGINAL_ORG}**.

---
"""

# Sisipkan sebelum section Lisensi
readme = readme.replace("## Lisensi\n", kredit_section + "## Lisensi\n")

# Update baris copyright di footer
readme = readme.replace(
    "MIT License — Copyright (c) 2026 Lembaga Falakiyah NU Wuluhan Jember",
    f"MIT License — Copyright (c) 2026 {DEVELOPER}\n\nBerdasarkan karya {ORIGINAL_ORG}."
)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)
results.append(f"UPDATED: {readme_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 4. README.txt — tambahkan info pengembang
# ─────────────────────────────────────────────────────────────────────────────
readmetxt_path = os.path.join(BASE, "README.txt")
with open(readmetxt_path, "r", encoding="utf-8") as f:
    txt = f.read()

dev_info = f"""PENGEMBANG
----------
Dikembangkan oleh : {DEVELOPER}
Berdasarkan karya : {ORIGINAL_ORG}

"""
txt = txt.replace("Versi: 1.0.0", dev_info + "Versi: 1.0.0")

with open(readmetxt_path, "w", encoding="utf-8") as f:
    f.write(txt)
results.append(f"UPDATED: {readmetxt_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 5. CHANGELOG.md — update header dan copyright
# ─────────────────────────────────────────────────────────────────────────────
cl_path = os.path.join(BASE, "CHANGELOG.md")
with open(cl_path, "r", encoding="utf-8") as f:
    cl = f.read()

# Update subtitle header
cl = cl.replace(
    "## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember",
    f"## Kalkulator Falak | Dikembangkan oleh {DEVELOPER}\n"
    f"> Berdasarkan aplikasi {ORIGINAL_ORG}"
)

# Tambahkan keterangan di bagian [1.0.0]
cl = cl.replace(
    "### Ketergantungan",
    f"### Kredit\n- Dikembangkan oleh: **{DEVELOPER}**\n"
    f"- Berdasarkan aplikasi asal dari: **{ORIGINAL_ORG}**\n\n"
    "### Ketergantungan"
)

with open(cl_path, "w", encoding="utf-8") as f:
    f.write(cl)
results.append(f"UPDATED: {cl_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 6. SECURITY.md — update nama lembaga/author
# ─────────────────────────────────────────────────────────────────────────────
sec_path = os.path.join(BASE, "SECURITY.md")
with open(sec_path, "r", encoding="utf-8") as f:
    sec = f.read()

sec = sec.replace(
    "## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember",
    f"## Kalkulator Falak | Dikembangkan oleh {DEVELOPER}"
)
sec = sec.replace(
    "**Email:** [email lembaga falakiyah]",
    f"**Pengembang:** {DEVELOPER}  \n**Email:** [email pengembang]"
)

with open(sec_path, "w", encoding="utf-8") as f:
    f.write(sec)
results.append(f"UPDATED: {sec_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 7. docs/PRD.md — update header PIC dan latar belakang
# ─────────────────────────────────────────────────────────────────────────────
prd_path = os.path.join(DOCS, "PRD.md")
with open(prd_path, "r", encoding="utf-8") as f:
    prd = f.read()

prd = prd.replace(
    "## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember",
    f"## Kalkulator Falak | Dikembangkan oleh {DEVELOPER}"
)
prd = prd.replace(
    "**PIC:** Lembaga Falakiyah NU Wuluhan Jember",
    f"**Pengembang:** {DEVELOPER}  \n**PIC / Pembuat Asal:** {ORIGINAL_ORG}"
)

# Update bagian latar belakang
old_lb = "Para ahli falak di lingkungan\nLembaga Falakiyah NU Wuluhan Jember membutuhkan alat kalkulator yang:"
new_lb = (f"Para ahli falak di lingkungan {ORIGINAL_ORG} membutuhkan alat kalkulator yang:\n\n"
          f"> Aplikasi ini dikembangkan oleh **{DEVELOPER}** sebagai penyempurnaan dari\n"
          f"> aplikasi asal yang dibuat oleh **{ORIGINAL_ORG}**.\n")
if old_lb in prd:
    prd = prd.replace(old_lb, new_lb)
else:
    # fallback: insert after the first occurrence of "Wuluhan Jember membutuhkan"
    prd = prd.replace(
        f"{ORIGINAL_ORG} membutuhkan alat kalkulator yang:",
        f"{ORIGINAL_ORG} membutuhkan alat kalkulator yang:\n\n"
        f"> Aplikasi ini dikembangkan oleh **{DEVELOPER}** sebagai penyempurnaan\n"
        f"> dari aplikasi asal yang dibuat oleh **{ORIGINAL_ORG}**.\n"
    )

with open(prd_path, "w", encoding="utf-8") as f:
    f.write(prd)
results.append(f"UPDATED: {prd_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 8. docs/DEVPLAN.md — update header
# ─────────────────────────────────────────────────────────────────────────────
dp_path = os.path.join(DOCS, "DEVPLAN.md")
with open(dp_path, "r", encoding="utf-8") as f:
    dp = f.read()

dp = dp.replace(
    "## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember",
    f"## Kalkulator Falak | Dikembangkan oleh {DEVELOPER}\n"
    f"> Berdasarkan aplikasi {ORIGINAL_ORG}"
)

with open(dp_path, "w", encoding="utf-8") as f:
    f.write(dp)
results.append(f"UPDATED: {dp_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 9. docs/DEVLOG.md — update header + entri kontributor
# ─────────────────────────────────────────────────────────────────────────────
dl_path = os.path.join(DOCS, "DEVLOG.md")
with open(dl_path, "r", encoding="utf-8") as f:
    dl = f.read()

dl = dl.replace(
    "## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember",
    f"## Kalkulator Falak | Dikembangkan oleh {DEVELOPER}\n"
    f"> Berdasarkan aplikasi {ORIGINAL_ORG}"
)
dl = dl.replace(
    "**Kontributor:** Tim Pengembang (dengan bantuan Antigravity AI)",
    f"**Kontributor:** {DEVELOPER} (dengan bantuan Antigravity AI)"
)
dl = dl.replace(
    "**Kontributor:** Tim Lembaga Falakiyah NU Wuluhan Jember",
    f"**Kontributor:** {ORIGINAL_ORG}"
)
# Tambahkan konteks pengembang di entri inisialisasi
dl = dl.replace(
    "#### Catatan:\n- Desain UI 3D kalkulator dinilai sangat bagus secara visual",
    f"#### Catatan:\n"
    f"- Aplikasi ini adalah karya asal {ORIGINAL_ORG}\n"
    f"- Selanjutnya dikembangkan dan disempurnakan oleh {DEVELOPER}\n"
    f"- Desain UI 3D kalkulator dinilai sangat bagus secara visual"
)

with open(dl_path, "w", encoding="utf-8") as f:
    f.write(dl)
results.append(f"UPDATED: {dl_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 10. docs/ARCHITECTURE.md — update header
# ─────────────────────────────────────────────────────────────────────────────
arch_path = os.path.join(DOCS, "ARCHITECTURE.md")
with open(arch_path, "r", encoding="utf-8") as f:
    arch = f.read()

arch = arch.replace(
    "## Kalkulator Falak | Lembaga Falakiyah NU Wuluhan Jember",
    f"## Kalkulator Falak | Dikembangkan oleh {DEVELOPER}\n"
    f"> Berdasarkan aplikasi {ORIGINAL_ORG}"
)

with open(arch_path, "w", encoding="utf-8") as f:
    f.write(arch)
results.append(f"UPDATED: {arch_path}")

# ─────────────────────────────────────────────────────────────────────────────
# 11. docs/laporan_analisis_kalkulator_falak.md
# ─────────────────────────────────────────────────────────────────────────────
lap_path = os.path.join(DOCS, "laporan_analisis_kalkulator_falak.md")
if os.path.exists(lap_path):
    with open(lap_path, "r", encoding="utf-8") as f:
        lap = f.read()

    lap = lap.replace(
        "> **Proyek:** Kalkulator Falak — Lembaga Falakiyah NU Wuluhan Jember",
        f"> **Proyek:** Kalkulator Falak\n"
        f"> **Pengembang:** {DEVELOPER}  \n"
        f"> **Berdasarkan karya:** {ORIGINAL_ORG}"
    )

    with open(lap_path, "w", encoding="utf-8") as f:
        f.write(lap)
    results.append(f"UPDATED: {lap_path}")
else:
    results.append(f"SKIP (not found): {lap_path}")

# ─────────────────────────────────────────────────────────────────────────────
# Hasil
# ─────────────────────────────────────────────────────────────────────────────
print("\n".join(results))
print(f"\nTotal: {len(results)} file diproses.")
