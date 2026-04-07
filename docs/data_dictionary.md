# Data Dictionary

Column-level documentation for all four datasets.

---

## Task 1: Course_Completion

| Column | Type | Description |
|--------|------|-------------|
| EmployeeID | Whole Number | Unique identifier for each learner |
| Employee_Name | Text | Full name of the learner |
| Department | Text | Department the learner belongs to |
| Course_Title | Text | Name of the course taken |
| Enrollment_Date | Date | Date the learner enrolled |
| Completion_Date | Date | Date completed (null = incomplete) |
| Completion_Status | Text | "Completed" or "Not Completed" |
| Score | Decimal | Assessment score out of 100 |
| Engagement_Score | Decimal | Engagement metric (1–5 scale) |
| Login_Count | Whole Number | Number of platform logins |
| Completion_Flag | Whole Number | Calculated: 1 = Completed, 0 = Incomplete |

---

## Task 2: Sales (Superstore)

| Column | Type | Description |
|--------|------|-------------|
| Row ID | Whole Number | Unique row identifier |
| Order ID | Text | Unique order identifier |
| Order Date | Date | Date the order was placed |
| Ship Date | Date | Date the order was shipped |
| Ship Mode | Text | First Class, Second Class, Standard, Same Day |
| Customer ID | Text | Unique customer identifier |
| Customer Name | Text | Full customer name |
| Segment | Text | Consumer / Corporate / Home Office |
| Country | Text | Country of the order |
| City | Text | City of the order |
| State | Text | State of the order |
| Region | Text | East / West / Central / South |
| Product ID | Text | Unique product identifier |
| Category | Text | Furniture / Office Supplies / Technology |
| Sub-Category | Text | Chairs, Binders, Phones, etc. |
| Product Name | Text | Full product name |
| Sales | Decimal | Revenue amount (USD) |
| Quantity | Whole Number | Units sold |
| Discount | Decimal | Discount applied (0.0–1.0) |
| Profit | Decimal | Profit amount (USD) |
| Profit Margin % | Decimal | Calculated: Profit / Sales * 100 |

---

## Task 3: Delivery_Logistics_Clean

| Column | Type | Notes |
|--------|------|-------|
| delivery_id | Whole Number | Unique delivery record ID |
| delivery_partner | Text | 9 partners (Delhivery, FedEx, DHL, Ekart, BlueDart, XpressBees, Shadowfax, Ecom Express, Amazon Logistics) |
| package_type | Text | Electronics, Groceries, Fragile Items, Pharmacy, Documents, Clothing, Furniture, Cosmetics, Automobile Parts |
| vehicle_type | Text | EV Bike, Van, Scooter, Bike, Truck, EV Van |
| delivery_mode | Text | Same Day, Express, Two Day, Standard |
| region | Text | West, Central, South, North, East |
| weather_condition | Text | Clear, Rainy, Foggy, Stormy, Cold, Hot |
| distance_km | Decimal | Distance in kilometres |
| package_weight_kg | Decimal | Weight in kilograms |
| delivery_time_hours | Whole Number | CLEANED from corrupted timestamp (0–19 hrs) |
| expected_time_hours | Whole Number | CLEANED from corrupted timestamp (2–24 hrs) |
| delayed | Text | "yes" / "no" (source binary flag) |
| delivery_status | Text | "delivered" / "delayed" / "failed" |
| delivery_rating | Whole Number | Customer rating (1–5) |
| delivery_cost | Decimal | Cost in INR |
| delay_hours | Whole Number | ENGINEERED: delivery_time - expected_time |
| status_label | Text | ENGINEERED: "On Time" or "Delayed" |
| delivery_date | Date | ENGINEERED: Synthetic 2023–2024 date for trends |

---

## Task 4: HRDataset_v14 (Cleaned)

| Column | Type | Notes |
|--------|------|-------|
| EmpID | Whole Number | Unique employee ID |
| Employee_Name | Text | Full name (Last, First) |
| Sex | Text | M / F |
| Department | Text | Production, IT/IS, Sales, Software Engineering, Admin Offices, Executive Office |
| Position | Text | Job title |
| ManagerName | Text | Direct manager name |
| DateofHire | Date | Hire date |
| DateofTermination | Date | Exit date (null for active — correct, not missing) |
| EmploymentStatus | Text | Active / Voluntarily Terminated / Terminated for Cause |
| Status | Text | ENGINEERED: "Active" or "Terminated" |
| Attrition_Flag | Whole Number | ENGINEERED: 1 = Terminated, 0 = Active |
| TermReason | Text | Reason for leaving |
| Salary | Whole Number | Annual salary in USD |
| PerformanceScore | Text | Exceeds / Fully Meets / Needs Improvement / PIP |
| PerformanceScore_Num | Whole Number | ENGINEERED: 4/3/2/1 mapping |
| EngagementSurvey | Decimal | 1.0–5.0 scale |
| EmpSatisfaction | Whole Number | 1–5 scale |
| DaysLateLast30 | Whole Number | Attendance signal |
| Absences | Whole Number | Total absences |
| SpecialProjectsCount | Whole Number | Special projects count |
| RecruitmentSource | Text | LinkedIn, Indeed, Google Search, Employee Referral, Diversity Job Fair, etc. |
| Age | Whole Number | ENGINEERED: Age vs 2024-01-01 |
| Tenure_Years | Decimal | ENGINEERED: Years of service |
| Hire_Year | Whole Number | ENGINEERED: Year of hire |
| Hire_Month | Text | ENGINEERED: YYYY-MM format |
| State | Text | US state |
| MaritalDesc | Text | Single, Married, Divorced, Separated, Widowed |
| RaceDesc | Text | Race/ethnicity |
| Termd | Whole Number | Original binary flag from source |
