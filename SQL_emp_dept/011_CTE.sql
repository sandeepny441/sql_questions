-- Standard CTE
1. Use a standard CTE to calculate the average salary across all employees and select employees earning above that average.
2. Define a standard CTE for departments with locations and join it to employees to list employee details with locations.
3. Create a standard CTE to count employees per department and then select departments with more than 1 employee.

-- Sequential CTE
1. Use sequential CTEs: first filter Engineering employees, then in the second CTE find those with salary > 80000, and select from the second.
2. Define sequential CTEs: one for managers (manager_id IS NULL), next for their direct reports, and list the reports.
3. Sequential CTEs: first compute avg salary per dept, second filter depts where avg > overall avg, and join back to depts.

-- Recursive CTE
1. Build a recursive CTE to display the employee hierarchy starting from top managers (manager_id IS NULL), showing levels.
2. Use a recursive CTE to find all reports under a specific manager, like under emp_id 105, including indirect reports.
3. Create a recursive CTE to traverse the manager chain upwards from a leaf employee to the top manager.

-- Nested CTE
1. Use a nested CTE: outer CTE defines employees in HR, inner CTE (inside outer) filters those with salary > 70000, and select from outer.
2. Nested CTE: outer for depts with employees, inner for counting per dept, and use inner in outer's select.
3. Define nested CTE: outer computes max salary, inner (nested) gets avg salary, and compare in outer.
