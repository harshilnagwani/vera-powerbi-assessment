# Architecture & Data Model Design

## Overview

The VERA Power BI report uses a **Star Schema** data model with a single shared
Date dimension (`DateTable`) connected to three fact tables.

## Data Model Diagram

```
DateTable (Date)
    |
    ├──► Sales[Order Date]          (One-to-Many · Active)
    ├──► Operations[delivery_date]  (One-to-Many · Active)
    └──► HR[DateofHire]             (One-to-Many · Active)

Course_Completion (independent — no date relationship needed for Task 1)
```

## Design Decisions

### 1. Single Shared DateTable
Rather than auto-generating date tables per dataset, one centralised
`DateTable = CALENDAR(DATE(2006,1,1), DATE(2024,12,31))` covers all domains.
This ensures consistent time-intelligence calculations and reduces model complexity.

### 2. Centralised Measures Table
All DAX measures live in a single `_Measures` table organised by Display Folders:
- `Task 1 - User Intelligence`
- `Task 2 - Sales Intelligence`
- `Task 3 - Operations Intelligence`
- `Task 4 - HR Intelligence`

### 3. Pre-processing Outside Power BI
The Operations and HR datasets required non-trivial transformations (timestamp
extraction, binary flag engineering) that are cleaner in Python than Power Query M.
Power Query is then used only for final type-casting and relationship setup.

### 4. Row-Level Security (Static)
Static RLS using `[Column] = "Value"` filters was chosen over dynamic
`USERPRINCIPALNAME()` RLS because the assessment environment uses a free Power BI
Service account without Azure AD user provisioning. See `rls_design.md` for extension path.

## Report Page Architecture

| Page | Type | Connected Tables |
|------|------|------------------|
| Home | Navigation | None |
| User Intelligence | Main | Course_Completion |
| Sales Intelligence | Main | Sales, DateTable |
| Product Detail | Drill-Through | Sales |
| Operations Intelligence | Main | Operations, DateTable |
| HR Intelligence | Main | HR, DateTable |
| HR Intelligence-2 | Support | HR |
| Employee Detail | Drill-Through | HR |
| Tooltip_User | Tooltip | Course_Completion |
| Tooltip_Operations | Tooltip | Operations |

## Power Query Steps per Dataset

### Operations (Delivery_Logistics_Clean.csv)
1. Import CSV from `data/processed/`
2. Set `delivery_time_hours` → Whole Number
3. Set `expected_time_hours` → Whole Number
4. Set `delivery_date` → Date
5. Set `delivery_cost` → Decimal Number
6. Rename query to `Operations`

### HR (HR_Clean.csv)
1. Import CSV from `data/processed/`
2. Set `DateofHire`, `DateofTermination` → Date
3. Set `Salary`, `EmpID`, `Attrition_Flag` → Whole Number
4. Set `EngagementSurvey`, `Tenure_Years` → Decimal Number
5. Rename query to `HR`
