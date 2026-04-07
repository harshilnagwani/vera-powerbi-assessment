# Task 3: Operations Intelligence Dashboard

## Objective
Optimize delivery operations by identifying delay bottlenecks,
measuring partner performance, and tracking cost efficiency.

## Dataset
Delivery_Logistics_Clean.csv — 25,000 delivery records (pre-processed).

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

## Bottlenecks Found
- Stormy weather: 41.45% delay rate (2.6x above clear weather)
- Rainy weather: 37.35% delay rate
- All regions within 1.45pp — geography NOT the bottleneck
- 5.3% failed deliveries (1,328 records)
