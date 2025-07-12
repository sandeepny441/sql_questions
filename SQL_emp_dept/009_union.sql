-- UNION
1. Combine the list of employee names and department names using UNION to get unique names.
2. Use UNION to merge employees with salary > 80000 from Engineering and those from HR.
3. Retrieve unique dept_ids from dept table UNION with dept_ids from emp table.

-- UNION ALL
1. Combine all employee names and department names using UNION ALL, allowing duplicates.
2. Use UNION ALL to list salaries from emp table twice, once for each half of the year (hypothetical split).
3. Merge all locations from dept with employee names using UNION ALL for a mixed list.

-- INTERSECT
1. Find common dept_ids between dept table and emp table using INTERSECT.
2. Use INTERSECT to find employees who are also managers (emp_id INTERSECT manager_id from emp).
3. Retrieve common locations that appear in multiple departments using INTERSECT (derived queries).

-- EXCEPT
1. Find dept_ids in dept table but not in emp table using EXCEPT.
2. Use EXCEPT to list employees who are not managers (emp_id EXCEPT SELECT manager_id FROM emp).
3. Retrieve locations in dept that are not NULL using EXCEPT with a query selecting NULL.