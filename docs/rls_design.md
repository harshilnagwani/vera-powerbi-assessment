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

## Testing Checklist

Each role was tested via **Modeling → View as Roles** in Power BI Desktop.

For each role, verify:
- [ ] KPI cards show only scoped data
- [ ] Bar charts filter to the role scope
- [ ] Slicers only show values within scope
- [ ] Drill-through pages inherit the RLS filter
- [ ] Total counts match manual filter on full dataset

## Extending to Dynamic RLS

To upgrade from static to dynamic RLS, add a `UserMapping` table:

```
UserMapping
-----------
UserEmail   (Text) | Department (Text) | Region (Text)
```

Then replace static filters with:

```dax
-- Dynamic HR role
[Department] = LOOKUPVALUE(
    UserMapping[Department],
    UserMapping[UserEmail],
    USERPRINCIPALNAME()
)
```

This requires Azure AD user provisioning in Power BI Service.
