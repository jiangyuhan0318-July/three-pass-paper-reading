# Self-check and verification scope

[English home](../README.md) | [中文主页](../README.zh-CN.md) | [完整中文阅读自检](../examples/self-check.zh-CN.md)

Date: **2026-10-25** (Asia/Shanghai).

The repository preserves two separate checks: the original paper-reading session and the preparation of its public GitHub package.

## Original reading session

| Check | Recorded outcome | Evidence |
|---|---|---|
| Fidelity to Keshav's method | Three passes, five Cs, continuation decisions, reconstruction, and survey mode mapped to the supplied 2007 article. Agent-specific additions are identified separately. | [Method provenance](../skills/three-pass-paper-reading/references/method-origin.md) |
| Skill format | The creator's `quick_validate.py` passed twice in the local session. | [Usage log](../examples/usage-log.json) |
| Actual application | Two papers received three-pass reviews, with first-pass decisions and initial reconstructions recorded. | [Process record](../examples/reading-process.zh-CN.md) |
| Text and visual inspection | 31 source pages including the method article; all were rendered, with detailed inspection of key pages. | [Usage log](../examples/usage-log.json) |
| Numerical checks | 36 calculations, including baselines, percentage points, compute ratios, class-average AP, counts, and latency conversions. | [Calculations](../examples/numeric-checks.json) |
| Local artifact links | 15 links resolved in the original local workspace. This is a historical count, not a public-URL check. | [Original check summary](original-session-checks.json) |
| Factual restraint | The reviews distinguish confirmed internal inconsistencies from risks requiring data/code; the agricultural paper's actual 46 ms edge report is retained. | [PCB review](../examples/pcb-defect-detection.zh-CN.md), [agricultural review](../examples/agricultural-detection.zh-CN.md) |

## Public package checks

The public package was checked for:

- A valid skill frontmatter and working skill-reference link.
- An English `README.md` with a working Chinese-language entry and a reciprocal link.
- Repository-relative Markdown file links that resolve within the package.
- Arithmetic output containing the same inputs, formulas, units, and results as the original calculation file when the script is rerun; published text uses LF line endings for portability.
- UTF-8 text and JSON that parse successfully.
- Removal of original machine paths and local account identifiers from the published notes/logs.
- Exclusion of source PDFs, full extracted texts, and rendered page screenshots.
- Consistency between the published skill files and the fingerprints in the source manifest.

The measured results are in [repository-checks.json](repository-checks.json). External sources are linked directly; repository link checks do not guarantee that an external publisher will remain available. The original PDF fingerprints identify the supplied copies, whose bytes may differ from other downloads.

## What this demonstrates

The examples demonstrate that the workflow can produce traceable reading notes, method reconstructions, targeted criticism, and reproducible arithmetic. Two worked examples are practical demonstrations, not a controlled evaluation of the skill's accuracy across research fields.

The original session did not execute the authors' models, reproduce training results, independently benchmark inference, test raw-data leakage, or perform new significance tests. It did not include an independent blind review of the skill. These boundaries are retained in the reports and [machine-readable usage log](../examples/usage-log.json).

## Correct an example

Open a GitHub issue with the paper/version, PDF page and table/figure number, the statement being corrected, and supporting evidence. A model-performance correction should also identify the data split, code/configuration, and evaluation protocol used.
