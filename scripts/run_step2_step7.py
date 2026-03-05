#!/usr/bin/env python3
"""Run Step2-Step7 pipeline in order."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

STEPS = [
    "scripts/step2_ingest_build_panel.py",
    "scripts/step3_eda.py",
    "scripts/step4_baseline_model.py",
    "scripts/step5_robustness_sensitivity.py",
    "scripts/step6_reproducibility_polish.py",
    "scripts/step7_stagely_recap.py",
]


def main() -> None:
    for step in STEPS:
        print(f"\n=== Running {step} ===")
        subprocess.run([sys.executable, str(PROJECT_ROOT / step)], check=True)
    print("\nDay2-Step7 pipeline complete.")


if __name__ == "__main__":
    main()
