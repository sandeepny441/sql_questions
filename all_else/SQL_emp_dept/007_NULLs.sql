-- IS NULL
1. Find all employees where the salary is NULL.
2. List departments with location IS NULL.
3. Retrieve employees whose manager_id IS NULL.

-- IS NOT NULL
1. Find all employees where dept_id IS NOT NULL.
2. List employees with salary IS NOT NULL and hired after 2020.
3. Retrieve departments where location IS NOT NULL.

-- COALESCE
1. Use COALESCE to replace NULL salaries with 0 and list all employees.
2. Display department locations, using COALESCE to show 'Unknown' for NULL locations.
3. For each employee, show manager_id or 'No Manager' using COALESCE.

-- NULLIF
1. Use NULLIF to set salary to NULL if it equals 80000, and list employees.
2. For dept_name, use NULLIF to return NULL if location is 'New York'.
3. Apply NULLIF on emp_id if it matches manager_id (though unlikely), to illustrate.

-- NULLS and Joins --- Where vs ON
1. Perform a RIGHT JOIN on dept and emp on dept_id, with condition hire_date > '2020-01-01' in ON clause, to include all depts with NULLs where condition fails.
2. Compare: LEFT JOIN emp to dept on dept_id, with location = 'New York' in WHERE vs in ON, to see how NULL locations are handled.
3. RIGHT JOIN emp to dept on dept_id, with salary > 70000 in ON vs WHERE, observing how NULL salaries affect row inclusion.