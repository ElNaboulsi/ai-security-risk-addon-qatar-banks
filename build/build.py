import sys, datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.worksheet.pagebreak import Break
import content as C

OUT = sys.argv[1] if len(sys.argv) > 1 else "out/AI_Security_Risk_Addon_Banks_Qatar.xlsx"
NAVY, MAROON, GREY, PH, EX, F = "1E2230", "8A1538", "EDEDED", "FCE4D6", "FFF2CC", "Arial"
thin = Side(style="thin", color="BFBFBF"); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
BANDFILL = {"Very Low": "A9D08E", "Low": "C6EFCE", "Medium": "FFEB9C", "High": "F8CBAD", "Severe": "E06666"}
LEVELFILL = {"Must": "F8CBAD", "Should": "FFEB9C", "May": "C6EFCE", "Mixed": "DDEBF7"}
STRFILL = {"REQUIRED": "F8CBAD", "CONDITIONAL": "FFEB9C", "RECOMMENDED": "DDEBF7", "GOOD PRACTICE": "EDEDED"}
fill = lambda c: PatternFill("solid", fgColor=c)
wb = Workbook(); wb.remove(wb.active)
R0 = 5; N = 200

def new(name, tab=NAVY):
    ws = wb.create_sheet(name); ws.sheet_properties.tabColor = tab; ws.sheet_view.showGridLines = False
    ws.page_setup.orientation = "landscape"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0; ws.sheet_properties.pageSetUpPr.fitToPage = True
    return ws
def title(ws, t, sub, width):
    ws.cell(1, 1, t).font = Font(name=F, size=15, bold=True, color=NAVY); ws.row_dimensions[1].height = 24
    c = ws.cell(2, 1, sub); c.font = Font(name=F, size=9, italic=True, color="595959"); c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(width, 4)); ws.row_dimensions[2].height = 40
def header(ws, row, cols, start=1):
    for j, (h, w) in enumerate(cols, start):
        c = ws.cell(row, j, h); c.font = Font(name=F, size=10, bold=True, color="FFFFFF"); c.fill = fill(NAVY); c.border = BOX
        c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
        if w: ws.column_dimensions[L(j)].width = w
    ws.row_dimensions[row].height = 46
def cell(ws, r, c, v, calc=False, bold=False, fc=None, h=None, fmt=None, small=False):
    x = ws.cell(r, c, v); x.font = Font(name=F, size=9 if small else 10, bold=bold); x.border = BOX
    x.alignment = Alignment(wrap_text=True, vertical="top", horizontal=h)
    if calc: x.fill = fill(GREY)
    if fc: x.fill = fill(fc)
    if fmt: x.number_format = fmt
    return x
def section(ws, r, t):
    ws.cell(r, 1, t).font = Font(name=F, size=12, bold=True, color=MAROON); ws.row_dimensions[r].height = 20
def dv_list(ws, items_ref, rng):
    v = DataValidation(type="list", formula1=items_ref, allow_blank=True, showErrorMessage=True, errorStyle="stop", errorTitle="Not in the list", error="Choose a value from the drop-down list."); ws.add_data_validation(v); v.add(rng)
def status_cf(ws, rng, good, mid, bad):
    for t, c in ((good, "C6EFCE"), (mid, "FFEB9C"), (bad, "F8CBAD")):
        ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{t}"'], fill=fill(c)))
def band_cf(ws, rng):
    for b, c in BANDFILL.items():
        ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{b}"'], fill=fill(c), font=Font(name=F, bold=True)))
def table(ws, cols, rows, wrapcols=(), heights=None, small=False):
    header(ws, 4, cols)
    for i, row in enumerate(rows):
        for j, v in enumerate(row, 1): cell(ws, R0 + i, j, v, small=small)
        if heights: ws.row_dimensions[R0 + i].height = heights(row)
    ws.freeze_panes = "B5"

# ------------------------------------------------------------------ lists (hidden; referenced by validations)
LISTS = {"yn": [C.YES, C.NO], "req": C.STATUS_REQ, "imp": C.STATUS_IMP, "bands": C.BANDS, "clev": ["C0 Public", "C1 Internal", "C2 Restricted", "C3 Secret / Confidential", "C4 Top Secret"],
         "ilev": ["I0", "I1", "I2", "I3"], "alev": ["A0", "A1", "A2", "A3"], "assets": [a[0] for a in C.ASSETS], "areas": C.AREAS,
         "treat": ["Avoid", "Mitigate", "Accept", "Transfer", "Tolerate"], "rstat": ["Open", "In progress", "Closed"]}
LREF = {k: f"=Lists!${L(i)}$2:${L(i)}${len(v)+1}" for i, (k, v) in enumerate(LISTS.items(), 1)}

# ------------------------------------------------------------------ 0 Start Here
ws = new("Start Here", MAROON)
ws.column_dimensions["A"].width = 30; ws.column_dimensions["B"].width = 110
ws.cell(1, 1, C.TITLE).font = Font(name=F, size=20, bold=True, color=NAVY); ws.row_dimensions[1].height = 32
ws.cell(2, 1, C.VERSION).font = Font(name=F, size=10, italic=True, color="595959")
c = ws.cell(4, 1, C.ADVISORY); c.font = Font(name=F, size=10, bold=True, color=MAROON); c.fill = fill("F7E8EC"); c.alignment = Alignment(wrap_text=True, vertical="center")
ws.merge_cells("A4:B4"); ws.row_dimensions[4].height = 48
c = ws.cell(5, 1, C.NOTICE); c.font = Font(name=F, size=9, italic=True, color="595959"); c.alignment = Alignment(wrap_text=True, vertical="center"); ws.merge_cells("A5:B5"); ws.row_dimensions[5].height = 26
r = 6; section(ws, r, "Purpose"); r += 1
for t in ["This add-on is for banks in Qatar that already run an information security risk management process based on ISO/IEC 27001, ISO/IEC 27005 and ISO 31000.",
          "It adds two things on top of that process: AI security risk content (assets, threats, vulnerabilities, scenarios, controls, indicators and triggers), and the requirements a bank must meet for AI under QCB regulations, Qatari law and NCSA publications.",
          "The bank keeps its own method, scales, register and tools. Nothing here needs to be rebuilt."]:
    x = ws.cell(r, 1, t); x.font = Font(name=F, size=10); x.alignment = Alignment(wrap_text=True); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2); ws.row_dimensions[r].height = 30; r += 1
r += 1; section(ws, r, "Three steps"); r += 1
for a, b in [("1. Add AI content", "Add AI asset types (1) to the asset inventory or IAR; use threats (2), vulnerabilities (3) and scenarios (4) in the existing register; select AI controls (5) into the Statement of Applicability; adopt indicators (6) and triggers (7); add the minimum fields (8)."),
             ("2. Map ratings to national bands", "Map the bank's own rating labels to the national EISRMF bands in 9B so that High and Severe risks are identified and reported to NCSA consistently."),
             ("3. Evidence compliance", "Record status and evidence against QCB requirements (9A), national requirements (9B), NIA for AI (5A, 5B) and laws (9C); track submissions (10); report status (11).")]:
    cell(ws, r, 1, a, bold=True, fc="EEF1F6"); cell(ws, r, 2, b); ws.row_dimensions[r].height = 34; r += 1
