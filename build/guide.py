# Guidance (Word) content for the add-on; writes guide.js for ../kit/build_doc.js
import json
import content as C
NAT = {n[0]: n for n in C.NAT}
B = []
def add(*b): B.append(list(b))
add("kicker", "ADVISORY TOOLKIT · BANKS IN QATAR")
add("title", C.TITLE)
add("sub", "Guidance for banks that already run an ISO/IEC 27001, ISO/IEC 27005 and ISO 31000 risk process: how to add AI security risk management and the QCB, legal and NCSA requirements on top of it")
add("meta", C.VERSION)
add("box", "**Advisory.** " + C.ADVISORY.split(" - ", 1)[1])
add("small", C.NOTICE)
add("pb")
add("h1", "Contents")
TOC = ["Purpose and who it is for", "What is required and what is suggested", "The add-on in three steps", "Adding AI to the asset-based risk process", "NIA Standard v2.1 for AI assets",
       "Mapping ratings to the national scales", "Keeping the register live", "Indicators: KRIs and KPIs", "Evidencing QCB compliance", "Reporting to NCSA and QCB",
       "A first 90 days for an established bank", "Points to confirm", "Annex A: Workbook guide", "Annex B: Glossary", "Annex C: References", "Annex D: Worked examples"]
add("n", TOC[:12]); add("b", TOC[12:]); add("pb")

add("h1", "1. Purpose and who it is for")
add("p", "This add-on is for banks in Qatar that already run an information security risk process built on ISO/IEC 27001, ISO/IEC 27005 and ISO 31000, aligned with QCB requirements. AI changes what that process must cover: new assets (models, training data, prompts, agents), new threats (prompt injection, data poisoning, deepfakes), and new obligations under the QCB Artificial Intelligence Guideline, the Cloud Computing Regulation and the Data Handling and Protection Regulation. NCSA has also published requirements that apply across organisations, including reporting under the EISRMF and the controls of the NIA Standard v2.1.")
add("p", "This add-on helps a bank close those gaps without rebuilding anything. It provides ready-made AI content to load into the existing register, inventory and Statement of Applicability, and a set of requirement sheets to record and evidence compliance.")
add("b", ["**Keep** the bank's method, scales, register, tools and governance.", "**Add** AI assets, threats, vulnerabilities, scenarios, controls, indicators and triggers.",
          "**Align** ratings to the national bands for reporting to NCSA, and **evidence** QCB, legal and NCSA requirements."])

add("h1", "2. What is required and what is suggested")
add("p", "Each requirement in the add-on is labelled by its source and by the strength of the source's own wording, so the bank can separate obligations from good practice.")
add("tbl", ["Source", "Strength in the add-on", "Basis"], [
 ["QCB AI Guideline, Cloud Computing Regulation, Data Handling and Protection Regulation, Incident Reporting Guideline", "Must / Should / May, or Mixed where a row combines them (the regulation's own words)", f"Banks are regulated by QCB under Law No. 13 of 2012. Sheet 9A lists {len(C.QCB_AI) + len(C.QCB_CD) + len(C.QCB_IR)} obligations relevant to AI, verified against the texts."],
 ["QCB Technology Risks circular (January 2018)", "Cited by section number", "The add-on cites section numbers, and states only the two timelines needed for the reporting calendar (8.2.10 and 7.1.1)."],
 ["Laws of Qatar", "Law", "Law No. 13 of 2016 (personal data) and Law No. 20 of 2019 (AML/CFT), where relevant to AI."],
 ["EISRMF and NISRMF (NCSA)", "REQUIRED: reporting; RECOMMENDED: adopting the full framework", "'Adoption of a risk framework is strongly encouraged. Reporting to NCSA is mandatory.' (NISRMF). The NISRMF describes the four deliverables as every organisation's obligations under Amiri Decree No. 1 of 2021, Article 3."],
 ["NIA Standard v2.1 (NCSA)", "REQUIRED: classification first; baseline (*) controls; additional controls for higher ratings", "'This standard applies to all Organizations'; baseline controls 'are mandatory and must be implemented' (2.2, 2.3)."],
 ["National Data Classification Policy v3.0 (NCSA)", "REQUIRED (confirm with QCB and NCSA)", "'The policy mandates that organizations within the scope of this policy, classify their data' (10.3). Its scope is 'in coordination with sector regulator'; QCB DHP 6.1-6.2 asks for a classification policy based on leading practice and says a bank 'may' use the national policy."],
 ["ECCMF v1.0 (NCSA)", "CONDITIONAL for Critical National Organisations; RECOMMENDED otherwise", "CNO compliance 'will be monitored by sector regulators'; others 'are also encouraged to adopt'."],
 ["National Incident Management Framework (NIMF) (NCSA)", "Reference (restates the NIA two-hour rule)", "Restates that organisations 'must report critical cyber incidents to the NCSA within two hours of identification' (4.1); NCSA assigns the national incident category (1.6, 4.1)."],
 ["National Cyber Crisis Management Framework (NCCMF) v1.0 (NCSA)", "Reference only", "National crisis management; the NIMF describes it as providing 'the national cyber crisis management capability beyond the NIMF' (1.6). No bank duties are taken from it."],
 ["ISO/IEC 27001 and 42001; ISO/IEC 27005 and ISO 31000", "Good practice (the bank's chosen method)", "ISO/IEC 27001 and 42001 cited by clause number; ISO/IEC 27005 and ISO 31000 cited by name."],
 ["OWASP Top 10 for LLM Applications 2026; OWASP Top 10 for Agentic Applications 2026", "Good practice (threat references)", "Threats in sheet 2 cite OWASP entry IDs and names (OWASP GenAI Security Project)."],
 ["Qatar 2022 Cybersecurity Framework (QCSF)", "GOOD PRACTICE", "Issued in 2018 for entities in the 2022 World Cup ecosystem; used for capability mapping only."],
], [30, 26, 44])
add("small", "Where a source does not say how it is enforced for banks (for example, the cycle for submitting the risk register to NCSA), the add-on shows 'Confirm with' rather than assuming.")

