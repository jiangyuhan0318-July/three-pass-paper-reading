# Worked examples

[English home](../README.md) | [中文主页](../README.zh-CN.md)

These examples show how the skill was used on two object-detection papers on 2026-10-25. The full reading reports are in Chinese; this page explains the main findings and how to inspect the evidence in English.

## What was actually done

| Activity | PCB paper | Agricultural paper |
|---|---|---|
| Full-text reading | 18 PDF pages | 11 PDF pages |
| Pass 1 | Five Cs and a decision to continue | Five Cs and a decision to continue |
| Pass 2 | Methods, experimental conditions, figures 1–6, tables 1–4 | Methods, experimental conditions, figures 1–7, tables I–V |
| Pass 3 | Initial method reconstruction, source comparison, corrections, critical appraisal | Initial TPS/STN/CBAM reconstruction, source comparison, corrections, critical appraisal |
| Detailed page-image inspection | Pages 2, 5, 7–12, 14–15 | Pages 1, 3, 5–10 |
| Full model replication | Not performed | Not performed |

Both papers were rendered and visually surveyed in full. Together with Keshav's two-page article, the reading used **31 source PDF pages**. The [process record](reading-process.zh-CN.md) preserves the first-pass decisions and the initial reconstructions written before the detailed comparison.

## Example A — PCB defect detection

**Zhe Sun, Ruihan Ma, and Qujiang Lei. _Small PCB Defect Detection Based on Convolutional Block Attention Mechanism and YOLOv8_. Applied Sciences 16, 1078 (2026).**

[Paper](https://doi.org/10.3390/app16021078) · [Full Chinese review](pcb-defect-detection.zh-CN.md)

### Reconstruct the idea

The paper integrates channel and spatial attention into YOLOv8 backbone features at P3/P4/P5, with the stated aim of highlighting small, low-contrast PCB defects before multi-scale fusion. The review reconstructs the CBAM operations, tensor shapes, training setup, and places where the implementation is underspecified. See paper pp.5–10 and the report's third-pass section.

### Keep the denominator and baseline visible

Paper p.14 contains two different reference rows:

| Comparison | Baseline mAP@50 | Proposed mAP@50 | Recalculated difference |
|---|---:|---:|---:|
| Table 3: “YOLOv8 CBAM + CIoU” | 89.3% | 98.8% | +9.5 percentage points |
| Table 4: “YOLOv8” | 95.5% | 98.8% | +3.3 percentage points |

Both subtractions are correct; they answer different comparisons. Table 4 also reports 8.1 versus 79.4 GFLOPs, a ratio of about **9.80×**. This makes model scale and computational accounting central to interpreting the claimed attention benefit. It does not by itself identify the cause of the difference.

### Trace inconsistencies to their sources

- On pp.13–14, the prose reverses the EIoU/SIoU mAP gains: the table gives **5.6** and **7.1** percentage points, respectively.
- The data statement on p.17 links to SSGD, whose maintainer describes smartphone screen-glass defects, while §3.1 describes the PKU PCB dataset. The review links both original dataset sources.
- The standard Ultralytics v8.3.0 model configuration has no CBAM, making the paper's “built-in CBAM” terminology important to clarify. The review identifies the exact official version inspected instead of assuming which version the authors ran.
- The paper argues for fusion-before/after placement choices, but the reported ablation does not isolate those positions. The proposed next check fixes model size, data, and training conditions before comparing placements.

**Reading lesson:** attach each improvement to its baseline and resource cost. A strong overall score and a clear architectural intuition do not isolate the mechanism on their own.

## Example B — agricultural detection

**Satvik Praveen and Yoonsung Jung. _CBAM-STN-TPS-YOLO: Enhancing Agricultural Object Detection through Spatially Adaptive Attention Mechanisms_. arXiv:2506.07357v1 (2025-06-09).**

[Paper and version](https://arxiv.org/abs/2506.07357v1) · [Full Chinese review](agricultural-detection.zh-CN.md)

### Reconstruct the idea

The intended pipeline replaces the affine transformation inside an STN with a thin-plate-spline mapping, adds CBAM, and applies YOLO detection. A useful reconstruction must specify the localization network, control points, mapping direction, sampler, feature placement, and relationship between predicted boxes and original-image labels. The paper leaves several of these details unresolved; the review separates those missing specifications from a demonstrated implementation error. See paper pp.3–7.

### Calculate what the main table supports

From paper p.9, table V:

| Dataset | STN-YOLO mAP | Full model mAP | Recalculated difference |
|---|---:|---:|---:|
| PGP | 72.56±0.90 | 73.71±0.85 | +1.15 percentage points |
| MelonFlower | 45.09±3.31 | 47.24±2.95 | +2.15 percentage points |

The values are reported means and standard deviations across three runs. The paper does not clearly define the IoU threshold/range for “mAP,” so these numbers are retained under their original label and are not compared with the PCB paper's mAP@50.

### Examine the unit of evidence

- Tables IV and V give different PGP results without explaining the change in conditions. For the full model, mAP is 72.61 in table IV and 73.71 in table V.
- The significance analysis on pp.9–10 uses paired measurements across 100 training epochs. Successive epochs share an optimization history and can be correlated; this does not supply 100 independent training repetitions. The review requests run-level evidence and does not invent replacement p-values.
- The abstract's “12% reduction in false positives” lacks a traceable count/threshold calculation. Precision alone does not determine the change in absolute false-positive counts.
- The abstract/introduction promise a TPS-regularization analysis, but the supplied version gives no corresponding parameter sweep or result table.
- The review retains the author's actual edge-deployment report: **46 ms per frame on Jetson Xavier with TensorRT** (p.6), equivalent to about 21.74 FPS. It asks for the measurement protocol rather than describing edge deployment as absent.

**Reading lesson:** understand which observations are independent, what a table actually measures, and which implementation details are needed before accepting a causal explanation.

## Reproduce the arithmetic

From the repository root:

```bash
python examples/numeric_checks.py
```

The script uses the Python standard library and rewrites [numeric-checks.json](numeric-checks.json). Its **36 calculations** cover reported deltas, relative changes, compute ratios, class-average AP, image counts, latency/FPS conversion, and descriptive ablation contrasts. Each calculation records a paper/table locator and its unit. A descriptive interaction contrast is not a statistical interaction test.

The inputs are manually transcribed values checked against the rendered papers. Re-running the script verifies the arithmetic, not the source experiments or the transcription by itself.

## Audit trail and scope

- [Full Chinese self-check](self-check.zh-CN.md): method fidelity, execution, source checks, and unresolved questions.
- [Usage log](usage-log.json): the depth actually reached and checks performed.
- [Source fingerprints](source-manifest.json): hashes of the exact locally supplied PDF copies, plus the published skill files. Online PDFs may differ at the byte level.
- [Original local-session checks](../validation/original-session-checks.json): historical verification of the local artifacts.
- [Publication self-check](../validation/SELF-CHECK.md): the separate portability, link, and packaging checks for this repository.

The examples are AI-assisted critical readings. Model training, independent inference measurements, data-leakage tests, and new significance tests were not performed. The reports distinguish internal inconsistencies that can be checked in the paper from hypotheses that still need code or data.
