# Task 4: HR Intelligence Dashboard

## Objective
Analyze workforce composition, attrition patterns, and performance
distribution to support people strategy decisions.

### Dataset — Human Resources Data Set
**Source:** [HR management system export (fictional US company)](https://www.kaggle.com/datasets/rhuebner/human-resources-data-set)
**Rows:** 311 employees | **Columns:** 29 cleaned (from 36 original)
**Purpose:** Analyze workforce composition, attrition drivers, and performance

| Column | Data Type | Description |
|--------|-----------|-------------|
| EmpID | Whole Number | Unique employee identifier |
| Employee_Name | Text | Full name of the employee (Last, First format) |
| Sex | Text | Gender of the employee (M / F) |
| Department | Text | Department (Production, IT/IS, Sales, Software Engineering, Admin Offices, Executive Office) |
| Position | Text | Job title / role of the employee |
| ManagerName | Text | Name of the employee's direct manager |
| DateofHire | Date | Date the employee joined the company |
| DateofTermination | Date | Date the employee left (null for active employees — correct, not missing) |
| Hire_Year | Whole Number | ENGINEERED: Year extracted from DateofHire for hiring trend chart |
| Hire_Month | Text | ENGINEERED: YYYY-MM string for monthly hiring trend |
| EmploymentStatus | Text | Detailed status (Active, Voluntarily Terminated, Terminated for Cause) |
| Status | Text | ENGINEERED: Simplified — "Active" or "Terminated" |
| Attrition_Flag | Whole Number | ENGINEERED: Binary — 1 = Terminated, 0 = Active |
| TermReason | Text | Reason for leaving (e.g., Another position, Unhappy, More money) |
| Salary | Whole Number | Annual salary in USD |
| PerformanceScore | Text | Qualitative rating (Exceeds, Fully Meets, Needs Improvement, PIP) |
| PerformanceScore_Num | Whole Number | ENGINEERED: Exceeds=4, Fully Meets=3, Needs Improvement=2, PIP=1 |
| EngagementSurvey | Decimal | Engagement survey score (1.0-5.0 scale) |
| EmpSatisfaction | Whole Number | Employee satisfaction rating (1-5 scale) |
| DaysLateLast30 | Whole Number | Days late in the last 30 days (attendance signal) |
| Absences | Whole Number | Total absences recorded |
| SpecialProjectsCount | Whole Number | Number of special projects participated in |
| RecruitmentSource | Text | Hiring channel (LinkedIn, Indeed, Google Search, Employee Referral, etc.) |
| Age | Whole Number | ENGINEERED: Calculated from DOB vs reference date 2024-01-01 |
| Tenure_Years | Decimal | ENGINEERED: Years from DateofHire to exit date (or 2024-01-01 for active) |
| State | Text | US state where the employee is located |
| MaritalDesc | Text | Marital status (Single, Married, Divorced, Separated, Widowed) |
| RaceDesc | Text | Race/ethnicity description |
| Termd | Whole Number | Original binary termination flag from source (1 = terminated) |

### Measures — Task 4

| Measure | Description |
|---------|-------------|
| Total Employees | Total headcount including active and terminated employees (311) |
| Active Employees | Current active headcount (207 employees — 66.6%) |
| Terminated Employees | Total employees who left the company (104 employees — 33.4%) |
| Attrition Rate % | Percentage of total employees who left — company-wide (33.44%) |
| Retention Rate % | Inverse of attrition — employees still active (66.56%) |
| Avg Performance Score | Average numeric performance score (1-4 scale) |
| Avg Engagement Score | Average engagement survey score (1-5 scale) |
| Avg Satisfaction | Average employee satisfaction rating (1-5 scale) |
| Avg Salary | Average annual salary in USD ($69,020 company-wide) |
| Avg Tenure (Years) | Average years of service across all employees |
| Top Performers | Count of employees rated "Exceeds" (37 employees — 10%) |
| At Risk Employees | Count of employees on PIP or Needs Improvement (31 employees) |
| Monthly New Hires | Month-to-date new hires for hiring trend time series (DATESMTD) |
| Dept Attrition Rate % | Attrition rate within each department context (ALLEXCEPT filter) |
| YoY Hiring Growth % | Year-over-year change in new hires using DATEADD |
## Dashboard Requirements
- [x] Total Employees KPI card
- [x] Active Employees KPI card
- [x] Attrition Rate % KPI card
- [x] Avg Salary KPI card
- [x] Avg Engagement Score KPI card
- [x] Attrition by Department (bar chart)
- [x] Performance Score distribution (donut chart)
- [x] Hiring Trend over time (line chart)
- [x] Salary vs Performance scatter (bubble chart)
- [x] Termination Reasons breakdown (bar chart)
- [x] Recruitment Source analysis (bar chart)
- [x] Employee Detail drill-through page
- [x] Row-Level Security: HR_Production, HR_IT, HR_Sales
- [x] Slicers: Department, Status, PerformanceScore, Date range

## Key Insights
1. 33.44% attrition — 2x above healthy benchmark
2. Production: 39.71% attrition, lowest avg salary
3. Sales: 16.13% attrition despite below-avg salary
4. Top 3 exit reasons = 43% of all terminations (all preventable)
5. 27% of all hires concentrated in 2011 alone