add("h1", "3. The add-on in three steps")
add("tbl", ["Step", "What the bank does", "Sheets", "Result"], [
 ["1. Add AI content", "Add AI asset types to the asset inventory or IAR; select the scenarios that apply and rate them on the bank's own scale; add the applicable AI controls to the SoA; adopt indicators and triggers; add the minimum fields.", "1-8", "AI risks in the existing register, controls in the SoA"],
 ["2. Map ratings to national bands", "Map each of the bank's rating labels to a national EISRMF band. The national band and the out-of-band flag then appear for every scenario.", "9B, 4", "Consistent High and Severe identification for NCSA"],
 ["3. Evidence compliance", "Record status and evidence for QCB, national, NIA and legal requirements; track submissions; report the summary.", "5A, 5B, 9A-9C, 10, 11", "A compliance view the bank can show to its board, QCB and NCSA"],
], [20, 46, 12, 22])

add("p", "The workbook has three layers. Start with sheet 0 Essentials: 13 actions whose source wording is mandatory (QCB \"must\", NCSA REQUIRED or NIA baseline); E12 also includes the QCB \"should\" timeframes of Incident Reporting Guideline 6.2. The working sheets (1-8 and 10) hold the content to load into the bank's existing process; fields and calendar rows are tagged Essential or Recommended, and scenarios and controls show whether they link to mandatory QCB requirements. Sheets 5B, 9A, 9B and 9C are the reference layer with the full requirement detail for evidence and audit. Every REQUIRED and Must row applies wherever it sits.")
add("h1", "4. Adding AI to the asset-based risk process")
add("p", f"The add-on follows the ISO/IEC 27005 asset-based approach: asset, threat, vulnerability, consequence. Each element has its own sheet, and the {len(C.SCEN)} scenarios in sheet 4 combine them.")
add("h2", "AI assets (sheet 1)")
add("p", "Ten AI asset types cover models, training data, chatbot interfaces, knowledge bases, AI APIs and cloud services, AI features inside vendor products, agents, prompts and guard rails, outputs and logs, and public AI tools. Most are secondary (supporting) assets; the business process and the information they serve are the primary assets. Record both, so that a risk to an AI component is linked to what the bank actually needs to protect.")
add("h2", "Threats and vulnerabilities (sheets 2 and 3)")
add("p", f"Sheet 2 lists {len(C.THREATS)} AI threats; where the OWASP Top 10 for LLM Applications 2026 or the OWASP Top 10 for Agentic Applications 2026 covers a threat, its entry is given. Sheet 3 lists {len(C.VULNS)} vulnerabilities that make those threats possible, how to detect them, and the controls that address them.")
add("h2", "Scenarios (sheet 4)")
add("p", "Each scenario states what could happen, to which asset, through which path and with what consequence, and names the main consequence area. The add-on also lists the suggested controls, the NIA baseline statements those controls support, the QCB requirements involved and the ISO/IEC 27001 Annex A controls. The bank decides which scenarios apply, assigns an owner and rates them with its own scales.")
add("b", ["Copy only the scenarios that apply; adapt the wording to the bank's systems.", "Use the bank's existing likelihood and impact scales; the national band is calculated from the mapping in 9B.",
          "A scenario rated High or Severe on the national band needs out-of-band reporting to NCSA (section 6)."])
