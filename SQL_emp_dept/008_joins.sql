-- INNER JOIN
1. List all employees along with their department names using INNER JOIN.
2. Find the total salary per department using INNER JOIN on emp and dept, grouped by dept_name.
3. Retrieve employee names and their manager names using INNER JOIN on emp (self-join for managers).

-- LEFT OUTER JOIN
1. List all departments and their employees, including departments with no employees, using LEFT OUTER JOIN.
2. Show all employees and their department locations, with NULL for employees without dept_id, using LEFT OUTER JOIN.
3. LEFT OUTER JOIN emp to dept on dept_id, and filter for locations IS NULL to find employees in departments without location.

-- RIGHT OUTER JOIN
1. List all departments and matching employees, including departments without employees, using RIGHT OUTER JOIN.
2. RIGHT OUTER JOIN dept to emp on dept_id, to include all departments even if no salary data.
3. Find departments without employees by RIGHT OUTER JOIN and where emp_id IS NULL.

-- FULL OUTER JOIN
1. Retrieve a full list of employees and departments, showing matches and non-matches on both sides using FULL OUTER JOIN.
2. Use FULL OUTER JOIN on emp and dept to count total unique dept_ids and emp_ids combined.
3. Identify orphaned records: employees without departments and departments without employees via FULL OUTER JOIN where one side is NULL.

-- SELF JOIN
1. List employees and their managers using SELF JOIN on emp (alias e and m on e.manager_id = m.emp_id).
2. Find pairs of employees in the same department using SELF JOIN where e1.dept_id = e2.dept_id and e1.emp_id < e2.emp_id.
3. Retrieve employees hired in the same year as their manager using SELF JOIN and YEAR(hire_date).

-- CROSS JOIN
1. Generate all possible pairs of employees and departments using CROSS JOIN.
2. Use CROSS JOIN between dept and a derived table of salary ranges to simulate categorizations.
3. CROSS JOIN emp with a list of months (from a numbers table or subquery) to generate monthly reports for each employee.