# Tech-Econ Weekly Lab Run (Week X)
## Broadband Expansion × Labor Outcomes

This repository now contains the **full Day2-Day7 continuation** for the approved Day-1 framing.

## Start here (primary single-page overview)
- **Executive summary:** [`docs/weekX_executive_summary.md`](docs/weekX_executive_summary.md)
- Website abstract source: [`docs/weekX_website_abstract.md`](docs/weekX_website_abstract.md)

## Scope completed in this run

### Executive summary
- `docs/weekX_executive_summary.md`

- ✅ **Day 2**: ingestion/spec lock/QA + analysis-ready county-year panel
- ✅ **Day 3**: EDA notebook + exploratory outputs
- ✅ **Day 4**: baseline FE model + event-study diagnostics
- ✅ **Day 5**: robustness/sensitivity package + limitations register
- ✅ **Day 6**: reproducibility polish (manifest, requirements snapshot, runbook)
- ✅ **Day 7**: weekly recap report suitable for website research summary

---

## Day-1 must-fix closure (applied before modeling)
- `docs/day2_preanalysis_lock.md`
- `docs/day2_data_extraction_spec.md`
- `docs/day2_data_qa_checklist.md`

---

## Data used
### Public real data (active)
- U.S. Census ACS 5-year API (county-year, 2017-2023)

### Blocked component and fallback
- **Blocked in Week-X:** harmonized historical FCC Form-477/BDC county availability panel.
- **Fallback used:** ACS household broadband subscription share (`B28002_004E / B28002_001E`) as treatment proxy.
- **Synthetic data:** not used.

---

## Repository structure

```text
.
├── README.md
├── PLAN.md
├── DAY1_problem_framing.md
├── DAY1_review.md
├── requirements.txt
├── data_raw/
├── data_intermediate/
├── data_analysis/
├── docs/
│   ├── day2_*.md
│   ├── day3_eda_note.md
│   ├── day4_interpretation_notes.md
│   ├── day5_robustness_limitations.md
│   ├── day6_reproducibility_runbook.md
│   ├── day6_reproducibility_checklist.md
│   └── day7_weekly_recap.md
├── notebooks/
├── outputs/
└── scripts/
    ├── day2_ingest_build_panel.py
    ├── day3_eda.py
    ├── day4_baseline_model.py
    ├── day5_robustness_sensitivity.py
    ├── day6_reproducibility_polish.py
    ├── day7_weekly_recap.py
    ├── run_day2_day4.py
    └── run_day2_day7.py
```

---

## Reproducibility

### Full rerun
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_day2_day7.py
```

### Reproducibility package outputs
- `outputs/day6_artifact_manifest.csv`
- `outputs/day6_requirements_snapshot.csv`
- `outputs/day6_run_metadata.json`
- `docs/day6_reproducibility_runbook.md`

---

## Day5-Day7 core artifacts

### Day 5 (robustness/sensitivity + limitations)
- `outputs/day5_robustness_sensitivity.csv`
- `outputs/day5_limitations_register.csv`
- `docs/day5_robustness_limitations.md`

### Day 6 (reproducibility polish)
- `outputs/day6_artifact_manifest.csv`
- `outputs/day6_requirements_snapshot.csv`
- `outputs/day6_run_metadata.json`
- `docs/day6_reproducibility_runbook.md`
- `docs/day6_reproducibility_checklist.md`

### Day 7 (weekly recap)
- `docs/day7_weekly_recap.md`
- `outputs/day7_website_summary.txt`
- `outputs/day7_recap_metadata.json`
