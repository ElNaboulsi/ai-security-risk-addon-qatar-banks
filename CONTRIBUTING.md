# Contributing

Thank you for helping improve the AI Security Risk Add-on for Banks in Qatar. Anyone can contribute: practitioners, auditors, risk and security teams.

## Ways to contribute

- **Report a correction** (a wrong clause number, level, deadline or mapping): open an issue with the *Correction* template.
- **Suggest an improvement** (a new scenario, control, indicator or mapping): open an issue with the *Suggestion* template.
- **Answer an open point:** the five points to confirm are listed in the README and in the workbook's References sheet.
- **Propose a change directly:** open a pull request (see below).

## The one rule: cite the official source

Every change to a requirement, level (Must / Should / REQUIRED / RECOMMENDED), deadline or mapping must cite the official text it rests on: the document, its version or date, the clause or page, and the exact wording. Changes without a verifiable source cannot be accepted.

Please also:

- Write in your own words; quote only the short wording needed to show the requirement.
- Do not upload copies of standards or other copyrighted or non-public documents.
- Keep the content vendor-neutral: no product, tool or vendor names.
- Do not include confidential information about any bank or organisation.

## Pull requests

The workbook and guides are generated from one data file, `build/content.py`, so changes go there rather than into the Excel or Word files:

1. Edit `build/content.py` (and `build/build.py`, `guide.py` or `quick.py` if the layout changes).
2. Rebuild as described in `build/README.md` and check that the workbook opens without formula errors.
3. In the pull request, list each change with its source citation.

Small fixes to the README or documentation are welcome as pull requests too.

## Review

Each contribution is checked against the cited source before it is accepted. Accepted changes are listed in `CHANGELOG.md` with the next version.

By contributing, you agree that your contribution is shared under the same licence as the project (CC BY 4.0).