add("h2", "Controls (sheet 5)")
add("p", f"Sheet 5 provides {len(C.CONTROLS)} AI controls ({sum(1 for c in C.CONTROLS if c['scope'] == 'Core')} core and {sum(1 for c in C.CONTROLS if c['scope'] != 'Core')} bank-specific), each with what good looks like and the evidence expected. Each control is mapped, where a match exists, to ISO/IEC 27001 Annex A for the Statement of Applicability, and to ISO/IEC 42001, NIA v2.1, QCSF, the QCB requirement rows and the Technology Risks circular sections. The bank marks each control as applicable or not and records implementation status and evidence.")

add("h1", "5. NIA Standard v2.1 for AI assets")
add("p", "The NIA Standard states that it 'applies to all Organizations and their corresponding information assets'. AI assets are information assets, so the same rules apply to them:")
add("n", ["**Classify first.** Using the National Data Classification Policy 'is a mandatory step before attempting to apply the controls' (2.3 a). Sheet 5A records the confidentiality, integrity and availability rating of each AI system.",
          "**Baseline controls.** Assets rated 1 or above 'require compliance to all control statements that are baseline at minimum' (2.3 c). NIA v2.1 has 166 baseline statements, marked * in the standard and 'Yes' in sheet 5B.",
          "**Additional controls.** Assets rated 2 need one or more additional controls per applicable domain, and assets rated 3 or above need two or more, chosen through risk assessment (2.3 d-e). Sheet 5A shows which applies to each AI system.",
          "**Priority.** Implementation priority should be based on the aggregate level, with High first (2.3 f)."])
add("p", "Sheet 5B lists all 356 statements with their domain, whether they are baseline, how they apply to AI assets, and which add-on controls support them. The bank records status and evidence for its AI assets. Statements are listed by number only; read each one in the NIA Standard v2.1 published by NCSA.")
add("small", "NIA v2.1 numbers two statements 'PH 2' and has no PH 1; the add-on shows them as PH 2 (first) and PH 2 (second).")

add("h1", "6. Mapping ratings to the national scales")
add("p", "The EISRMF does not ask a bank to replace its framework. It states that organisations that already run one 'adopt the components required for national consistency and align their scoring to the national scales'. The add-on does this with a mapping table in 9B: the bank lists its own rating labels and selects the matching national band for each.")
add("tbl", ["National band", "Score range (likelihood x consequence)", "Reporting"],
    [[b, r, "Notify NCSA immediately; detailed report within 48 hours" if b in ("High", "Severe") else "Regular cycle"] for b, r in zip(C.BANDS, C.BAND_RANGES)], [20, 34, 46])
add("small", "The add-on applies out-of-band reporting to NCSA for High and Severe risks, in line with the EISRMF reporting section (pp. 20-24) and the NISRMF (pp. 14, 15, 22). Confirm with NCSA whether the inherent or residual rating applies; the add-on uses the current rating.")
add("small", "The score ranges are read from the national risk matrix in the NISRMF (Figure 7), where every likelihood and consequence pair falls within them; they agree with the EISRMF example that likelihood 4 x consequence 3 = 12 is High. The 48-hour report covers the risk description and severity, the potential impact on critical assets or infrastructure, current mitigation efforts and any support requested from NCSA (NISRMF).")
add("p", "9B also includes a crosswalk from the content of the national registers (Information Asset Register, Information Security Risk Register, Annual Risk Treatment Plan and the 48-hour report) to typical ISO/IEC 27005 register fields, so the bank can confirm that its existing templates can produce what NCSA receives.")

