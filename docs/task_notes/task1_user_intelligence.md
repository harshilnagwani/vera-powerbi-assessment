# Task 1: User Intelligence Dashboard

## Objective
Analyze user behavior, engagement, and course completion patterns
from an internal learning platform.

### Dataset — Student Course Completion Prediction Dataset
**Source:**[ Internal learning platform export](https://www.kaggle.com/datasets/nisargpatel344/student-course-completion-prediction-dataset)
**Rows:** ~1,000+ | **Purpose:** Track learner activity, engagement, and course completion

| Column | Data Type | Description |
|--------|-----------|-------------|
| EmployeeID | Whole Number | Unique identifier for each learner |
| Employee_Name | Text | Full name of the learner |
| Department | Text | Department the learner belongs to |
| Course_Title | Text | Name of the course taken |
| Enrollment_Date | Date | Date the learner enrolled in the course |
| Completion_Date | Date | Date the learner completed the course (null if incomplete) |
| Completion_Status | Text | "Completed" or "Not Completed" |
| Score | Decimal | Assessment score out of 100 |
| Engagement_Score | Decimal | Engagement metric (1-5 scale) |
| Login_Count | Whole Number | Number of platform logins by the learner |
| Completion_Flag | Whole Number | Calculated: 1 = Completed, 0 = Incomplete |

### Measures — Task 1

| Measure | Description |
|---------|-------------|
| Total Enrollments | Total number of course enrollments across all learners |
| Completed Courses | Count of courses where Completion_Flag = 1 |
| Completion Rate % | Percentage of enrollments that resulted in completion |
| Avg Score | Average assessment score across all completed courses |
| Avg Engagement Score | Average learner engagement level on the platform |
| Active Users | Number of unique learners with at least one enrollment |
| Monthly Enrollments | Enrollments within the current month (DATESMTD) |


---

## Dashboard Requirements
- [x] Total Enrollments KPI card
- [x] Completion Rate % KPI card
- [x] Avg Score KPI card
- [x] Avg Engagement Score KPI card
- [x] Active Users KPI card
- [x] Completion Rate by Department (bar chart)
- [x] Enrollment trend over time (line chart)
- [x] Top courses by enrollment (horizontal bar)
- [x] Score distribution (histogram / column)
- [x] Custom tooltip page (Tooltip_User)
- [x] Slicers: Department, Course_Title, Enrollment_Date range

## Key Insights
1. Sub-50% completion in several departments — training engagement gap
2. Enrollment peaks suggest batch onboarding cycles
3. IT/IS and Software Engineering lead in avg score
4. Production has highest volume but below-average scores
5. Some learners never return after initial enrollment
