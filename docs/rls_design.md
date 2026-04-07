# Row-Level Security Design

## Overview

Static RLS roles restrict dashboard access by department and region,
ensuring each manager sees only data relevant to their scope.

## Roles Implemented

### HR Table

```dax
-- Role: HR_Production
[Department] = "Production"

-- Role: HR_IT
[Department] = "IT/IS"

-- Role: HR_Sales
[Department] = "Sales"
```

### Operations Table

```dax
-- Role: Ops_West
[region] = "west"

-- Role: Ops_Central
[region] = "central"
```

g in Power BI Service.
