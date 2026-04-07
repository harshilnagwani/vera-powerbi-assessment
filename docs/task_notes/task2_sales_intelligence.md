# Task 2: Sales Intelligence Dashboard

## Objective
Track revenue, profitability, and sales performance across regions,
categories, and customer segments.

### Dataset — Superstore Sales Dataset
**Source:** [E-commerce retail transactions](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)
**Rows:** ~10,000 | **Purpose:** Track revenue, profitability, and regional performance

| Column | Data Type | Description |
|--------|-----------|-------------|
| Row ID | Whole Number | Unique row identifier |
| Order ID | Text | Unique identifier for each order |
| Order Date | Date | Date the order was placed |
| Ship Date | Date | Date the order was shipped |
| Ship Mode | Text | Shipping method (First Class, Second Class, etc.) |
| Customer ID | Text | Unique identifier for each customer |
| Customer Name | Text | Full name of the customer |
| Segment | Text | Customer segment (Consumer, Corporate, Home Office) |
| Country | Text | Country of the order |
| City | Text | City of the order |
| State | Text | State of the order |
| Region | Text | Geographic region (East, West, Central, South) |
| Product ID | Text | Unique product identifier |
| Category | Text | Product category (Furniture, Office Supplies, Technology) |
| Sub-Category | Text | Product sub-category (Chairs, Binders, Phones, etc.) |
| Product Name | Text | Full name of the product |
| Sales | Decimal | Revenue amount for the line item (USD) |
| Quantity | Whole Number | Number of units sold |
| Discount | Decimal | Discount percentage applied (0.0-1.0) |
| Profit | Decimal | Profit amount for the line item (USD) |
| Profit Margin % | Decimal | Calculated: Profit / Sales * 100 per row |

### Measures — Task 2

| Measure | Description |
|---------|-------------|
| Total Revenue | Total sales revenue across all transactions |
| Total Profit | Total profit across all transactions |
| Profit Margin % | Overall profitability ratio as a percentage |
| Total Orders | Total number of order line items |
| Total Quantity | Total units sold |
| Avg Order Value | Average revenue per transaction line |
| YTD Revenue | Revenue accumulated from Jan 1 to current date |
| MoM Revenue Growth % | Month-over-month percentage change in revenue |
| Top Product Revenue | Revenue of the single best-selling product |

---
## Dashboard Requirements
- [x] Total Revenue KPI card
- [x] Total Profit KPI card
- [x] Profit Margin % KPI card
- [x] YTD Revenue KPI card
- [x] MoM Revenue Growth % KPI card
- [x] Revenue by Category (donut chart)
- [x] Monthly Sales Trend with MoM line (combo chart)
- [x] Region-wise Revenue (map + bar chart)
- [x] Top 10 Products by Revenue (horizontal bar)
- [x] Discount vs Profit scatter chart
- [x] Product Detail drill-through page
- [x] Slicers: Category, Region, Segment, Date range

## Key Insights
1. Technology = 37% of revenue; highest category
2. Furniture shows negative margins due to heavy discounting
3. West region leads all regions in revenue
4. Discounts >30% = near-zero or negative profit
5. Q4 consistently strongest quarter YoY
