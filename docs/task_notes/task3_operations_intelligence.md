# Task 3: Operations Intelligence Dashboard

## Objective
Optimize delivery operations by identifying delay bottlenecks,
measuring partner performance, and tracking cost efficiency.

### Dataset — Delivery _Logistics...dataset
**Source:** [Multi-partner delivery logistics platform (India)](https://www.kaggle.com/datasets/ayeshaseherr/delivery-logistics-dataset)
**Rows:** 25,000 | **Columns:** 18 (15 original + 3 engineered)
**Purpose:** Track delivery performance, identify delay bottlenecks, measure partner efficiency

| Column | Data Type | Description |
|--------|-----------|-------------|
| delivery_id | Whole Number | Unique identifier for each delivery record |
| delivery_partner | Text | Delivery company name (9 partners: Delhivery, FedEx, DHL, Ekart, BlueDart, XpressBees, Shadowfax, Ecom Express, Amazon Logistics) |
| package_type | Text | Type of package (Electronics, Groceries, Fragile Items, Pharmacy, Documents, Clothing, Furniture, Cosmetics, Automobile Parts) |
| vehicle_type | Text | Vehicle used (EV Bike, Van, Scooter, Bike, Truck, EV Van) |
| delivery_mode | Text | Service level (Same Day, Express, Two Day, Standard) |
| region | Text | Delivery region (West, Central, South, North, East) |
| weather_condition | Text | Weather at time of delivery (Clear, Rainy, Foggy, Stormy, Cold, Hot) |
| distance_km | Decimal | Distance from warehouse to delivery location in kilometres |
| package_weight_kg | Decimal | Weight of the package in kilograms |
| delivery_time_hours | Whole Number | CLEANED: Actual hours taken to complete delivery (range: 0-19 hrs) |
| expected_time_hours | Whole Number | CLEANED: Promised SLA delivery hours (range: 2-24 hrs) |
| delayed | Text | Binary delay flag from source data ("yes" / "no") |
| delivery_status | Text | Final delivery outcome ("delivered", "delayed", "failed") |
| delivery_rating | Whole Number | Customer rating for the delivery (1-5 scale) |
| delivery_cost | Decimal | Cost of the delivery in INR |
| delay_hours | Whole Number | ENGINEERED: delivery_time_hours minus expected_time_hours (positive = late) |
| status_label | Text | ENGINEERED: "On Time" or "Delayed" (mapped from delayed column) |
| delivery_date | Date | ENGINEERED: Synthetic 2023-2024 date for time-series trend analysis |

> **Data Quality Note:** The original delivery_time_hours and expected_time_hours
> were stored as corrupted Unix timestamp strings. The actual integer hour values
> were encoded in the nanosecond digits and extracted via Python pre-processing.

### Measures — Task 3

| Measure | Description |
|---------|-------------|
| Total Deliveries | Total number of delivery records in the dataset |
| On Time Deliveries | Count of deliveries completed within the SLA |
| Delayed Deliveries | Count of deliveries that exceeded expected delivery time |
| Failed Deliveries | Count of deliveries never completed (delivery_status = "failed") |
| On Time Rate % | Percentage of all deliveries completed on time (73.32%) |
| Delay Rate % | Percentage of all deliveries that were late (26.68%) |
| Avg Delivery Time (hrs) | Average actual delivery time across all records |
| Avg Expected Time (hrs) | Average promised SLA delivery time across all records |
| Avg Delay (hrs) | Average delay in hours for delayed deliveries only |
| Total Cost | Total delivery cost in INR across all records |
| Avg Delivery Cost | Average cost per delivery |
| Avg Delivery Rating | Average customer satisfaction score (1-5 scale) |
| Monthly Delay Rate % | Month-to-date delay rate for trend line (DATESMTD) |

### Bottlenecks Identified

**Bottleneck 1 — Weather Condition (Primary Driver)**

| Weather | Delay Rate | vs Overall Avg (26.68%) |
|---------|------------|-------------------------|
| Stormy | 41.45% | +14.77 pp above avg |
| Rainy | 37.35% | +10.67 pp above avg |
| Foggy | 30.32% | +3.64 pp above avg |
| Clear | 17.43% | -9.25 pp below avg |
| Hot | 17.12% | -9.56 pp below avg |
| Cold | 16.02% | -10.66 pp below avg |

Stormy conditions cause 2.6x more delays than clear weather.

**Bottleneck 2 — Regional Uniformity (No Geographic Bottleneck)**
All 5 regions have delay rates between 25.80% and 27.25% (only 1.45 pp range).
Geography is NOT the bottleneck — weather and partner-level factors are.

**Bottleneck 3 — Delivery Partner Accountability**
XpressBees has the lowest customer rating (3.61/5). Partner matrix enables
direct accountability tracking across Delay Rate %, Rating, and Cost.

**Bottleneck 4 — Failed Deliveries**
1,328 records (5.3%) show delivery_status = "failed" — complete non-delivery
events costlier than delays in terms of customer impact.

## Data Quality Fix
Original `delivery_time_hours` and `expected_time_hours` were corrupted
Unix timestamp strings. Hour values extracted from nanosecond digits
using `scripts/fix_operations_timestamps.py`.

## Dashboard Requirements
- [x] Total Deliveries KPI card
- [x] On Time Rate % KPI card
- [x] Delay Rate % KPI card
- [x] Avg Delivery Rating KPI card
- [x] Total Cost KPI card
- [x] On Time vs Delayed donut chart
- [x] Region-wise stacked bar (On Time vs Delayed)
- [x] Delay Rate by Weather Condition (column chart)
- [x] Monthly Volume vs Delay Rate % (combo chart)
- [x] Partner Performance matrix (conditional formatting)
- [x] Delay by Vehicle Type (bar chart)
- [x] Python heatmap: Region x Vehicle Type delay rate
- [x] Slicers: region, delivery_mode, weather_condition, date range

### Key Insights
- Overall: 73.32% on-time rate — 1 in 4 deliveries is late
- Weather is the root cause: stormy + rainy together account for majority
  of avoidable delays; proactive weather-based dispatch could reduce delays
  by an estimated 10-15 percentage points
- Vehicle type is NOT a bottleneck: all 6 types within 1% of each other
  (26.14%-27.04%), ruling out fleet composition as a cause
- Many "on-time" deliveries have delay_hours near zero, indicating systemic
  under-resourcing rather than genuine operational efficiency
- All 9 partners perform within 0.09 rating points — market is homogeneous
  at macro level but individual accountability matters for contracts

---
