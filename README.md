# AI Security Risk Add-on for Banks in Qatar

**Version 1.0 - November 2026** · by Abed Al Rahman Naboulsi

A free add-on for the information security risk register a bank already runs. It adds the AI-specific content, and the QCB and NCSA requirements that apply to AI, so there is nothing to rebuild.

> **Advisory.** This add-on offers suggestions to help banks add AI security risk management and the national requirements to their existing ISO/IEC 27001, ISO/IEC 27005 and ISO 31000 process. It does not replace any law, regulation, standard or framework, and it does not interpret QCB or NCSA requirements. The official texts prevail. Each bank remains responsible for its own compliance.

This is a personal, non-commercial initiative. It is not affiliated with or endorsed by Qatar Central Bank (QCB), the National Cyber Security Agency (NCSA) or any other organisation.

---

## Who it is for

Banks in Qatar that already run an ISO/IEC 27001-based risk process (and often hold NIA, QCB, PCI DSS or SWIFT CSP obligations) and now need to cover AI systems: CISOs, information security and technology risk teams, AI system owners and internal audit.

## What is in the repository

| Folder | File | What it is |
|---|---|---|
| `workbook/` | `AI_Security_Risk_Addon_Banks_Qatar.xlsx` | The add-on workbook (20 sheets) |
| `docs/` | `AI_Security_Risk_Addon_Banks_Qatar_Guidance.pdf` / `.docx` | 22-page guidance |
| `docs/` | `AI_Security_Risk_Addon_Quick_Guide.pdf` / `.docx` | 3-page quick guide, including "When X happens: what to do and where" |
| `docs/` | `AI_Security_Risk_Addon_Overview.pdf` | 9-slide overview |
| `qa/` | `AI_Security_Risk_Addon_QA_Report.xlsx` | QA trail: each mapping, the reference it cites, the source wording checked and the verdict |
| `build/` | Python and Node.js scripts | Rebuild the workbook and guides from one data file (see `build/README.md`) |

## What the add-on covers

- **AI content ready to load:** 10 AI asset types, 24 AI threats (mapped to the OWASP Top 10 for LLM Applications 2026 and the OWASP Top 10 for Agentic Applications 2026 where covered), 25 vulnerabilities and 42 risk scenarios.
- **31 AI controls** with Statement of Applicability mappings to ISO/IEC 27001:2022 and ISO/IEC 42001:2023 Annex A, NIA v2.1 statements and QCSF capabilities.
- **NIA by AI system:** enter each AI system's confidentiality, integrity and availability ratings to see the baseline and additional NIA v2.1 controls it needs; all 356 NIA v2.1 statements (166 baseline) are listed by number and applied to AI.
- **QCB requirements for AI:** 71 rows from the AI Guideline, the Cloud Computing Regulation, the Data Handling and Protection Regulation and the Incident Reporting Guideline, each labelled with the source's own wording (44 Must / 23 Mixed / 4 Should).
- **The national layer:** 20 rows from NCSA frameworks (EISRMF, NISRMF, NIA v2.1, National Data Classification Policy, ECCMF and others), labelled REQUIRED / CONDITIONAL / RECOMMENDED / GOOD PRACTICE; mapping of the bank's ratings to the national EISRMF bands; out-of-band reporting of High and Severe risks to NCSA.
- **Governance:** approver per band and risk appetite per consequence area (set by the bank), the EISRMF decision-making levels, and a risk acceptance log with review dates.
- **One calendar for QCB and NCSA:** incident timeframes, the AI Register and Cloud Register disclosures, the national risk register, treatment plan and attestation.
- **13 Essentials** to start with, 25 indicators (KRIs and KPIs), 17 inputs and triggers, 3 worked examples, and a compliance summary.

**Not mapped in v1.0:** PCI DSS and SWIFT CSP (they stay in their own programmes). ISO/IEC 27090 is listed for reference only.

## Quick start

1. Open `docs/AI_Security_Risk_Addon_Quick_Guide.pdf` (3 pages).
2. Open the workbook and start with sheet **0 Essentials**.
3. Work through the sheets as the Quick Guide describes: add the AI asset types (1), rate AI systems (5A), select the scenarios that apply (4), map your ratings to the national bands (9B), set your governance values (8A) and enter submission dates (10).

The workbook was built and tested in LibreOffice Calc. Formulas recalculate when the file is opened; if values look empty, recalculate (LibreOffice: Data > Calculate > Recalculate Hard).

## How it was checked

Every requirement and citation was checked against the QCB and NCSA source texts, then reviewed again by independent reviews before release. The QA report in `qa/` records each check. ISO/IEC 42001 control IDs were checked against a published Annex A list, because the standard's text is copyrighted.

The add-on was built with AI assistance.

### Points to confirm

These cannot be settled from the published texts and are listed openly in the workbook (sheet **References**):

1. Whether the inherent or residual rating applies to out-of-band reporting to NCSA (the add-on uses the current rating).
2. Each bank's Critical National Organisation status (determined centrally by NCSA).
3. Which document is the Sector-Specific Security Regulation referred to in the QCB Incident Reporting Guideline.
4. The exact date and circular number of the QCB Incident Reporting Guideline.
5. Whether the 1-hour rule in the QCB Technology Risks circular (8.2.10) also covers reporting to NCSA, which NIA v2.1 IM 8 sets at 2 hours (the add-on suggests 1 hour until confirmed).

If you can answer any of these from an official source, please open an issue.

## Sources

QCB: Artificial Intelligence Guideline; Cloud Computing Regulation; Data Handling and Protection Regulation; Incident Reporting Guideline; Technology Risks circular (January 2018).
NCSA: Enterprise Information Security Risk Management Framework (EISRMF) v1.0; National Information Security Risk Management Framework (NISRMF) v1.0; National Information Assurance Standard v2.1; National Data Classification Policy v3.0; Enterprise Cyber Crisis Management Framework (ECCMF) v1.0; National Incident Management Framework; National Cyber Crisis Management Framework v1.0.
Other: Qatar 2022 Cybersecurity Framework (QCSF) v1.0 (good practice reference); Qatar laws on personal data privacy (No. 13 of 2016), AML/CFT (No. 20 of 2019) and the QCB Law (No. 13 of 2012); ISO/IEC 27001:2022, ISO/IEC 27005:2022, ISO 31000:2018, ISO/IEC 42001:2023; OWASP Top 10 for LLM Applications 2026; OWASP Top 10 for Agentic Applications 2026.

The full list, with the status of each source, is in the workbook's **References** sheet. Always use the latest official text from the issuer.

## How to credit

Free to use and adapt; please credit the source. A suggested credit line:

> Based on the *AI Security Risk Add-on for Banks in Qatar* (Version 1.0, November 2026) by Abed Al Rahman Naboulsi, https://github.com/ElNaboulsi/ai-security-risk-addon-qatar-banks

## Licence

The add-on's own content is licensed under the [Creative Commons Attribution 4.0 International licence](LICENSE) (CC BY 4.0). Short extracts quoted from QCB, NCSA, OWASP, ISO and other texts remain the property of their owners and are not covered by this licence; names of standards and frameworks are used for reference only.

## Contributing

Corrections and improvements are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md): every suggested change to a requirement or mapping should cite the official source text.

## Planned for a later version

- A vendor-neutral note on cloud landing zones
- Mapping to PCI DSS and SWIFT CSP
- Mapping to ISO/IEC 27090

See [CHANGELOG.md](CHANGELOG.md) for the version history.
