-- Inner Self Join
1. Use an INNER SELF JOIN to list pairs of employees who work in the same department (exclude self-pairs) and order by emp_name.
2. Find employees and their managers by INNER JOINING emp on manager_id = emp_id, displaying emp_name and manager's emp_name.
3. List pairs of employees hired in the same year using INNER SELF JOIN on YEAR(hire_date), excluding the same employee.
4. Use INNER SELF JOIN to find employees with the same salary, showing pairs where e1.emp_id < e2.emp_id to avoid duplicates.

-- Left Outer Self Join
1. Use LEFT OUTER SELF JOIN on emp to list all employees and their managers; if no manager, show NULL for manager details.
2. LEFT JOIN emp to itself on dept_id to find all employees and any colleagues with higher salary, but limit to show per employee the one with next higher salary using ROW_NUMBER if needed.
3. List all employees and pair them with employees hired later in the same department using LEFT SELF JOIN and hire_date < condition.
4. Use LEFT OUTER SELF JOIN to show all employees and count of their direct reports by joining on manager_id = emp_id and grouping.

-- Right Outer Self Join
1. Use RIGHT OUTER SELF JOIN on manager_id = emp_id to list all potential managers (all employees) and their reports; if no reports, show NULL.
2. RIGHT JOIN emp to itself on salary = salary to include all employees, even those with unique salaries, and list pairs.
3. Find all employees (right side) and match to earlier hires (left side) in the same dept using RIGHT SELF JOIN and hire_date > condition.
4. Use RIGHT OUTER SELF JOIN to emphasize including all "right" employees even without matches in hierarchical queries.

-- Full Outer Self Join
1. Use FULL OUTER SELF JOIN on emp_id = manager_id (though unusual) to show all employees as both potential employees and managers.
2. FULL JOIN emp to itself on dept_id to list all possible same-dept pairs, including unmatched (but since same table, all match).
3. Simulate finding symmetric differences in salaries using FULL OUTER SELF JOIN with non-equi conditions.
4. Use FULL OUTER SELF JOIN to combine employee and manager views, showing hierarchies with orphans on both sides.

-- Cross Self Join
1. Use CROSS SELF JOIN to generate all possible pairs of employees (Cartesian product) and filter for those in different departments.
2. CROSS JOIN emp to itself and calculate the salary difference for every pair where e1.emp_id < e2.emp_id.
3. Generate all possible manager-report assignments using CROSS SELF JOIN and filter where dept_id matches but current manager_id doesn't.
4. Use CROSS SELF JOIN to list all combinations of employees and compute hypothetical teams of two per department.

-- Hierarchical Self Join
1. Use self join to list employees and their direct managers, then join again for grand-managers (two-level hierarchy).
2. Find the reporting chain for a specific employee (e.g., emp_id 101) by joining multiple times up the manager_id.
3. Count the number of levels in the hierarchy by self-joining recursively or with multiple joins.
4. List all employees under a top manager (e.g., 105) by joining for direct and indirect reports using multiple self joins.

-- Non-Equi Self Join
1. Use non-equi self join (e1.salary > e2.salary) to find for each employee how many earn less than them.
2. List pairs where one employee was hired before another in the same department using e1.hire_date < e2.hire_date.
3. Find employees who earn more than their manager using self join on manager_id = emp_id and salary > manager's salary.
4. Use non-equi join to pair employees with all others in the same dept where emp_id != and salary between ranges.

-- Self Join with Aggregates/Subqueries/CTEs
1. Use self join with GROUP BY to find managers and the average salary of their direct reports.
2. In a CTE, self join to find pairs with same hire_date, then aggregate count of such pairs.
3. Use self join in a subquery to find the max salary per manager's reports, then compare to overall max.
4. Combine self join with window functions over partitions to rank reports per manager, effectively using self join for grouping.
5. Use a self join in HAVING clause after grouping to filter managers with more reports than average.
6. Wrap a self join in a CTE to compute tenure differences between employees and managers, then average per department.
