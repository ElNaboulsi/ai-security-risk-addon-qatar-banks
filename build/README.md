# Building the add-on

The workbook, the guidance and the quick guide are generated from one data file, `content.py`. Edit the data there, then rebuild.

## Requirements

- Python 3.10 or later, with `pip install -r requirements.txt` (openpyxl)
- Node.js 18 or later, with `npm install` in this folder (the `docx` package)
- LibreOffice (to recalculate the workbook and to convert the guides to PDF)

## Steps

Run from this `build` folder:

```bash
mkdir -p out

# 1. Workbook
python3 build.py out/AI_Security_Risk_Addon_Banks_Qatar.xlsx

# 2. Guidance and quick guide (.docx)
python3 guide.py && node build_doc.js guide.js out/AI_Security_Risk_Addon_Banks_Qatar_Guidance.docx
python3 quick.py && node build_doc.js quick.js out/AI_Security_Risk_Addon_Quick_Guide.docx
python3 strip_comments.py out/AI_Security_Risk_Addon_Banks_Qatar_Guidance.docx out/AI_Security_Risk_Addon_Quick_Guide.docx

# 3. PDFs
cd out && soffice --headless --convert-to pdf AI_Security_Risk_Addon_Banks_Qatar_Guidance.docx AI_Security_Risk_Addon_Quick_Guide.docx
```

The workbook is written with formulas only; open it in LibreOffice Calc (or another spreadsheet program) and save it once so the calculated values are stored. `fixapp.py <file>` clears the application name from a file's properties.

## Files

| File | Purpose |
|---|---|
| `content.py` | All add-on data: assets, threats, vulnerabilities, scenarios, controls, requirements, calendar, governance settings and texts |
| `build.py` | Builds the workbook |
| `guide.py`, `quick.py` | Write the guide contents as `guide.js` and `quick.js` |
| `build_doc.js` | Turns `guide.js` / `quick.js` into .docx |
| `strip_comments.py` | Removes an empty comments part from the .docx files |
| `fixapp.py` | Clears the application name in a file's properties |

The source texts used for checking (QCB, NCSA, ISO, OWASP) are not included: obtain them from the issuers. NIA v2.1 statements are referenced by number and baseline flag only.