add("h1", "7. Keeping the register live")
add("p", "Sheet 7 lists the inputs that should feed the register and trigger reassessment: AI incidents, data breaches, test and red-team findings, KRIs at red, threat intelligence, significant changes, vendor AI changes, audit and QCB findings, supplier assessments, exercises, complaints and changes in law or regulation. Reassessment times are placeholders; NCSA and QCB deadlines take precedence.")
add("b", ["**Material change.** The NISRMF asks for the register to be reviewed whenever a material change occurs, as well as at least every six months.",
          "**Intelligence from NCSA.** The NISRMF states that 'Intelligence shared with an organization must be recorded in that organization's risk register' and reflected in its treatment plan.",
          "**Vendor AI changes.** A provider adding an AI feature or replacing a model is a change: assess it before use. If the bank acts as Provider (AI Guideline 14.3), check whether it is a material modification that needs QCB approval (11.1).",
          "**Incidents.** Where NIA controls and other regulations overlap, the NIA Standard asks organisations to comply with both or with whichever gives the higher degree of security. Incidents go to QCB under its Incident Reporting Guideline (High cyber or technology incidents within 1 hour, Medium within 4 hours) and critical incidents to NCSA within two hours (NIA IM 8); the Technology Risks circular (8.2.10) also sets 1 hour for critical incidents to QCB and the relevant governmental authorities (whether this covers NCSA is an open point). Data breaches are reported as incidents to QCB and also to NCSA and the Ministry of Interior (DHP 16.1-16.3). An incident at an AI provider that affects the bank is reported to QCB by the bank (Incident Reporting Guideline 6.3 bullet 10). An incident that escalates to a crisis follows the bank's crisis plan in line with the ECCMF."])

add("h1", "8. Indicators: KRIs and KPIs")
add("p", f"Sheet 6 provides {sum(1 for k in C.KRIS if k[1] == 'KRI')} KRIs and {sum(1 for k in C.KRIS if k[1] == 'KPI')} KPIs. KRIs show changes in exposure (for example unregistered AI services, blocked sensitive uploads, drift, detected deepfake attacks); KPIs show control performance (for example AI systems assessed, NIA baseline statements implemented, incidents reported on time). Each has a formula, data source, frequency and suggested amber and red thresholds; the status is calculated when the current value is entered. Thresholds marked 'set from baseline' should be set after a few months of measurement.")

add("h1", "9. Evidencing QCB compliance")
add("p", "Sheet 9A lists the obligations relevant to AI from four QCB instruments, verified against the official texts, with clause numbers, the regulation's own wording level and scope, and the add-on controls that support each.")
add("tbl", ["Instrument", "Rows", "Key points for AI"], [
 ["Artificial Intelligence Guideline (in force 4 September 2024)", str(len(C.QCB_AI)), "AI Register (10.7) and annual disclosure (10.6); high-risk classification (9.6-9.7); QCB approval before Provider launch, material change or high-risk agreements (11); human oversight (13); model security including prompt injection (17.4-17.7); serious incident reporting (19.5); customer notice, explanation and recourse (20-21)."],
 ["Cloud Computing Regulation (in force 15 April 2024)", str(sum(1 for q in C.QCB_CD if q['id'].startswith('CL'))), "QCB approval before a cloud arrangement (21.5); approval before signing material arrangements (13.4); PII and financial information processed in Qatar only (21.4); Cloud Register (9)."],
 ["Incident Reporting Guideline (2024; exact date to confirm)", str(len(C.QCB_IR)), "Triage with QCB priorities, High assumed until downgraded (6.1); High cyber or technology incidents within 1 hour, Medium within 4 hours, other High within 4 hours (6.2); Hotline first, initial report content, updates, final report within 3 days of resolution (6.3); monthly consolidated report within 7 days of month end (6.2-6.3); incidents reported to other authorities and incidents at third parties also reported to QCB (6.3)."],
 ["Data Handling and Protection Regulation (effective 16 February 2025)", str(sum(1 for q in C.QCB_CD if q['id'].startswith('DH'))), "Classification (may use the National Data Classification Policy, 6.2); ROPA (6.4); PIA (10.4); privacy assessment for autonomous processing (13.4); QCB approval for fully autonomous decision-making (13.5); foreign storage approval (15.1); breach reporting (16.3)."],
], [28, 10, 62])
add("p", "Each row keeps the regulation's own wording level. A row marked Mixed combines clauses with different wording and contains at least one \"must\" clause; the \"Wording by clause\" column lists which clauses are \"should\", \"may\" or \"will\". The DHP itself states that \"must\" is obligatory and \"may\" is advisory (DHP 3).")
add("p", "For each row the bank records status, evidence and owner. The compliance summary (sheet 11) counts status for Must rows and Mixed rows separately.")

