"""Recalculate visually checked paper-table values; no model training/replication."""
from pathlib import Path
import json

checks = []


def delta(label, source, baseline, proposed, unit="percentage_points"):
    result = {"label": label, "source": source, "baseline": baseline,
              "proposed": proposed, "formula": "proposed - baseline",
              "value": proposed - baseline, "unit": unit}
    if baseline:
        result["relative_change_percent"] = (proposed / baseline - 1) * 100
    checks.append(result)


def value(label, source, expression, result, unit):
    checks.append({"label": label, "source": source, "formula": expression,
                   "value": result, "unit": unit})


for metric, base, new in [("mAP50", 89.3, 98.8), ("P", 90.8, 98.2), ("R", 85.0, 97.3)]:
    delta("A Table3 CIoU " + metric, "A p14 Table3", base, new)
for metric, base, new in [("mAP50", 95.5, 98.8), ("P", 95.3, 98.2), ("R", 93.9, 97.3)]:
    delta("A Table4 YOLOv8 " + metric, "A p14 Table4", base, new)
delta("A EIoU mAP50", "A p14 Table3", 90.2, 95.8)
delta("A SIoU mAP50", "A p14 Table3", 91.1, 98.2)
value("A compute ratio Table3", "A p14 Table3", "79.4 / 8.2", 79.4 / 8.2, "times")
value("A compute ratio Table4", "A p14 Table4", "79.4 / 8.1", 79.4 / 8.1, "times")
delta("A throughput Table3", "A p14 Table3; interpreted as FPS from prose", 132.46, 109.11, "FPS")
delta("A throughput Table4", "A p14 Table4; interpreted as FPS from prose", 124, 109.11, "FPS")
value("A proposed latency", "A p14 Table4; FPS interpretation", "1000 / 109.11", 1000 / 109.11, "ms_per_image")
ap50 = [0.992, 0.990, 0.985, 0.982, 0.986, 0.991]
ap5095 = [0.654, 0.611, 0.597, 0.632, 0.590, 0.630]
value("A class mean mAP50", "A p12 Table2 rounded class entries", "mean(class_AP50) * 100", sum(ap50) / 6 * 100, "percent")
value("A class mean mAP50_95", "A p12 Table2 rounded class entries", "mean(class_AP50_95) * 100", sum(ap5095) / 6 * 100, "percent")
value("A original images in Figure6", "A p15 Figure6", "116+115+116+116+115+115", 116+115+116+116+115+115, "images")
value("A augmented images in Figure6", "A p15 Figure6", "696+695+696+746+687+690", 696+695+696+746+687+690, "images")

for dataset, baseline, stn, tps, cbam, full in [
    ("PGP", 71.76, 72.56, 73.01, 72.87, 73.71),
    ("MelonFlower", 44.91, 45.09, 46.23, 46.77, 47.24),
]:
    delta("B " + dataset + " full vs YOLO mAP", "B p9 TableV; mAP IoU definition unspecified", baseline, full)
    delta("B " + dataset + " full vs STN mAP", "B p9 TableV", stn, full)
    delta("B " + dataset + " TPS vs STN mAP", "B p9 TableV", stn, tps)
    delta("B " + dataset + " CBAM vs STN mAP", "B p9 TableV", stn, cbam)
    value("B " + dataset + " descriptive interaction", "B p9 TableV; not a significance test",
          "full - tps - cbam + stn", full - tps - cbam + stn, "percentage_points")
delta("B PGP full vs YOLO accuracy", "B p9 TableV; accuracy definition unspecified", 84.86, 83.24)
delta("B PGP CBAM vs STN precision", "B p9 TableV", 95.34, 95.11)
delta("B PGP full vs STN precision", "B p9 TableV", 95.34, 96.27)
delta("B PGP full vs STN recall", "B p9 TableV", 89.52, 90.28)
delta("B PGP full vs YOLO latency", "B p9 TableV", 16.25, 14.22, "ms_per_image")
delta("B PGP full vs STN latency", "B p9 TableV", 16.92, 14.22, "ms_per_image")
value("B Jetson Xavier equivalent FPS", "B p6 III-F; author-reported mean latency", "1000 / 46", 1000 / 46, "FPS")
value("B TableV PGP false discovery rate decrease", "B p9 TableV; FDR is not raw FP count",
      "((100-95.34)-(100-96.27))/(100-95.34)*100",
      ((100-95.34)-(100-96.27))/(100-95.34)*100, "percent_relative_FDR_reduction")
value("B PGP crop counts", "B p4 III-A1", "442+246+449", 442+246+449, "images")

out = Path(__file__).with_name("numeric-checks.json")
with out.open("w", encoding="utf-8", newline="\n") as stream:
    json.dump({"scope": "Arithmetic only; transcribed values checked against rendered tables",
               "checks": checks}, stream, ensure_ascii=False, indent=2)
for item in checks:
    print(f'{item["label"]}: {item["value"]:.6f} {item["unit"]}')
print(f"Saved {len(checks)} checks to {out}")
