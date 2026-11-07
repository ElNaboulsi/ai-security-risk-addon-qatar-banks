# 2-page quick guide, built from the same content as the workbook
import json, re, content as C
B = []
def add(*b): B.append(list(b))
add("kicker", "QUICK GUIDE · BANKS IN QATAR")
add("title", "AI Security Risk Add-on: quick guide")
add("small", C.VERSION + " · " + C.NOTICE)
add("box", "Advisory. Suggestions to help banks add AI security risk management and the national requirements to their existing ISO/IEC 27001, ISO/IEC 27005 and ISO 31000 process. The official texts prevail. Each bank remains responsible for its own compliance.")
add("p", "Three layers: 1. Essentials (sheet 0) - start here; 2. Working sheets (1-8, 10) - content for the existing inventory, register, SoA and calendar, with fields and calendar rows tagged Essential or Recommended; 3. Reference (5B, 9A, 9B, 9C) - full requirement detail for evidence and audit, where status is recorded. Every REQUIRED and Must row applies wherever it sits.")
add("h1", "The 13 essentials")
add("tbl", ["ID", "Action", "Source"], [[e[0], e[1], re.sub(r"(\d)-(\d)", "\\1\u2011\\2", e[2])] for e in C.ESSENTIALS], [7, 63, 30])
add("small", "Rule: an action is an essential only if its source uses mandatory wording (QCB 'must', NCSA REQUIRED, NIA baseline). E12 also includes the 'should' timeframes of Incident Reporting Guideline 6.2.")
add("h1", "Then, in the working sheets")
add("p", "Add the AI asset types (1) and rate AI systems (5A). Select the scenarios that apply (4), rate them on the bank's own scale and map ratings to the national bands (9B). Mark applicable AI controls (5) in the SoA. Add missing fields (8), starting with those tagged Essential. Set approvers and risk appetite (8A); log accepted risks (8B). Enter last submission dates (10); start indicators (6) and triggers (7).")
add("h1", "Two reporting lines")
add("tbl", ["To", "What", "Source"], [
 ["QCB", "Critical incidents within 1 hour (Technology Risks circular 8.2.10); incidents by QCB priority (cyber or technology High 1 hour, Medium 4 hours; other High 4 hours; final report 3 days after resolution, monthly report); AI Register yearly; approvals before launch or signing", "Technology Risks circular 8.2.10; Incident Reporting Guideline 6.2-6.3; AI Guideline 10.6, 11; Cloud Regulation 13.4, 21.5"],
 ["NCSA", "Critical incidents within 2 hours (1 hour suggested until confirmed); High and Severe risks out of band (48-hour report); register, treatment plan, attestation", "NIA v2.1 IM 8; Technology Risks circular 8.2.10; EISRMF; NISRMF"]], [10, 60, 30])
add("pb")
add("h1", "When X happens: what to do and where")
add("p", "Ten everyday events. Numbers are sheets, letters are columns. Sheet 7 lists all inputs, where to record each one and the reassessment days (set by the bank). Deadlines as stated in the sources cited; open points are in the References sheet.")
add("tbl", ["When", "What to do, and by when", "Where to record it", "Who approves"], [[re.sub(r"(\d)-(\d)", "\\1\u2011\\2", x) for x in w] for w in C.WHEN], [17, 38, 27, 18])
open("quick.js", "w").write("module.exports = " + json.dumps({"rtl": False, "title": C.TITLE + " - Quick guide", "creator": "Abed Al Rahman Naboulsi", "header": C.TITLE + " · Quick guide",
    "footer": "Advisory toolkit · " + C.VERSION, "blocks": B}, ensure_ascii=False, indent=1) + ";\n")
print("ok", len(B))
