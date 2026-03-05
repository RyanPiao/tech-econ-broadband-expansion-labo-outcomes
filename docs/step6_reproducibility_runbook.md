# Step 6 — Reproducibility Runbook

## Purpose
This runbook defines a repeatable Step2-Step7 execution path for the Stage-X broadband-labor repository.

## Environment
- Python 3.9+ (tested in project `.venv`)
- Dependencies pinned in `requirements.txt`
- Network access required for ACS API pulls in Step 2

## Quick start (full rerun)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_step2_step7.py
```

## Stage-by-stage execution
```bash
python scripts/step2_ingest_build_panel.py
python scripts/step3_eda.py
python scripts/step4_baseline_model.py
python scripts/step5_robustness_sensitivity.py
python scripts/step6_reproducibility_polish.py
python scripts/step7_stagely_recap.py
```

## Reproducibility outputs to verify
- `outputs/step6_artifact_manifest.csv`
- `outputs/step6_requirements_snapshot.csv`
- `outputs/step6_run_metadata.json`
- `docs/step7_stagely_recap.md`

## Troubleshooting
1. **ACS API timeout/rate limits**
   - Re-run Step 2; source pulls are idempotent.
2. **Package mismatch errors**
   - Recreate `.venv` and reinstall from `requirements.txt`.
3. **Missing Step5/Step6 files**
   - Run scripts in order; Step 7 depends on Step 5 and Step 6 outputs.
