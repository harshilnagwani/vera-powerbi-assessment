# Raw Data


## Files

| File | Task | Rows | Notes |
|------|------|------|-------|
| `course_completion.csv` | Task 1 — User Intelligence | ~1,000 | No pre-processing needed |
| `superstore_sales.csv` | Task 2 — Sales Intelligence | ~10,000 | No pre-processing needed |
| `Delivery_Logistics.csv` | Task 3 — Operations Intelligence | 25,000 | Run `fix_operations_timestamps.py` |
| `HRDataset_v14.csv` | Task 4 — HR Intelligence | 311 | Run `clean_hr_dataset.py` |

## Notes

- Raw files are excluded from Git tracking (see `.gitignore`) to keep the repo lightweight.
- The Operations dataset contains corrupted timestamp columns — this is a known data quality issue resolved by the pre-processing script.
- HRDataset_v14 is the publicly available dataset from Kaggle by Dr. Rich Huebner.
