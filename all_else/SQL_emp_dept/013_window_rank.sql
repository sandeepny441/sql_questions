-- ROW_NUMBER()
1. Assign a unique row number to each employee ordered by salary descending.
2. Use ROW_NUMBER() over PARTITION BY dept_id ordered by hire_date to number employees within each department by hire date.
3. Find the 2nd highest paid employee using ROW_NUMBER() = 2 in a subquery or CTE.

-- RANK()
1. Rank employees by salary descending, allowing ties to share the same rank.
2. Use RANK() over PARTITION BY dept_id ordered by salary DESC to rank within departments.
3. Identify the top-ranked employee per manager using RANK() = 1 partitioned by manager_id.

-- DENSE_RANK()
1. Assign dense ranks to employees by hire_date ascending, without gaps in ranking.
2. Use DENSE_RANK() over PARTITION BY YEAR(hire_date) ordered by salary DESC to rank salaries densely per hire year.
3. Find departments' dense rank by average salary using DENSE_RANK() on a grouped query.

-- CUME_DIST()
1. Calculate the cumulative distribution of salaries to see the proportion of employees with lower or equal salary.
2. Use CUME_DIST() over PARTITION BY dept_id ordered by hire_date to find hire order distribution within departments.
3. Compute CUME_DIST() on salaries to identify employees in the top 20% by salary.

-- PERCENT_RANK()
1. Find the percent rank of each employee's salary within the entire company.
2. Use PERCENT_RANK() over PARTITION BY manager_id ordered by salary to rank reports relative to their peers.
3. Calculate PERCENT_RANK() on hire_dates to see how early or late each hire was relatively.

-- NTILE(n)
1. Divide employees into 4 quartiles based on salary using NTILE(4) ordered by salary.
2. Use NTILE(3) over PARTITION BY dept_id ordered by hire_date to group employees into thirds per department by hire order.
3. Apply NTILE(5) on salaries to categorize employees into 5 equal buckets for analysis.
