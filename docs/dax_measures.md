# DAX Measures Reference

All measures are stored in the `_Measures` table.
Display Folder is shown in brackets.

---

## [Task 1 - User Intelligence]

```dax
Total Enrollments =
COUNTROWS(Course_Completion_P_)

Completed Courses =
CALCULATE(
    COUNTROWS(Course_Completion_P_),
    Course_Completion_P_[Completion_Flag] = 1
)

Completion Rate % =
DIVIDE([Completed Courses], [Total Enrollments], 0) * 100

Avg Score =
AVERAGE(Course_Completion_P_[Score])

Avg Engagement Score =
AVERAGE(Course_Completion_P_[Engagement_Score])

Active Users =
DISTINCTCOUNT(Course_Completion_P_[EmployeeID])

Monthly Enrollments =
CALCULATE([Total Enrollments], DATESMTD(DateTable[Date]))
```

---

## [Task 2 - Sales Intelligence]

```dax
Total Revenue =
SUM(Sales[Sales])

Total Profit =
SUM(Sales[Profit])

Profit Margin % =
DIVIDE([Total Profit], [Total Revenue], 0) * 100

Total Orders =
COUNTROWS(Sales)

Total Quantity =
SUM(Sales[Quantity])

Avg Order Value =
DIVIDE([Total Revenue], [Total Orders], 0)

YTD Revenue =
CALCULATE([Total Revenue], DATESYTD(DateTable[Date]))

MoM Revenue Growth % =
VAR CurrentMonth = [Total Revenue]
VAR PrevMonth =
    CALCULATE([Total Revenue], DATEADD(DateTable[Date], -1, MONTH))
RETURN
    DIVIDE(CurrentMonth - PrevMonth, PrevMonth, 0) * 100
```

---

## [Task 3 - Operations Intelligence]

```dax
Total Deliveries =
COUNTROWS(Operations)

On Time Deliveries =
CALCULATE(COUNTROWS(Operations), Operations[status_label] = "On Time")

Delayed Deliveries =
CALCULATE(COUNTROWS(Operations), Operations[status_label] = "Delayed")

Failed Deliveries =
CALCULATE(COUNTROWS(Operations), Operations[delivery_status] = "failed")

On Time Rate % =
DIVIDE([On Time Deliveries], [Total Deliveries], 0) * 100

Delay Rate % =
DIVIDE([Delayed Deliveries], [Total Deliveries], 0) * 100

Avg Delivery Time (hrs) =
AVERAGE(Operations[delivery_time_hours])

Avg Expected Time (hrs) =
AVERAGE(Operations[expected_time_hours])

Avg Delay (hrs) =
AVERAGEX(
    FILTER(Operations, Operations[delay_hours] > 0),
    Operations[delay_hours]
)

Total Cost =
SUM(Operations[delivery_cost])

Avg Delivery Cost =
AVERAGE(Operations[delivery_cost])

Avg Delivery Rating =
AVERAGE(Operations[delivery_rating])

Monthly Delay Rate % =
CALCULATE([Delay Rate %], DATESMTD(DateTable[Date]))
```

---

## [Task 4 - HR Intelligence]

```dax
Total Employees =
COUNTROWS(HR)

Active Employees =
CALCULATE(COUNTROWS(HR), HR[Status] = "Active")

Terminated Employees =
CALCULATE(COUNTROWS(HR), HR[Status] = "Terminated")

Attrition Rate % =
DIVIDE([Terminated Employees], [Total Employees], 0) * 100

Retention Rate % =
100 - [Attrition Rate %]

Avg Performance Score =
AVERAGE(HR[PerformanceScore_Num])

Avg Engagement Score =
AVERAGE(HR[EngagementSurvey])

Avg Satisfaction =
AVERAGE(HR[EmpSatisfaction])

Avg Salary =
AVERAGE(HR[Salary])

Avg Tenure (Years) =
AVERAGE(HR[Tenure_Years])

Top Performers =
CALCULATE(COUNTROWS(HR), HR[PerformanceScore] = "Exceeds")

At Risk Employees =
CALCULATE(
    COUNTROWS(HR),
    HR[PerformanceScore] IN {"PIP", "Needs Improvement"}
)

Monthly New Hires =
CALCULATE([Total Employees], DATESMTD(DateTable[Date]))

Dept Attrition Rate % =
DIVIDE(
    CALCULATE(COUNTROWS(HR), HR[Status] = "Terminated"),
    CALCULATE(COUNTROWS(HR), ALLEXCEPT(HR, HR[Department])),
    0
) * 100

YoY Hiring Growth % =
VAR CY =
    CALCULATE([Total Employees],
        YEAR(DateTable[Date]) = MAXX(ALL(DateTable), YEAR(DateTable[Date])))
VAR PY = CALCULATE([Total Employees], DATEADD(DateTable[Date], -1, YEAR))
RETURN DIVIDE(CY - PY, PY, 0) * 100
```