r += 1; section(ws, r, "Sheets"); r += 1
SHEETS = [("0 Essentials", "13 mandatory actions to start with, each linked to the detailed sheets (E12 also includes the QCB 'should' timeframes of Incident Reporting Guideline 6.2)."), ("1 AI Asset Types", "AI assets to add to the asset inventory, with classification guidance and fields."), ("2 AI Threats", "AI-specific threats with OWASP LLM and Agentic Top 10 (2026) references."),
          ("3 AI Vulnerabilities", "Weaknesses that enable the threats, how to detect them and the controls that fix them."),
          ("4 Risk Scenarios", f"{len(C.SCEN)} asset-based scenarios (ISO/IEC 27005) to copy into the existing register; rate with the bank's scale, national band calculated."),
          ("5 AI Controls", "31 controls with ISO/IEC 27001, ISO/IEC 42001, NIA v2.1 (baseline shown), QCSF, QCB and Technology Risks references; SoA columns."),
          ("5A NIA by AI System", "Which NIA controls each AI system needs, from its C, I and A ratings (NIA v2.1, 2.3)."),
          ("5B NIA for AI", "All 356 NIA v2.1 statements (166 baseline) with how each applies to AI assets; status and evidence."),
          ("6 KRIs and KPIs", "AI risk and performance indicators with thresholds; status calculated."), ("7 Inputs and Triggers", "Inputs that feed the register, reassessment times, escalation, and where to record each one."),
          ("8 Fields to Add", "Minimum fields to add to the existing register and inventory, with the requirement behind each."),
          ("8A Governance Settings", "For each national band: the bank's approver and acceptance period, with the EISRMF meaning and NCSA reporting; risk appetite for each consequence area; decision-making authority (EISRMF Figure 3)."),
          ("8B Risk Acceptance Log", "One row per accepted risk: risk owner, approver check against 8A, review date and status calculated (ISO/IEC 27001 6.1.3)."),
          ("9A QCB Requirements", f"AI Guideline ({len(C.QCB_AI)} rows), Cloud Computing ({sum(1 for q in C.QCB_CD if q['id'].startswith('CL'))}), Data Handling and Protection ({sum(1 for q in C.QCB_CD if q['id'].startswith('DH'))}) and Incident Reporting Guideline ({len(C.QCB_IR)}) obligations relevant to AI; status and evidence."),
          ("9B National Requirements", "NCSA requirements (EISRMF, NISRMF, NIA, Data Classification Policy, ECCMF) plus the QCSF (good practice), with source wording and strength; scale mapping; register crosswalk."),
          ("9C Laws", "Laws relevant to AI use in banks."), ("10 Reporting Calendar", "Submissions to NCSA and QCB with due dates; how QCB and NCSA severity scales relate."),
          ("11 Compliance Summary", "Status counts across the requirement sheets."), ("References", "Sources and their status; open points to confirm.")]
for a, b in SHEETS:
    cell(ws, r, 1, a, bold=True); cell(ws, r, 2, b); ws.row_dimensions[r].height = 22; r += 1
r += 1; section(ws, r, "Requirement strength"); r += 1
for k, v in C.STRENGTH.items():
    cell(ws, r, 1, k, bold=True, fc=STRFILL[k]); cell(ws, r, 2, v); r += 1
cell(ws, r, 1, "QCB level", bold=True); cell(ws, r, 2, "QCB rows keep the regulation's own wording: Must, Should, May, or Mixed. Mixed rows contain at least one 'must' clause; the 'Wording by clause' column in 9A shows which clauses are not 'must'. The DHP states that 'must' is obligatory and 'may' is advisory (DHP 3)."); ws.row_dimensions[r].height = 30; r += 2
section(ws, r, "Cell colours"); r += 1
for a, b, fc in [("Orange", "To be completed by the bank.", PH), ("Grey", "Calculated, or fixed text from a published source.", GREY), ("Yellow ID", "Example row; replace or delete.", EX)]:
    cell(ws, r, 1, a, bold=True, fc=fc); cell(ws, r, 2, b); r += 1
r += 1; section(ws, r, "Where to start: three layers"); r += 1
for a, b in [("1. Essentials", "Sheet '0 Essentials': 13 actions whose source wording is mandatory (QCB 'must', NCSA REQUIRED or NIA baseline); E12 also includes the QCB 'should' timeframes of Incident Reporting Guideline 6.2. Start here."),
             ("2. Working sheets", "Sheets 1-8 and 10: content to load into the existing register, inventory, SoA and calendar. Fields and calendar rows are tagged Essential or Recommended; scenarios and controls show whether they link to mandatory QCB requirements."),
             ("3. Reference", "Sheets 5B, 9A, 9B and 9C: the full requirement detail, for evidence and audit. Status is recorded there; nothing in them is optional because it is in the reference layer.")]:
    cell(ws, r, 1, a, bold=True, fc="EEF1F6"); cell(ws, r, 2, b); ws.row_dimensions[r].height = 30; r += 1

# ------------------------------------------------------------------ 0 essentials
ws = new("0 Essentials", "C00000")
title(ws, "Essentials: start here", "Rule: an action is listed only if its source uses mandatory wording (QCB 'must', NCSA REQUIRED, NIA baseline), except E12 (see the note below). Everything else in the add-on is Recommended or Reference. Status here summarises the detailed rows in the sheets shown; the full requirement text and evidence sit in 9A and 9B.", 10)
header(ws, 4, [("ID", 6), ("Action", 52), ("Source", 26), ("Source wording", 12), ("Detailed rows (9A / 9B)", 16), ("Where in the add-on (sheets)", 16), ("Status", 14), ("Owner", 14), ("Target date", 11), ("Evidence", 22)])
NATS = {n[0]: n[5] for n in C.NAT}
for i, e in enumerate(C.ESSENTIALS):
    r = R0 + i
    lv = sorted({("Must" if C.QCB_ROW[x]["level"] in ("Must", "Mixed") else C.QCB_ROW[x]["level"]) for x in e[3]} | {NATS[x] for x in e[4]})
    assert all(v in ("Must", "REQUIRED") for v in lv) or (e[0] == "E12" and set(lv) <= {"Must", "REQUIRED", "Should"}), (e[0], lv)  # E12: IR03 (6.2 timeframes, should) linked as the stated exception
    for j, v in enumerate([e[0], e[1], e[2], " / ".join(lv), ", ".join(e[3] + e[4]), e[5]], 1): cell(ws, r, j, v, bold=j in (1, 2))
    for j in (7, 8, 9, 10): cell(ws, r, j, None, fc=PH, fmt="yyyy-mm-dd" if j == 9 else None)
    ws.row_dimensions[r].height = 44
