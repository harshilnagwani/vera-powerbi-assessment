#!/usr/bin/env python3
"""
clean_hr_dataset.py
-------------------
Engineers calculated columns for the HR dataset (HRDataset_v14.csv)
before loading into Power BI.

Columns Added:
    - Status              : "Active" or "Terminated"
    - Attrition_Flag      : 1 = Terminated, 0 = Active
    - PerformanceScore_Num: Numeric mapping (Exceeds=4, etc.)
    - Tenure_Years        : Years of service
    - Age                 : Age vs 2024-01-01
    - Hire_Year           : Year of DateofHire
    - Hire_Month          : YYYY-MM format

Usage:
    python scripts/clean_hr_dataset.py

Output:
    data/processed/HR_Clean.csv
"""

import pandas as pd
import os

RAW_PATH = "data/raw/HRDataset_v14.csv"
OUT_PATH = "data/processed/HR_Clean.csv"
REFERENCE_DATE = pd.Timestamp("2024-01-01")

PERF_MAP = {
    "Exceeds": 4,
    "Fully Meets": 3,
    "Needs Improvement": 2,
    "PIP": 1,
}


def clean_hr(df: pd.DataFrame) -> pd.DataFrame:
    df["Status"] = df["EmploymentStatus"].apply(
        lambda x: "Active" if "Active" in str(x) else "Terminated"
    )
    df["Attrition_Flag"] = (df["Status"] == "Terminated").astype(int)
    df["PerformanceScore_Num"] = (
        df["PerformanceScore"].map(PERF_MAP).fillna(0).astype(int)
    )
    df["DateofHire"] = pd.to_datetime(df["DateofHire"], errors="coerce")
    df["DateofTermination"] = pd.to_datetime(
        df["DateofTermination"], errors="coerce"
    )
    df["DOB"] = pd.to_datetime(df["DOB"], errors="coerce")

    end_date = df["DateofTermination"].fillna(REFERENCE_DATE)
    df["Tenure_Years"] = (
        (end_date - df["DateofHire"]).dt.days / 365.25
    ).round(2)

    df["Age"] = (
        (REFERENCE_DATE - df["DOB"]).dt.days / 365.25
    ).round(0).astype("Int64")

    df["Hire_Year"] = df["DateofHire"].dt.year
    df["Hire_Month"] = df["DateofHire"].dt.strftime("%Y-%m")
    return df


def main():
    print(f"Reading: {RAW_PATH}")
    df = pd.read_csv(RAW_PATH)
    print(f"  Rows loaded: {len(df):,}")

    df = clean_hr(df)
    print("  Engineered: Status, Attrition_Flag, PerformanceScore_Num,")
    print("              Tenure_Years, Age, Hire_Year, Hire_Month")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}  ({len(df):,} rows)")

    print("\nQA Summary:")
    print(f"  Total Employees : {len(df):,}")
    print(f"  Active          : {(df['Status']=='Active').sum():,}")
    print(f"  Terminated      : {(df['Status']=='Terminated').sum():,}")
    print(f"  Attrition Rate  : {df['Attrition_Flag'].mean()*100:.2f}%")
    print(f"  Avg Tenure (yr) : {df['Tenure_Years'].mean():.2f}")
    print(f"  Avg Age         : {df['Age'].mean():.1f}")


if __name__ == "__main__":
    main()