add("h1", "10. Reporting to NCSA and QCB")
add("p", "A bank reports along two lines: to QCB as its regulator and to NCSA as the national cyber security authority. Each line has its own triggers, timelines and severity scale, and one event can need reports on both.")
add("tbl", ["Line", "What is reported", "Source"], [
 ["QCB", "Incidents by QCB priority (1 hour / 4 hours / monthly consolidated report; final report within 3 days of resolution); critical incidents within 1 hour; serious AI incidents; data breaches; annual AI Register, Cloud Register and Technology Risks compliance report; approvals and notifications before launch or signing", "Incident Reporting Guideline 6.2-6.3; Technology Risks circular 8.2.10, 7.1.1; AI Guideline 10.6, 11, 13.6.1, 19.5; Cloud Regulation 9.4, 13.4, 21.5; DHP 13.5, 15.1, 16.1-16.3"],
 ["NCSA", "Critical incidents within 2 hours (1 hour suggested until confirmed whether Technology Risks circular 8.2.10 applies); High and Severe risks out of band (immediately, detailed report within 48 hours); Information Security Risk Register, Annual Risk Treatment Plan and attestation; data breaches", "NIA v2.1 IM 8; NIMF 4.1; EISRMF; NISRMF; DHP 16.3"],
], [10, 58, 32])
add("p", "Where the two lines meet:")
add("b", ["**One incident, two reports.** Two rules apply to a critical cyber incident: the Technology Risks circular (8.2.10) sets 1 hour for reporting to QCB and the relevant governmental authorities, and NIA v2.1 (IM 8) sets 2 hours for reporting to NCSA. Whether NCSA is one of those authorities is an open point to confirm with QCB and NCSA; until then, reporting to NCSA within 1 hour is the cautious option. The Incident Reporting Guideline states that an incident reported to any authority must also be reported to QCB, and the NIA Standard asks organisations to comply with both requirements where they intersect.",
          "**Different scales.** QCB rates incidents High, Medium or Low under its own scheme; NIA v2.1 refers to Critical incidents without defining the term; the EISRMF bands (Very Low to Severe) rate risks, not incidents. Sheet 10 sets out the scales and a suggested way to apply them together; no official mapping is published.",
          "**Submitted to NCSA.** EISRMF and NISRMF deliverables are submitted by the bank to NCSA. Still to confirm with NCSA: the submission cycle and how NIA is enforced for banks."])
add("tbl", ["Scale", "Levels", "Used for", "Source"], [list(x) for x in C.SEVERITY], [22, 30, 28, 20])
add("h2", "Who signs what")
add("p", "The two registers sent to the authorities have different sign-off rules:")
add("tbl", ["Register", "What the source says", "Source"], [
 ["QCB AI Register", "Disclosed to QCB annually and on request. No signatory is named. The Board and senior management remain accountable for the outcomes and decisions of AI systems; roles must be clearly allocated between model owners, developers and approvers.", "AI Guideline 10.6, 7.1, 8.2.3"],
 ["NCSA Information Security Risk Register", "Reviewed internally at least every six months and submitted to NCSA. The attestation of adoption is submitted annually by the President or equivalent (EISRMF); it is signed and sent with copies of the risk register and treatment plan (NISRMF).", "EISRMF, Reporting to NCSA; NISRMF, What organizations owe"],
], [22, 56, 22])
add("p", "A suggested sign-off chain that satisfies both, and ISO/IEC 27001:")
add("n", ["AI system owners confirm that their AI Register entries are accurate and complete (suggested practice).",
          "Risk owners approve the risk treatment plan and accept residual risk (ISO/IEC 27001 6.1.3: required for conformity).",
          "The AI oversight / risk function reviews and consolidates both registers (suggested practice; AI Guideline 7.4-7.5 on the function overseeing AI).",
          "Senior management approves the QCB disclosure and the Board is informed (suggested practice; AI Guideline 7.1, 7.3.4).",
          "The President or equivalent submits the NCSA attestation (EISRMF; NISRMF)."])