ee = R0 + len(C.ESSENTIALS) - 1
dv_list(ws, LREF["req"], f"G{R0}:G{ee}"); status_cf(ws, f"G{R0}:G{ee}", C.STATUS_REQ[0], C.STATUS_REQ[1], C.STATUS_REQ[2])
_ve = DataValidation(type="date", operator="greaterThan", formula1="DATE(2000,1,1)", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter a date."); ws.add_data_validation(_ve); _ve.add(f"I{R0}:I{ee}")
x = ws.cell(ee + 2, 1, "E12 combines QCB 'must' duties (Hotline first, final report, monthly report) with the 'should' reporting timeframes of 6.2; both are shown in 10. Essentials do not replace the full requirement rows: every REQUIRED and Must row in 9A and 9B still applies."); x.font = Font(name=F, size=9, italic=True)
ws.merge_cells(start_row=ee + 2, start_column=1, end_row=ee + 2, end_column=10); x.alignment = Alignment(wrap_text=True); ws.row_dimensions[ee + 2].height = 30
ws.freeze_panes = "C5"

# ------------------------------------------------------------------ 1 assets
ws = new("1 AI Asset Types")
title(ws, "AI asset types to add to the asset inventory / Information Asset Register", "Asset-based approach (ISO/IEC 27005). AI components are usually secondary (supporting) assets; record the primary process and information assets they support. Rate every AI asset under the National Data Classification Policy (NIA v2.1, 2.3 a).", 8)
table(ws, [("ID", 7), ("AI asset type", 24), ("Description", 40), ("Banking examples", 34), ("Primary / secondary", 14), ("Classification guidance", 40), ("Inventory fields to add", 32), ("Typical owner", 18)],
      C.ASSETS, heights=lambda r: 58)

# ------------------------------------------------------------------ 2 threats
ws = new("2 AI Threats")
title(ws, "AI threat catalogue", "OWASP entry given where the OWASP Top 10 for LLM Applications 2026 (LLM01-LLM10) or the OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10) covers the threat. '-' = not an entry in either list.", 6)
table(ws, [("ID", 7), ("Threat", 26), ("Description", 44), ("Affected asset types", 20), ("OWASP Top 10 reference (2026)", 26), ("Banking example", 48)],
      [(t[0], t[1], t[2], t[3], t[4], C.THREAT_EX[t[0]]) for t in C.THREATS], heights=lambda r: 36)

# ------------------------------------------------------------------ 3 vulnerabilities
ws = new("3 AI Vulnerabilities")
title(ws, "AI vulnerability catalogue", "Weaknesses that allow the threats in sheet 2, how to detect them, and the controls in sheet 5 that address them.", 5)
table(ws, [("ID", 7), ("Vulnerability", 46), ("Enables threats", 16), ("How to detect", 44), ("Controls (sheet 5)", 18)], C.VULNS, heights=lambda r: 32)

# ------------------------------------------------------------------ 9B is referenced by 4: compute mapping position first
NAT_END = R0 + len(C.NAT) - 1
MAP0 = NAT_END + 4      # first mapping row
MAPN = 8
MAPREF = f"'9B National Requirements'!$A${MAP0}:$B${MAP0 + MAPN - 1}"
MAPLAB = f"='9B National Requirements'!$A${MAP0}:$A${MAP0 + MAPN - 1}"

# ------------------------------------------------------------------ 8A positions (referenced by 4 and 8B)
GA0 = 6; GAE = GA0 + len(C.BANDS) - 1              # bands
GB0 = GAE + 5; GBE = GB0 + len(C.AREAS) - 1         # tolerance by area
GC0 = GBE + 4                                       # decision levels
G8A = "'8A Governance Settings'"
GBANDS = f"{G8A}!$A${GA0}:$E${GAE}"; GTOL = f"{G8A}!$A${GB0}:$B${GBE}"
BRANK = LREF["bands"][1:]
ACC0, ACCN = R0, 100
ACCA = f"'8B Risk Acceptance Log'!$A${ACC0}:$A${ACC0 + ACCN - 1}"; ACCB = f"'8B Risk Acceptance Log'!$B${ACC0}:$B${ACC0 + ACCN - 1}"
def approver(ref):
    v = f"VLOOKUP({ref},{GBANDS},2,FALSE)"
    return f'IFERROR(IF(TRIM({v}&"")="","Set in 8A",{v}),"")'

# ------------------------------------------------------------------ 4 scenarios
ws = new("4 Risk Scenarios", MAROON)
title(ws, "Ready-made AI risk scenarios (ISO/IEC 27005 asset-based format)", "Copy the scenarios that apply into the existing register. Rate them with the bank's own scales (orange). The national band is looked up from the mapping in 9B (grey); High and Severe need out-of-band reporting to NCSA (EISRMF). Consequence areas: the six NISRMF national consequence dimensions plus legal and regulatory, financial, operational and reputation areas for the bank.", 20)
cols = [("ID", 7), ("Asset type", 8), ("Threat", 8), ("Vulnerability", 9), ("Risk scenario", 44), ("Consequences", 26), ("Main consequence area", 16), ("Suggested controls (sheet 5)", 14),
        ("NIA baseline (*) statements supported", 18), ("QCB requirements (sheet 9A)", 20), ("ISO/IEC 27001 Annex A (from controls)", 16), ("Applicable? (Yes/No)", 9), ("Risk owner", 14),
        ("Current rating (bank scale)", 11), ("National band (current)", 11), ("Out-of-band report to NCSA?", 10), ("Target residual rating (bank scale)", 11), ("National band (residual)", 11),
        ("Treatment", 11), ("Status", 10), ("Linked to a mandatory QCB clause? (Must or Mixed row)", 11),
        ("Approver for current band (8A), in addition to the risk owner", 16), ("Above the area's risk appetite? (8A)", 13), ("Latest acceptance record (8B)", 11),
        ("Treatment target date", 12), ("Treatment overdue? (High / Severe)", 11)]
header(ws, 4, cols)
def union(field, ctrls):
    out = []
    for c in ctrls:
        for t in [x.strip() for x in C.CTRL[c][field].replace(";", ",").split(",") if x.strip() and x.strip() != "-"]:
            if t not in out: out.append(t)
    return ", ".join(out) if out else "-"
for i, s in enumerate(C.SCEN):
    r = R0 + i; ctr = [x.strip() for x in s[7].split(",")]
    base = C.nia_compact(sorted({p for c in ctr for p in C.nia_expand(C.CTRL[c]["nia"]) if C.NIA_IDX[p]["base"]}))
    q = "; ".join(f"{x.strip()} ({C.QCB_ROW[x.strip()]['clauses']})" for x in s[8].split(",") if x.strip() != "-") or "-"
    vals = [s[0], s[1], s[2], s[3], s[4], s[5], C.AREAS[s[6]], s[7], base, q, union("iso27001", ctr)]
    for j, v in enumerate(vals, 1): cell(ws, r, j, v, small=j in (9, 10, 11))
    for j in (12, 13, 14, 17, 19, 20): cell(ws, r, j, None, fc=PH)
    cell(ws, r, 15, f'=IF(N{r}="","",IF(IFERROR(VLOOKUP(N{r},{MAPREF},2,FALSE)&"","")="","Map rating in 9B",VLOOKUP(N{r},{MAPREF},2,FALSE)))', calc=True, bold=True, h="center")
    cell(ws, r, 16, f'=IF(O{r}="","",IF(OR(O{r}="High",O{r}="Severe"),"{C.YES}",IF(ISNUMBER(MATCH(O{r},{LREF["bands"][1:]},0)),"{C.NO}","")))', calc=True, bold=True, h="center")
    cell(ws, r, 18, f'=IF(Q{r}="","",IF(IFERROR(VLOOKUP(Q{r},{MAPREF},2,FALSE)&"","")="","Map rating in 9B",VLOOKUP(Q{r},{MAPREF},2,FALSE)))', calc=True, bold=True, h="center")
    cell(ws, r, 21, C.scen_must(s), h="center")
    cell(ws, r, 22, f'=IF(O{r}="","",{approver(f"O{r}")})', calc=True)
    tol = f"VLOOKUP(G{r},{GTOL},2,FALSE)"
    cell(ws, r, 23, f'=IF(OR(O{r}="",NOT(ISNUMBER(MATCH(O{r},{BRANK},0)))),"",IF(TRIM(IFERROR({tol}&"",""))="","Set appetite in 8A",IFERROR(IF(MATCH(O{r},{BRANK},0)>MATCH({tol},{BRANK},0),"Above appetite","Within appetite"),"Set appetite in 8A")))', calc=True, bold=True, h="center")
    cell(ws, r, 24, f'=IF(COUNTIF({ACCB},A{r})=0,"",IFERROR(IF(LOOKUP(2,1/({ACCB}=A{r}),{ACCA})&""="","Row without ID",LOOKUP(2,1/({ACCB}=A{r}),{ACCA})&""),""))', calc=True, h="center")
    cell(ws, r, 25, None, fc=PH, fmt="yyyy-mm-dd")
    cell(ws, r, 26, f'=IF(NOT(ISNUMBER(Y{r})),"",IF(AND(OR(O{r}="High",O{r}="Severe"),T{r}<>"Closed",Y{r}<TODAY()),"Overdue",""))', calc=True, bold=True, h="center")
    ws.row_dimensions[r].height = 62
e = R0 + len(C.SCEN) - 1
dv_list(ws, LREF["yn"], f"L{R0}:L{e}"); dv_list(ws, MAPLAB, f"N{R0}:N{e}"); dv_list(ws, MAPLAB, f"Q{R0}:Q{e}")
dv_list(ws, LREF["treat"], f"S{R0}:S{e}"); dv_list(ws, LREF["rstat"], f"T{R0}:T{e}")
band_cf(ws, f"O{R0}:O{e}"); band_cf(ws, f"R{R0}:R{e}")
ws.conditional_formatting.add(f"P{R0}:P{e}", CellIsRule(operator="equal", formula=[f'"{C.YES}"'], fill=fill("F8CBAD"), font=Font(name=F, bold=True)))
ws.conditional_formatting.add(f"W{R0}:W{e}", CellIsRule(operator="equal", formula=['"Above appetite"'], fill=fill("F8CBAD"), font=Font(name=F, bold=True)))
ws.conditional_formatting.add(f"W{R0}:W{e}", CellIsRule(operator="equal", formula=['"Within appetite"'], fill=fill("C6EFCE")))
ws.conditional_formatting.add(f"Z{R0}:Z{e}", CellIsRule(operator="equal", formula=['"Overdue"'], fill=fill("F8CBAD"), font=Font(name=F, bold=True)))
dv_date = DataValidation(type="date", operator="greaterThan", formula1="DATE(2000,1,1)", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter a date."); ws.add_data_validation(dv_date); dv_date.add(f"Y{R0}:Y{e}")
ws.freeze_panes = "F5"; ws.auto_filter.ref = f"A4:Z{e}"

# ------------------------------------------------------------------ 5 controls
ws = new("5 AI Controls", MAROON)
title(ws, "AI control catalogue", "Select applicable controls into the Statement of Applicability (ISO/IEC 27001 6.1.3). NIA references cite NIA v2.1 statement numbers; the next column lists which are baseline (*), i.e. mandatory for assets rated 1 or above. QCSF names follow the Qatar 2022 Cybersecurity Framework (good practice).", 21)
cols = [("ID", 7), ("Scope", 10), ("Tier", 11), ("Control", 24), ("Objective", 28), ("What good looks like", 48), ("Evidence expected", 30), ("ISO/IEC 27001:2022 Annex A", 12), ("ISO/IEC 42001 Annex A", 12),
        ("NIA v2.1 statements", 14), ("of which baseline (*)", 14), ("QCSF capability", 24), ("QCB AI Guideline (9A IDs)", 16), ("QCB Cloud / Data / Incident (9A IDs)", 16),
        ("Technology Risks circular (2018) section", 13), ("Applicable? (Yes/No)", 11), ("Implementation status", 14), ("Evidence reference", 18), ("Owner", 14), ("Target date", 11), ("QCB rows with mandatory clauses supported (Must or Mixed)", 10)]
header(ws, 4, cols)
for i, c in enumerate(C.CONTROLS):
    r = R0 + i
    vals = [c["id"], c["scope"], c["tier"], c["name"], c["objective"], c["good"], c["evidence"], c["iso27001"], c["iso42001"], c["nia"], c["nia_base"], c["qcsf"], c["qai"], c["qcd"], c["trb"]]
    for j, v in enumerate(vals, 1): cell(ws, r, j, v, bold=j == 4, small=j >= 8)
    for j in range(16, 21): cell(ws, r, j, None, fc=PH, fmt="yyyy-mm-dd" if j == 20 else None)
    cell(ws, r, 21, C.ctrl_must(c), h="center")
    ws.row_dimensions[r].height = 92
e = R0 + len(C.CONTROLS) - 1
dv_list(ws, LREF["yn"], f"P{R0}:P{e}"); dv_list(ws, LREF["imp"], f"Q{R0}:Q{e}")
status_cf(ws, f"Q{R0}:Q{e}", C.STATUS_IMP[0], C.STATUS_IMP[1], C.STATUS_IMP[2])
ws.freeze_panes = "E5"; ws.auto_filter.ref = f"A4:U{e}"

# ------------------------------------------------------------------ 5A NIA by AI system
ws = new("5A NIA by AI System", MAROON)
title(ws, "NIA v2.1 control requirements for each AI system", "Enter each AI system's ratings under the National Data Classification Policy; the aggregate level follows the policy's classification matrix (Table 1); C4 is treated as High, because Table 1 stops at C3 and NIA 2.3 e covers C3 and higher. The sheet shows what NIA v2.1 section 2.3 requires: baseline (*) statements for assets rated 1 or above; additional controls per applicable domain for ratings of 2 (one or more) or 3 and above (two or more), chosen by risk assessment; implementation priority by aggregate level.", 10)
cols = [("AI-ID", 9), ("AI system", 30), ("AI asset type (sheet 1)", 12), ("Confidentiality", 18), ("Integrity", 9), ("Availability", 10), ("Aggregate level", 11),
        ("Baseline (*) statements required?", 30), ("Additional controls per applicable domain", 32), ("Implementation priority", 15)]
header(ws, 4, cols)
EX5A = C.EX5A
for k in range(50):
    r = R0 + k; ex = EX5A[k] if k < len(EX5A) else (None,) * 6
    for j, v in enumerate(ex, 1): cell(ws, r, j, v, fc=EX if (ex[0] and j == 1) else PH)
    ws.row_dimensions[r].height = 30
    n = lambda z: f"VALUE(MID({z}{r},2,1))"
    mx = f"MAX({n('D')},{n('E')},{n('F')})"
    ok = f'AND(LEFT(D{r},1)="C",{n("D")}<=4,LEFT(E{r},1)="I",{n("E")}<=3,LEFT(F{r},1)="A",{n("F")}<=3)'
    cell(ws, r, 7, f'=IFERROR(IF(OR(D{r}="",E{r}="",F{r}=""),"",IF(NOT({ok}),"Check rating",IF({mx}=0,"Not rated",IF(OR({n("D")}>=3,{n("E")}=3,{n("F")}=3),"High",IF({mx}=2,"Medium","Low"))))),"Check rating")', calc=True, bold=True, h="center")
    cell(ws, r, 8, f'=IF(OR(G{r}="",G{r}="Check rating"),"",IF(G{r}="Not rated","No - minimal controls may apply (NIA 2.3 b)",IF({mx}>=1,"Yes - all baseline (*) statements (sheet 5B)","No - minimal controls may apply")))', calc=True)
    cell(ws, r, 9, f'=IF(OR(G{r}="",G{r}="Check rating",G{r}="Not rated"),"",IF({mx}>=3,"Two or more per applicable domain, by risk assessment",IF({mx}=2,"One or more per applicable domain, by risk assessment","None required beyond baseline")))', calc=True)
    cell(ws, r, 10, f'=IF(OR(G{r}="",G{r}="Check rating",G{r}="Not rated"),"",IF(G{r}="High",1,IF(G{r}="Medium",2,3)))', calc=True, h="center")
e = R0 + 49
dv_list(ws, LREF["assets"], f"C{R0}:C{e}"); dv_list(ws, LREF["clev"], f"D{R0}:D{e}"); dv_list(ws, LREF["ilev"], f"E{R0}:E{e}"); dv_list(ws, LREF["alev"], f"F{R0}:F{e}")
for t, c_ in (("High", "F8CBAD"), ("Medium", "FFEB9C"), ("Low", "C6EFCE")):
    ws.conditional_formatting.add(f"G{R0}:G{e}", CellIsRule(operator="equal", formula=[f'"{t}"'], fill=fill(c_), font=Font(name=F, bold=True)))
ws.freeze_panes = "C5"

# ------------------------------------------------------------------ 5B NIA for AI
ws = new("5B NIA for AI", "7F7F7F")
title(ws, "Reference: NIA Standard v2.1 applied to AI assets", "All 356 control statements of NIA v2.1 (166 baseline), listed by statement number; read each statement in the NIA Standard v2.1 published by NCSA. Baseline (*) statements apply to every asset rated 1 or above, including assets rated 2, 3 and higher. For assets rated 2 or above, add controls from the other statements, chosen by risk assessment: one or more per applicable domain at rating 2, two or more at 3 and above (NIA v2.1, 2.3 c-e; see 5A). 'AI relevance' only guides attention; it never removes a baseline obligation.", 11)
cols = [("NIA ID", 11), ("Domain", 18), ("Sub-section", 16), ("Baseline (*)", 9), ("Applies to", 18), ("AI relevance", 9), ("How it applies to AI assets", 46),
        ("Add-on controls (sheet 5)", 12), ("Status for AI assets", 14), ("Evidence", 22)]
header(ws, 4, cols)
seen = {}
for i, o in enumerate(C.NIA):
    r = R0 + i; key = (o["dom"], o["n"]); seen[key] = seen.get(key, 0) + 1
    nid = f'{o["dom"]} {o["n"]}' + ((" (first)" if seen[key] == 1 else " (second)") if sum(1 for x in C.NIA if (x["dom"], x["n"]) == key) > 1 else "")
    rel, note = C.NIA_DOM_AI[o["dom"]]
    vals = [nid, o["domain"], o["sub"] or "-", C.YES if o["base"] else C.NO, "All assets rated 1 or above" if o["base"] else "Additional for assets rated 2 or above, if selected by risk assessment",
            rel, note, ", ".join(C.NIA_CTRL.get(key, [])) or "-"]
    for j, v in enumerate(vals, 1): cell(ws, r, j, v, small=True, bold=j == 1)
    cell(ws, r, 9, None, fc=PH); cell(ws, r, 10, None, fc=PH)
    ws.row_dimensions[r].height = 30
e = R0 + len(C.NIA) - 1
dv_list(ws, LREF["imp"], f"I{R0}:I{e}")
status_cf(ws, f"I{R0}:I{e}", C.STATUS_IMP[0], C.STATUS_IMP[1], C.STATUS_IMP[2])
ws.conditional_formatting.add(f"D{R0}:D{e}", CellIsRule(operator="equal", formula=[f'"{C.YES}"'], fill=fill("F8CBAD"), font=Font(name=F, bold=True)))
ws.freeze_panes = "B5"; ws.auto_filter.ref = f"A4:J{e}"

# ------------------------------------------------------------------ 6 KRIs and KPIs
ws = new("6 KRIs and KPIs")
title(ws, "AI key risk indicators (KRI) and key performance indicators (KPI)", "KRIs show changes in AI risk exposure; KPIs show how well AI controls work. Thresholds are suggestions to agree with the risk owner. Enter the current value; status is calculated.", 13)
cols = [("ID", 6), ("Type", 6), ("Indicator", 32), ("Formula", 40), ("Data source", 16), ("Frequency", 10), ("Amber", 9), ("Red", 9), ("Direction", 12), ("Linked scenarios / controls", 16),
        ("Current value (KPIs: 0-100, not %)", 12), ("Date", 11), ("Status", 9)]
header(ws, 4, cols)
for i, k in enumerate(C.KRIS):
    r = R0 + i
    vals = list(k[:8]) + ["Higher is worse" if k[8] == 0 else "Lower is worse", k[9]]
    for j, v in enumerate(vals, 1): cell(ws, r, j, v, h="center" if j in (7, 8) else None)
    for j in (7, 8):
        if isinstance(vals[j - 1], str): ws.cell(r, j).fill = fill(PH)
    cell(ws, r, 11, None, fc=PH); cell(ws, r, 12, None, fc=PH, fmt="yyyy-mm-dd")
    hw = f'IF(K{r}>=H{r},"Red",IF(AND(ISNUMBER(G{r}),K{r}>=G{r}),"Amber","Green"))'; lw = f'IF(K{r}<=H{r},"Red",IF(AND(ISNUMBER(G{r}),K{r}<=G{r}),"Amber","Green"))'
    cell(ws, r, 13, f'=IF(OR(K{r}="",NOT(ISNUMBER(H{r}))),"",IF(I{r}="Higher is worse",{hw},{lw}))', calc=True, bold=True, h="center")
    ws.row_dimensions[r].height = 40
e = R0 + len(C.KRIS) - 1
_vk = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter a number."); ws.add_data_validation(_vk)
_vp = DataValidation(type="decimal", operator="between", formula1="0", formula2="100", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter a percentage from 0 to 100 (for example 95, not 95%).", promptTitle="Percentage", prompt="Enter 0-100", showInputMessage=True); ws.add_data_validation(_vp)
for i_, k_ in enumerate(C.KRIS):
    (_vp if k_[1] == "KPI" else _vk).add(f"K{R0 + i_}"); _vk.add(f"G{R0 + i_}"); _vk.add(f"H{R0 + i_}")
_vl = DataValidation(type="date", operator="greaterThan", formula1="DATE(2000,1,1)", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter a date."); ws.add_data_validation(_vl); _vl.add(f"L{R0}:L{e}")
status_cf(ws, f"M{R0}:M{e}", "Green", "Amber", "Red")
ws.freeze_panes = "D5"

# ------------------------------------------------------------------ 7 triggers
ws = new("7 Inputs and Triggers")
title(ws, "Inputs that feed the register and trigger reassessment", "Log each input in the bank's existing risk input or incident process, decide whether it creates or updates a risk, and reassess within the time shown (placeholders). Deadlines set by NCSA or QCB take precedence.", 5)
table(ws, [("ID", 6), ("Input source", 30), ("AI examples", 44), ("Reassess within (days)", 11), ("Escalation and reporting", 60), ("Where to record it in the add-on", 44), ("Date to enter", 34)],
      [(t[0], t[1], t[2], t[3], t[4] or "-") + C.T7_RECORD[t[0]] for t in C.TRIGGERS], heights=lambda r: 32)
for i in range(len(C.TRIGGERS)): ws.cell(R0 + i, 4).fill = fill(PH); ws.cell(R0 + i, 4).alignment = Alignment(horizontal="center", vertical="top")

# ------------------------------------------------------------------ 8 fields
ws = new("8 Fields to Add")
title(ws, "Minimum fields to add to the existing register, inventory and incident records", "Add only what the existing templates lack. Each field is linked to the requirement that needs it.", 6)
table(ws, [("Field", 44), ("Add to", 13), ("Why", 38), ("Requirement source", 34), ("Strength", 14), ("Already in bank template? (Yes/No)", 12), ("Priority", 12)],
      [f + (None, C.FIELD_PRIORITY[f[4]]) for f in C.FIELDS], heights=lambda r: 30)
e = R0 + len(C.FIELDS) - 1
for i, f in enumerate(C.FIELDS):
    ws.cell(R0 + i, 5).fill = fill(STRFILL[f[4]]); ws.cell(R0 + i, 6).fill = fill(PH)
dv_list(ws, LREF["yn"], f"F{R0}:F{e}")

# ------------------------------------------------------------------ 8A governance settings
ws = new("8A Governance Settings", MAROON)
title(ws, "Governance settings: approval, response and risk appetite", "Orange cells are set by the bank; grey cells give published text (EISRMF, NISRMF) and are fixed. Sheets 4 and 8B use these settings to show the approver, the appetite check and acceptance review dates. The approver set here is in addition to the risk owner, who approves treatment and accepts residual risk (ISO/IEC 27001 6.1.3).", 5)
for j, w in enumerate([30, 40, 40, 24, 48], 1): ws.column_dimensions[L(j)].width = w
section(ws, GA0 - 2, "A. Approval and response by national band")
header(ws, GA0 - 1, [("National band", None), ("Approver for treatment and residual-risk acceptance, in addition to the risk owner (bank sets)", None), ("What the band means (EISRMF, Figure 5)", None), ("Maximum acceptance period, months (bank sets)", None), ("Reporting to NCSA (EISRMF; NISRMF)", None)])
for i, b in enumerate(C.BANDS):
    r = GA0 + i; cell(ws, r, 1, b, bold=True, fc=BANDFILL[b])
    cell(ws, r, 2, None, fc=PH); cell(ws, r, 3, C.EIS_BAND[b], calc=True); cell(ws, r, 4, None, fc=PH, h="center")
    cell(ws, r, 5, C.GOV_FIXED.get(b, "-"), calc=True); ws.row_dimensions[r].height = 30
x = ws.cell(GAE + 1, 1, C.GOV_EXAMPLE); x.font = Font(name=F, size=9, italic=True); x.alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells(start_row=GAE + 1, start_column=1, end_row=GAE + 1, end_column=5); ws.row_dimensions[GAE + 1].height = 30
v = DataValidation(type="whole", operator="between", formula1="1", formula2="120", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter whole months from 1 to 120."); ws.add_data_validation(v); v.add(f"D{GA0}:D{GAE}")
section(ws, GB0 - 2, "B. Risk appetite by consequence area")
header(ws, GB0 - 1, [("Consequence area", None), ("Highest acceptable band (bank sets)", None), ("Note", None)])
for i, a in enumerate(C.AREAS):
    r = GB0 + i; cell(ws, r, 1, a, bold=True); cell(ws, r, 2, None, fc=PH, h="center")
    cell(ws, r, 3, "National consequence dimension (NISRMF)" if i < 4 or i in (5, 6) else "Bank area", small=True)
dv_list(ws, LREF["bands"], f"B{GB0}:B{GBE}"); band_cf(ws, f"B{GB0}:B{GBE}")
x = ws.cell(GBE + 1, 1, C.APPETITE_NOTE); x.font = Font(name=F, size=9, italic=True); x.alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells(start_row=GBE + 1, start_column=1, end_row=GBE + 1, end_column=5); ws.row_dimensions[GBE + 1].height = 30
ws.row_breaks.append(Break(id=GC0 - 3))
section(ws, GC0 - 2, "C. Decision-making authority")
header(ws, GC0 - 1, [("Level", None), ("EISRMF (Figure 3)", None), ("Typical decisions (example)", None), ("Who in the bank (bank sets)", None)])
for i, (a, b, c_) in enumerate(C.GOV_LEVELS):
    r = GC0 + i; cell(ws, r, 1, a, bold=True); cell(ws, r, 2, b, calc=True); cell(ws, r, 3, c_); cell(ws, r, 4, None, fc=PH); ws.row_dimensions[r].height = 30
x = ws.cell(GC0 + len(C.GOV_LEVELS), 1, C.COMMITTEE_NOTE); x.font = Font(name=F, size=9, italic=True); x.alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells(start_row=GC0 + len(C.GOV_LEVELS), start_column=1, end_row=GC0 + len(C.GOV_LEVELS), end_column=5); ws.row_dimensions[GC0 + len(C.GOV_LEVELS)].height = 30
x = ws.cell(GC0 + len(C.GOV_LEVELS) + 2, 1, C.GOV_FOOTER); x.font = Font(name=F, size=9, italic=True, bold=True)
ws.merge_cells(start_row=GC0 + len(C.GOV_LEVELS) + 2, start_column=1, end_row=GC0 + len(C.GOV_LEVELS) + 2, end_column=5)

# ------------------------------------------------------------------ 8B risk acceptance log
ws = new("8B Risk Acceptance Log", MAROON)
title(ws, "Risk acceptance log", "One row per accepted risk. The risk owner approves the treatment plan and accepts the residual risk (ISO/IEC 27001 6.1.3); the approver required by 8A for the band is in addition to the risk owner. 'Check' means the approver role recorded differs from 8A. 'Incomplete' means the risk owner, the date the risk owner accepted, the approver (in 8A or on the row), the band or the acceptance period is missing. Row RA-01 is an example; replace or delete it.", 14)
header(ws, 4, [("Acceptance ID", 11), ("Scenario / risk ID", 11), ("National band at acceptance", 12), ("Risk owner", 18), ("Date risk owner accepted", 12), ("Approver required (8A)", 20),
               ("Approver role recorded", 22), ("Approver check", 10), ("Approver name", 18), ("Date approved", 12), ("Review date", 12), ("Rationale", 32), ("Conditions / compensating controls", 32), ("Status", 14)])
BOK = f"ISNUMBER(MATCH(C{{r}},{BRANK},0))"
for k in range(ACCN):
    r = ACC0 + k; ex = C.ACC_EXAMPLE if k == 0 else (None,) * 10
    dmy = lambda d: dt.datetime.strptime(d, "%Y-%m-%d") if d else None
    vals = {1: ex[0], 2: ex[1], 3: ex[2], 4: ex[3], 5: dmy(ex[4]), 7: ex[5], 9: ex[6], 10: dmy(ex[7]), 12: ex[8], 13: ex[9]}
    for j, v_ in vals.items(): cell(ws, r, j, v_, fc=EX if (k == 0 and j == 1) else PH, fmt="yyyy-mm-dd" if j in (5, 10) else None)
    bok = BOK.format(r=r)
    cell(ws, r, 6, f'=IF(C{r}="","",IF(NOT({bok}),"Check band",{approver(f"C{r}")}))', calc=True)
    cell(ws, r, 8, f'=IF(F{r}="","",IF(OR(F{r}="Set in 8A",F{r}="Check band"),F{r},IF(TRIM(G{r}&"")="","Missing",IF(TRIM(G{r})=TRIM(F{r}),"OK","Check"))))', calc=True, bold=True, h="center")
    per = f"VLOOKUP(C{r},{GBANDS},4,FALSE)"
    cell(ws, r, 11, f'=IF(OR(C{r}="",J{r}=""),"",IF(NOT({bok}),"Check band",IFERROR(IF(ISNUMBER({per}),EDATE(J{r},{per}),"Set period in 8A"),"Set period in 8A")))', calc=True, fmt="yyyy-mm-dd", h="center")
    cell(ws, r, 14, f'=IF(AND(C{r}="",J{r}=""),"",IF(OR(TRIM(D{r}&"")="",NOT(ISNUMBER(E{r})),NOT(ISNUMBER(K{r})),H{r}="Missing",H{r}="Set in 8A"),"Incomplete",IF(K{r}<TODAY(),"Expired",IF(K{r}-TODAY()<=30,"Due within 30 days","Active"))))', calc=True, bold=True, h="center")
e = ACC0 + ACCN - 1
dv_list(ws, LREF["bands"], f"C{ACC0}:C{e}"); band_cf(ws, f"C{ACC0}:C{e}")
dvd = DataValidation(type="date", operator="greaterThan", formula1="DATE(2000,1,1)", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter a date."); ws.add_data_validation(dvd); dvd.add(f"E{ACC0}:E{e}"); dvd.add(f"J{ACC0}:J{e}")
status_cf(ws, f"N{ACC0}:N{e}", "Active", "Due within 30 days", "Expired")
ws.conditional_formatting.add(f"N{ACC0}:N{e}", CellIsRule(operator="equal", formula=['"Incomplete"'], fill=fill("FFEB9C")))
ws.conditional_formatting.add(f"H{ACC0}:H{e}", CellIsRule(operator="equal", formula=['"Check"'], fill=fill("F8CBAD"), font=Font(name=F, bold=True)))
ws.conditional_formatting.add(f"H{ACC0}:H{e}", CellIsRule(operator="equal", formula=['"Missing"'], fill=fill("F8CBAD"), font=Font(name=F, bold=True)))
ws.conditional_formatting.add(f"H{ACC0}:H{e}", CellIsRule(operator="equal", formula=['"OK"'], fill=fill("C6EFCE")))
ws.freeze_panes = "C5"

# ------------------------------------------------------------------ 9A QCB
ws = new("9A QCB Requirements", "7030A0")
title(ws, "Reference: QCB requirements relevant to AI", "AI Guideline (in force 4 September 2024), Cloud Computing Regulation (in force 15 April 2024), Data Handling and Protection Regulation (effective 16 February 2025) and Incident Reporting Guideline (2024; exact date to confirm), verified against the texts. Requirements are paraphrased; QCB's text prevails. Level uses the regulation's own wording.", 12)
cols = [("ID", 7), ("Regulation", 14), ("Section", 9), ("Topic", 18), ("Requirement (paraphrase)", 60), ("Clauses", 12), ("Level", 8), ("Wording by clause", 30), ("Applies to", 16), ("Add-on support", 18),
        ("Status", 14), ("Evidence", 22), ("Owner", 14)]
header(ws, 4, cols)
rows = C.QCB_AI + C.QCB_CD + C.QCB_IR
for i, q in enumerate(rows):
    r = R0 + i
    for j, v in enumerate([q["id"], q["reg"], q["section"], q["topic"], q["req"], q["clauses"], q["level"], C.WORDING[q["id"]], q["applies"], q["support"]], 1):
        cell(ws, r, j, v, bold=j in (1, 4), fc=LEVELFILL.get(v) if j == 7 else None, h="center" if j == 7 else None, small=j in (8, 10))
    for j in (11, 12, 13): cell(ws, r, j, None, fc=PH)
    ws.row_dimensions[r].height = max(30, 13 * (len(q["req"]) // 85 + 1) + 6)
e = R0 + len(rows) - 1
dv_list(ws, LREF["req"], f"K{R0}:K{e}"); status_cf(ws, f"K{R0}:K{e}", C.STATUS_REQ[0], C.STATUS_REQ[1], C.STATUS_REQ[2])
ws.freeze_panes = "E5"; ws.auto_filter.ref = f"A4:M{e}"

# ------------------------------------------------------------------ 9B national
ws = new("9B National Requirements", "7030A0")
title(ws, "Reference: National (NCSA) requirements to add on top of the existing process", "NCSA issued these under Amiri Decree No. 1 of 2021, Article 3 (except N20, the Qatar 2022 Cybersecurity Framework, issued by the Supreme Committee for Delivery & Legacy and used as good practice); the NISRMF describes the four deliverables as every organisation's obligations under that Article. Strength follows each source's own wording (quoted). The NISRMF states that adopting a risk framework is 'strongly encouraged' and that reporting to NCSA is mandatory, and the EISRMF states 'Adoption is flexible; reporting is not.'; the NIA Standard states that it applies to all organisations and that baseline controls are mandatory. Where the source does not state how it is enforced for banks, see 'Confirm with'.", 11)
cols = [("ID", 14), ("Requirement", 34), ("Source", 18), ("Section", 16), ("Source wording (verbatim extract)", 40), ("Strength", 13), ("How to meet it on top of the existing ISO process", 38),
        ("Add-on sheets", 10), ("Confirm with", 16), ("Status", 14), ("Evidence", 20)]
header(ws, 4, cols)
for i, n in enumerate(C.NAT):
    r = R0 + i
    for j, v in enumerate(n, 1):
        cell(ws, r, j, v, bold=j in (1, 6), fc=STRFILL.get(v) if j == 6 else None, small=j in (3, 4, 5))
    cell(ws, r, 10, None, fc=PH); cell(ws, r, 11, None, fc=PH)
    ws.row_dimensions[r].height = 58
dv_list(ws, LREF["req"], f"J{R0}:J{NAT_END}"); status_cf(ws, f"J{R0}:J{NAT_END}", C.STATUS_REQ[0], C.STATUS_REQ[1], C.STATUS_REQ[2])
ws.row_breaks.append(Break(id=MAP0 - 3))
section(ws, MAP0 - 2, "Scale mapping: the bank's rating labels to the national EISRMF bands (complete; example values shown)")
for j, h in enumerate(["Bank rating label", "National band", "Bank score range (optional)", "Note"], 1):
    c = ws.cell(MAP0 - 1, j, h); c.font = Font(name=F, bold=True, color="FFFFFF"); c.fill = fill(NAVY); c.border = BOX; c.alignment = Alignment(wrap_text=True)
EXMAP = [("Critical", "Severe"), ("High", "High"), ("Medium", "Medium"), ("Low", "Low"), ("Very Low", "Very Low")]
for k in range(MAPN):
    r = MAP0 + k; a, b = EXMAP[k] if k < len(EXMAP) else (None, None)
    cell(ws, r, 1, a, fc=EX if a else PH, bold=True); cell(ws, r, 2, b, fc=PH, bold=True); cell(ws, r, 3, None, fc=PH); cell(ws, r, 4, None, fc=PH)
dv_list(ws, LREF["bands"], f"B{MAP0}:B{MAP0 + MAPN - 1}"); band_cf(ws, f"B{MAP0}:B{MAP0 + MAPN - 1}")
r = MAP0 + MAPN + 1
section(ws, r, "National bands: score = likelihood (1-5) x consequence (1-5) (EISRMF); bands from the NISRMF national risk matrix (Figure 7)"); r += 1
for j, h in enumerate(["National band", "Score range", "Note"], 1):
    c = ws.cell(r, j, h); c.font = Font(name=F, bold=True, color="FFFFFF"); c.fill = fill(NAVY); c.border = BOX
r += 1
for b, rg in zip(C.BANDS, C.BAND_RANGES):
    cell(ws, r, 1, b, bold=True, fc=BANDFILL[b]); cell(ws, r, 2, rg, h="center")
    cell(ws, r, 3, "Out-of-band report to NCSA: notify immediately; detailed report within 48 hours." if b in ("High", "Severe") else "Regular reporting cycle."); r += 1
x = ws.cell(r, 1, "Score ranges read from the NISRMF national risk matrix (Figure 7): every likelihood and consequence pair falls in these ranges; consistent with the EISRMF example 4 x 3 = 12 = High."); x.font = Font(name=F, size=9, italic=True)
r += 2
section(ws, r, "Crosswalk: national content to the bank's register fields"); r += 1
for j, h in enumerate(["National content item", "Source", "Typical ISO/IEC 27005 register field", "Add-on field", "Bank's field name"], 1):
    c = ws.cell(r, j, h); c.font = Font(name=F, bold=True, color="FFFFFF"); c.fill = fill(NAVY); c.border = BOX; c.alignment = Alignment(wrap_text=True)
r += 1
for row in C.CROSSWALK:
    for j, v in enumerate(row, 1): cell(ws, r, j, v)
    cell(ws, r, 5, None, fc=PH); ws.row_dimensions[r].height = 30; r += 1
ws.freeze_panes = "C5"

# ------------------------------------------------------------------ 9C laws
ws = new("9C Laws", "7030A0")
title(ws, "Reference: laws relevant to AI use in banks", "Only laws verified as applicable are listed. Other laws may apply to specific use cases; confirm with the bank's legal function.", 6)
table(ws, [("ID", 6), ("Law", 46), ("Relevance to AI", 60), ("Add-on support", 16), ("Status", 14), ("Evidence", 22)], [l + (None, None) for l in C.LAWS], heights=lambda r: 40)
e = R0 + len(C.LAWS) - 1
for i in range(len(C.LAWS)): ws.cell(R0 + i, 5).fill = fill(PH); ws.cell(R0 + i, 6).fill = fill(PH)
dv_list(ws, LREF["req"], f"E{R0}:E{e}"); status_cf(ws, f"E{R0}:E{e}", C.STATUS_REQ[0], C.STATUS_REQ[1], C.STATUS_REQ[2])

# ------------------------------------------------------------------ 10 calendar
ws = new("10 Reporting Calendar", "C55A11")
title(ws, "Submissions to NCSA and QCB", "Enter the date last submitted; next due date and status are calculated. Event-driven items have no frequency. Where NCSA and QCB deadlines differ for the same event, meet both.", 8)
header(ws, 4, [("Deliverable", 36), ("To", 16), ("Source", 26), ("Frequency (months)", 10), ("Last submitted", 12), ("Next due", 12), ("Check", 16), ("Notes", 40), ("Priority", 22)])
for i, (dl, to, src, fq, last, note) in enumerate(C.CAL):
    r = R0 + i
    cell(ws, r, 1, dl, bold=True); cell(ws, r, 2, to); cell(ws, r, 3, src); cell(ws, r, 4, fq if fq else "Event", h="center", fc=PH if fq else None)
    cell(ws, r, 5, dt.datetime.strptime(last, "%Y-%m-%d") if last else None, fc=PH, fmt="yyyy-mm-dd"); cell(ws, r, 8, note)
    cell(ws, r, 9, ("Recommended: " + C.CAL_RECOMMENDED[dl]) if dl in C.CAL_RECOMMENDED else ("Essential (6.2 timeframes use 'should')" if "Incident Reporting Guideline 6.2" in src else "Essential"))
    nd = f'=IF(E{r}="","",EOMONTH(E{r},0)+7)' if dl.startswith("Monthly consolidated incident report") else f'=IF(NOT(ISNUMBER(D{r})),"Event-driven",IF(E{r}="","",EDATE(E{r},D{r})))'
    cell(ws, r, 6, nd, calc=True, fmt="yyyy-mm-dd", h="center")
    cell(ws, r, 7, f'=IF(OR(NOT(ISNUMBER(D{r})),E{r}=""),"",IF(F{r}<TODAY(),"Overdue",IF(F{r}-TODAY()<=30,"Due within 30 days","OK")))', calc=True, bold=True, h="center")
    ws.row_dimensions[r].height = 30
e = R0 + len(C.CAL) - 1
_vf = DataValidation(type="whole", operator="between", formula1="1", formula2="120", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter whole months from 1 to 120."); ws.add_data_validation(_vf)
_vd = DataValidation(type="date", operator="greaterThan", formula1="DATE(2000,1,1)", allow_blank=True, showErrorMessage=True, errorStyle="stop", error="Enter a date."); ws.add_data_validation(_vd)
for i_, c_ in enumerate(C.CAL):
    if c_[3]: _vf.add(f"D{R0 + i_}")
_vd.add(f"E{R0}:E{e}")
ws.conditional_formatting.add(f"G{R0}:G{e}", CellIsRule(operator="equal", formula=['"Overdue"'], fill=fill("F8CBAD"), font=Font(name=F, bold=True)))
ws.conditional_formatting.add(f"G{R0}:G{e}", CellIsRule(operator="equal", formula=['"Due within 30 days"'], fill=fill("FFEB9C")))
r = e + 2
section(ws, r, "Severity scales: one event may need reports to both QCB and NCSA"); r += 1
for j, h in enumerate(["Scale", "Levels", "Used for", "Source"], 1):
    c = ws.cell(r, j, h); c.font = Font(name=F, bold=True, color="FFFFFF"); c.fill = fill(NAVY); c.border = BOX; c.alignment = Alignment(wrap_text=True)
r += 1
for row in C.SEVERITY:
    for j, v in enumerate(row, 1): cell(ws, r, j, v)
    ws.row_dimensions[r].height = 44; r += 1
for t in C.SEVERITY_NOTE:
    x = ws.cell(r, 1, t); x.font = Font(name=F, size=9, italic=True); x.alignment = Alignment(wrap_text=True); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8); ws.row_dimensions[r].height = 30; r += 1
ws.freeze_panes = "B5"

# ------------------------------------------------------------------ 11 summary
ws = new("11 Compliance Summary", "548235")
title(ws, "Compliance summary", "Counts from the status columns. Use for management reporting; it does not replace the bank's own compliance assessment.", 7)
for j, w in enumerate([44, 13, 13, 13, 13, 13, 13], 1): ws.column_dimensions[L(j)].width = w
header(ws, 4, [("Area", None)] + [(s, None) for s in C.STATUS_REQ] + [("Total rows", None)])
nq = len(C.QCB_AI + C.QCB_CD + C.QCB_IR); nn = len(C.NAT)
ROWS = [
 ("Essentials (0)", "'0 Essentials'", "G", None, None, len(C.ESSENTIALS), C.STATUS_REQ),
 ("QCB requirements - Must rows (9A)", "'9A QCB Requirements'", "K", "G", '"Must"', nq, C.STATUS_REQ),
 ("QCB requirements - Mixed rows, with at least one 'must' clause (9A)", "'9A QCB Requirements'", "K", "G", '"Mixed"', nq, C.STATUS_REQ),
 ("QCB requirements - all rows (9A)", "'9A QCB Requirements'", "K", None, None, nq, C.STATUS_REQ),
 ("National requirements - REQUIRED (9B)", "'9B National Requirements'", "J", "F", '"REQUIRED"', nn, C.STATUS_REQ),
 ("National requirements - CONDITIONAL (9B)", "'9B National Requirements'", "J", "F", '"CONDITIONAL"', nn, C.STATUS_REQ),
 ("Laws (9C)", "'9C Laws'", "E", None, None, len(C.LAWS), C.STATUS_REQ),
 ("NIA baseline (*) statements for AI assets (5B)", "'5B NIA for AI'", "I", "D", f'"{C.YES}"', len(C.NIA), C.STATUS_IMP),
 ("AI controls marked applicable (5)", "'5 AI Controls'", "Q", "P", f'"{C.YES}"', len(C.CONTROLS), C.STATUS_IMP),
]
for i, (lab, sh, col, fcol, fval, n, sts) in enumerate(ROWS):
    r = R0 + i; cell(ws, r, 1, lab, bold=True)
    rng = f"{sh}!${col}${R0}:${col}${R0 + n - 1}"
    cond = f",{sh}!${fcol}${R0}:${fcol}${R0 + n - 1},{fval}" if fcol else ""
    cell(ws, r, 7, f"=COUNTIF({sh}!${fcol}${R0}:${fcol}${R0 + n - 1},{fval})" if fcol else f"=ROWS({rng})", calc=True, h="center", bold=True)
    for j, s_ in enumerate(sts[:4], 2):
        cell(ws, r, j, f'=COUNTIFS({rng},"{s_}"{cond})', calc=True, h="center")
    cell(ws, r, 6, f"=G{r}-SUM(B{r}:E{r})", calc=True, h="center")
r = R0 + len(ROWS) + 1
x = ws.cell(r, 1, "For the NIA and controls rows the status columns read Implemented / Partially / Not implemented / Not applicable / Not assessed (blank counts as not assessed)."); x.font = Font(name=F, size=9, italic=True)
r += 2; ws.row_breaks.append(Break(id=r - 1)); section(ws, r, "Other indicators"); r += 1
OTHER = [("Scenarios with current national band High or Severe (4)", f"=COUNTIF('4 Risk Scenarios'!$O${R0}:$O${R0 + len(C.SCEN) - 1},\"High\")+COUNTIF('4 Risk Scenarios'!$O${R0}:$O${R0 + len(C.SCEN) - 1},\"Severe\")"),
         ("Scenario ratings not yet mapped in 9B (4)", f"=COUNTIF('4 Risk Scenarios'!$O${R0}:$R${R0 + len(C.SCEN) - 1},\"Map rating in 9B\")"),
         ("Scenarios with current band above the area's appetite (4, 8A)", f"=COUNTIF('4 Risk Scenarios'!$W${R0}:$W${R0 + len(C.SCEN) - 1},\"Above appetite\")"),
         ("High or Severe treatments past their target date (4)", f"=COUNTIF('4 Risk Scenarios'!$Z${R0}:$Z${R0 + len(C.SCEN) - 1},\"Overdue\")"),
         ("Risk acceptances expired (8B)", f"=COUNTIF('8B Risk Acceptance Log'!$N${ACC0}:$N${ACC0 + ACCN - 1},\"Expired\")"),
         ("Risk acceptances incomplete (8B)", f"=COUNTIF('8B Risk Acceptance Log'!$N${ACC0}:$N${ACC0 + ACCN - 1},\"Incomplete\")"),
         ("Indicators at red (6)", f"=COUNTIF('6 KRIs and KPIs'!$M${R0}:$M${R0 + len(C.KRIS) - 1},\"Red\")"),
         ("Submissions overdue (10)", f"=COUNTIF('10 Reporting Calendar'!$G${R0}:$G${R0 + len(C.CAL) - 1},\"Overdue\")"),
         ("AI systems needing two or more additional NIA controls per domain (5A)", f"=COUNTIF('5A NIA by AI System'!$I${R0}:$I${R0 + 49},\"Two or more*\")")]
for a, f_ in OTHER:
    cell(ws, r, 1, a, bold=True); cell(ws, r, 2, f_, calc=True, h="center", bold=True); r += 1
x = ws.cell(r + 1, 1, "Example rows (yellow IDs in 5A and 8B) are counted until replaced or deleted. The appetite count uses each scenario's current band, so a risk that has been accepted is still counted until its rating changes."); x.font = Font(name=F, size=9, italic=True)
ws.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1, end_column=7); x.alignment = Alignment(wrap_text=True); ws.row_dimensions[r + 1].height = 30

# ------------------------------------------------------------------ references
ws = new("References", "7F7F7F")
title(ws, "References", "Requirements are paraphrased or quoted in short extracts; the official texts prevail. NCSA is acknowledged as the source and owner of NCSA publications. ISO content is cited by clause number only.", 3)
table(ws, [("Document", 70), ("Issuer", 30), ("Status", 60)], C.REFS, heights=lambda r: 22)
r = R0 + len(C.REFS) + 1; section(ws, r, "Open points to confirm"); r += 1
for t in C.OPEN:
    x = cell(ws, r, 1, t); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3); ws.row_dimensions[r].height = 22; r += 1
r += 1; section(ws, r, "Notes"); r += 1
for t in C.NOTES:
    x = cell(ws, r, 1, t); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3); ws.row_dimensions[r].height = 22; r += 1

# ------------------------------------------------------------------ lists
ws = new("Lists")
for i, (k, vals) in enumerate(LISTS.items(), 1):
    ws.cell(1, i, k)
    for j, v in enumerate(vals, 2): ws.cell(j, i, v)
ws.sheet_state = "hidden"
# Final review 4 Nov 2026: row heights fitted to the text so nothing is clipped
import math
from openpyxl.utils import column_index_from_string
def _fit(ws):
    merged = {}
    for mr in ws.merged_cells.ranges:
        merged[(mr.min_row, mr.min_col)] = (mr.max_col, mr.max_row)
    covered = {(r, c) for mr in ws.merged_cells.ranges for r in range(mr.min_row, mr.max_row + 1) for c in range(mr.min_col, mr.max_col + 1)} - set(merged)
    need = {}
    for row in ws.iter_rows():
        for c in row:
            v = c.value
            if v is None or (c.row, c.column) in covered: continue
            s = str(v)
            if s.startswith("="): continue
            mc, mrow = merged.get((c.row, c.column), (c.column, c.row))
            if mrow != c.row: continue
            w = sum((ws.column_dimensions[L(k)].width or 8.43) for k in range(c.column, mc + 1))
            size = (c.font.sz or 10) if c.font else 10
            cpl = max(1.0, (w - 1.0) * 10.0 / size * 1.05)
            lines = sum(max(1, math.ceil(len(part) / cpl)) for part in s.split("\n"))
            h = lines * size * 1.32 + 5
            need[c.row] = max(need.get(c.row, 0), h)
    for r, h in need.items():
        cur = ws.row_dimensions[r].height
        if r == 1: continue
        if cur is None or cur < h: ws.row_dimensions[r].height = min(409, round(h, 1))
for _ws in wb.worksheets:
    if _ws.title != "Lists": _fit(_ws)
# Full review 6 Nov 2026: print setup (repeat header row, footer, no blank pages from empty input rows)
for _ws in wb.worksheets:
    if _ws.title == "Lists": continue
    hrs = [r for r in range(1, _ws.max_row + 1) if (_ws.cell(r, 1).fill.fgColor.rgb or "").endswith(NAVY)]
    if len(hrs) == 1 and not _ws.title.startswith("11 "): _ws.print_title_rows = f"{hrs[0]}:{hrs[0]}"  # repeat only where the sheet holds a single table
    last = max((c.row for row in _ws.iter_rows() for c in row if c.value is not None and not str(c.value).startswith("=")), default=1)
    _ws.print_area = f"A1:{L(_ws.max_column)}{min(_ws.max_row, last + 10)}"
    _ws.oddFooter.left.text = C.TITLE + " - " + C.VERSION; _ws.oddFooter.left.size = 8
    _ws.oddFooter.right.text = "Page &P of &N"; _ws.oddFooter.right.size = 8
wb.properties.title = C.TITLE; wb.properties.creator = "Abed Al Rahman Naboulsi"; wb.properties.lastModifiedBy = "Abed Al Rahman Naboulsi"
wb.save(OUT); print("saved", OUT)
