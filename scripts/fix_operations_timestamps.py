#!/usr/bin/env python3


import pandas as pd
import numpy as np
import os

RAW_PATH = "data/raw/Delivery_Logistics.csv"
OUT_PATH = "data/processed/Delivery_Logistics_Clean.csv"


def fix_timestamp_column(series: pd.Series) -> pd.Series:
    """Extract integer hour from corrupted nanosecond timestamp string."""
    s = series.astype(str).str.strip()
    try:
        return pd.to_numeric(s)
    except ValueError:
        pass
    extracted = s.str.extract(r"(\d+)$")[0]
    return pd.to_numeric(extracted, errors="coerce").fillna(0).astype(int)


def engineer_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add calculated columns used in Power BI."""
    df["delay_hours"] = df["delivery_time_hours"] - df["expected_time_hours"]
    df["status_label"] = (
        df["delayed"].str.strip().str.lower()
        .map({"yes": "Delayed", "no": "On Time"})
        .fillna("On Time")
    )
    # Synthetic delivery date for time-series trending (2023-2024)
    df["delivery_date"] = pd.to_datetime("2023-01-01") + pd.to_timedelta(
        df["delivery_id"] % 730, unit="D"
    )
    df["delivery_date"] = df["delivery_date"].dt.strftime("%Y-%m-%d")
    return df


def main():
    print(f"Reading: {RAW_PATH}")
    df = pd.read_csv(RAW_PATH)
    print(f"  Rows loaded: {len(df):,}")

    for col in ["delivery_time_hours", "expected_time_hours"]:
        if df[col].dtype == object:
            print(f"  Fixing corrupted column: {col}")
            df[col] = fix_timestamp_column(df[col])
        else:
            print(f"  Column {col} already numeric — skipping fix")

    df = engineer_columns(df)
    print("  Engineered columns: delay_hours, status_label, delivery_date")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}  ({len(df):,} rows)")

    print("\nQA Summary:")
    print(f"  On Time Rate : {(df['status_label']=='On Time').mean()*100:.2f}%")
    print(f"  Delay Rate   : {(df['status_label']=='Delayed').mean()*100:.2f}%")
    print(f"  Avg delivery_time_hours : {df['delivery_time_hours'].mean():.2f}")
    print(f"  Avg expected_time_hours : {df['expected_time_hours'].mean():.2f}")
    print(f"  Avg delay_hours (delayed only): "
          f"{df.loc[df['delay_hours']>0,'delay_hours'].mean():.2f}")


if __name__ == "__main__":
    main()