add("p", "Keep each register as a working file and each disclosure as a dated, approved snapshot (ISO/IEC 27001 and 42001, 7.5 Documented information). Sheet 8 lists the fields and sheet 10 the internal sign-off date.")
add("h2", "Governance settings (sheets 8A and 8B)")
add("p", "Sheet 8A holds the bank's own approval and escalation settings next to the published EISRMF text. The bank sets the approvers, acceptance periods, appetite and who holds each decision level; the EISRMF meaning of each band, the NCSA reporting rule and the EISRMF decision-making levels are given as fixed text.")
add("b", ["**By band.** For each national band: the approver for treatment and residual-risk acceptance (in addition to the risk owner) and the maximum acceptance period, set by the bank; what the band means (EISRMF Figure 5); and out-of-band reporting to NCSA for High and Severe risks (EISRMF; NISRMF).",
          "**Risk appetite.** For each consequence area, the highest band the bank accepts. Sheet 4 compares each scenario's current band with it and shows \"Above appetite\" when it is exceeded; the EISRMF prioritises risks above appetite for treatment.",
          "**Decision-making authority.** Strategic (Executive Management or Board), tactical (CISO or relevant business owners) and operational (designated individuals), as in EISRMF Figure 3; the bank names who holds each level. The same figure describes an Information Security Governance Committee (ISGC) and a Risk Management Committee; map them to the bank's existing committees.",
          "**Acceptance log (8B).** One row per accepted risk, with the risk owner and the date they accepted it (ISO/IEC 27001 6.1.3). The approver required and the review date come from 8A; an approver role different from 8A is flagged \"Check\", and expired or incomplete acceptances are flagged.",
          "**Example.** Approval authority usually rises with the band, for example from the information security function to senior management and then the Board or a Board committee. The Board and senior management remain accountable for AI (QCB AI Guideline 7.1), and senior management keeps the Board informed (7.3.4).",
          "**Review.** " + C.GOV_FOOTER])
add("h2", "Submission calendar (sheet 10)")
add("tbl", ["Deliverable", "To", "When", "Source"],
    [[c[0], c[1], ({1: "Monthly", 3: "Quarterly", 6: "Every 6 months", 12: "Annual"}.get(c[3], f"Every {c[3]} months") if c[3] else "Event-driven") + (". " + c[5] if c[5] else ""), c[2]] for c in C.CAL], [30, 18, 34, 18])
add("small", "Sheet 10 calculates due dates from the date last submitted. EISRMF and NISRMF deliverables are submitted to NCSA; confirm the submission cycle with NCSA.")

add("h1", "11. A first 90 days for an established bank")
add("tbl", ["Period", "Focus"], [
 ["Days 1-30", "Assign an owner to each of the 13 essentials (sheet 0). Compare the bank's templates with sheet 8 and the 9B crosswalk; add missing fields. Complete the scale mapping in 9B. Add AI asset types to the inventory and rate AI systems in 5A. Set up the direct reporting line to NCSA."],
 ["Days 31-60", "Set the governance values (8A) and start the acceptance log (8B). Select and rate applicable scenarios (4) in the existing register. Mark applicable controls (5) in the SoA. Record NIA baseline status for AI assets (5B). Record QCB status and evidence (9A), focusing on 'Must' rows and approvals."],
 ["Days 61-90", "Start the indicators (6) and triggers (7). Report High and Severe AI risks to NCSA if any. Present the compliance summary (11) to management and plan remaining gaps in the Annual Risk Treatment Plan."],
], [16, 84])

add("h1", "12. Points to confirm")
add("p", f"{len(C.OPEN)} points need confirmation from QCB or NCSA:")
add("b", C.OPEN)
add("p", "Notes:")
add("b", C.NOTES)

add("h1", "Annex A: Workbook guide")
add("tbl", ["Sheet", "Purpose", "Bank completes"], [
 ["Start Here", "Purpose, three steps, three layers, strength legend, colours.", "-"], ["0 Essentials", "13 mandatory actions to start with (E12 also includes QCB \"should\" timeframes).", "Status, owner, date, evidence"], ["1 AI Asset Types", "AI assets with classification guidance and fields.", "Add to inventory"],
 ["2 AI Threats", "Threat catalogue with OWASP LLM and Agentic Top 10 references.", "-"], ["3 AI Vulnerabilities", "Weaknesses, detection and fixes.", "-"],
 ["4 Risk Scenarios", f"{len(C.SCEN)} scenarios with controls, NIA, QCB and ISO links.", "Applicability, owner, ratings, treatment, status"],
 ["5 AI Controls", "31 controls with full mappings.", "Applicability, status, evidence, owner, date"],
 ["5A NIA by AI System", "NIA requirements per AI system from its ratings.", "AI systems and C, I, A ratings"],
 ["5B NIA for AI", "All 356 NIA statements applied to AI assets.", "Status and evidence"], ["6 KRIs and KPIs", "Indicators with thresholds.", "Current values"],
 ["7 Inputs and Triggers", "Inputs, reassessment times, escalation, where to record each one and the date to enter.", "Reassessment times"], ["8 Fields to Add", "Minimum fields with requirement source.", "Already in template?"],
 ["8A Governance Settings", "Approver and acceptance period per band, with EISRMF meaning and NCSA reporting; appetite per area; decision-making authority.", "Approvers, periods, appetite, who holds each level"], ["8B Risk Acceptance Log", "Accepted risks with risk owner, approver check, review date and status.", "One row per acceptance"],
 ["9A QCB Requirements", f"{len(C.QCB_AI) + len(C.QCB_CD) + len(C.QCB_IR)} QCB obligations relevant to AI.", "Status, evidence, owner"], ["9B National Requirements", "NCSA requirements plus the QCSF (good practice), scale mapping, crosswalk.", "Status, evidence, mapping, field names"],
 ["9C Laws", "Laws relevant to AI.", "Status, evidence"], ["10 Reporting Calendar", "NCSA and QCB submissions; severity scales.", "Last submitted dates"],
 ["11 Compliance Summary", "Status counts.", "-"], ["References", "Sources and open points.", "-"],
], [24, 46, 30])
add("h1", "Annex B: Glossary")
add("tbl", ["Term", "Meaning in this add-on"], sorted([
 ["AI agent", "Software that uses a model to plan and carry out actions through tools, APIs or other systems."], ["Aggregate level", "Low, Medium or High: the classification level from the C, I and A ratings in the National Data Classification Policy matrix (Table 1); NIA v2.1 2.3 f calls it the aggregate security level."],
 ["Baseline control (NIA)", "A control statement marked * in NIA v2.1; mandatory for assets rated 1 or above."], ["Cloud arrangement (QCB)", "Any arrangement with a cloud service provider, or with a third party that uses one in the services it provides (Cloud Regulation, definitions)."],
 ["Deepfake", "Synthetic audio, image or video made to imitate a real person."], ["IAR", "Information Asset Register (EISRMF)."], ["ISRR", "Information Security Risk Register (EISRMF)."],
 ["National band", "Very Low, Low, Medium, High or Severe on the national EISRMF scales."], ["Out-of-band report", "Immediate notification to NCSA of a High or Severe risk, with a detailed report within 48 hours."],
 ["Prompt injection", "Instructions hidden in input or content that make an AI system ignore its intended behaviour."], ["Primary / secondary asset", "Primary assets are business processes and information; secondary assets are the systems that support them."],
 ["ROPA", "Record of Processing Activities (DHP 6.4)."], ["PIA", "Privacy Impact Assessment (DHP 10.4)."], ["SoA", "Statement of Applicability (ISO/IEC 27001 6.1.3)."],
], key=lambda x: x[0]), [24, 76])
add("h1", "Annex C: References")
add("tbl", ["Document", "Issuer", "Status"], [list(r) for r in C.REFS], [50, 22, 28])
add("pb")
add("h1", "Annex D: Worked examples")
add("p", "Three AI systems taken end to end through the workbook. Ratings, bands, appetite levels and approvers are examples; each bank uses its own scale and its own values in 8A.")
for i, w in enumerate(C.WORKED):
    s_, e_, rows_ = C.worked(w)
    add("h2", f"D.{i + 1} {e_[1]} ({s_[0]})")
    add("tbl", ["Step", "Example"], [list(x) for x in rows_], [17, 83])

open("guide.js", "w").write("module.exports = " + json.dumps({"rtl": False, "title": C.TITLE + " - Guidance", "creator": "Abed Al Rahman Naboulsi", "header": C.TITLE + " · Guidance",
                                                                "footer": "Advisory toolkit · " + C.VERSION, "blocks": B}, ensure_ascii=False, indent=1) + ";\n")
print("ok", len(B))
