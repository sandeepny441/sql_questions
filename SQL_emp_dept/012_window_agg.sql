-- PARTITION BY
1. Calculate the average salary per department using a window function with PARTITION BY dept_id.
2. List each employee with the count of employees in their department using PARTITION BY dept_id over COUNT(*).
3. Find the maximum hire_date in each department for each employee using PARTITION BY dept_id.

-- ORDER BY
1. Compute the running total of salaries ordered by hire_date using a window function with ORDER BY hire_date.
2. Rank employees by salary descending within the entire table using ROW_NUMBER() with ORDER BY salary DESC.
3. Calculate the cumulative average salary ordered by emp_id using AVG() with ORDER BY emp_id.

-- RANGE or ROWS
1. Compute the sum of salaries for the current row and the previous one using ROWS BETWEEN 1 PRECEDING AND CURRENT ROW.
2. Find the average salary over an unbounded preceding range using RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW.
3. Use ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING to calculate moving count of employees ordered by hire_date.

-- SUM()
1. Use SUM(salary) OVER (PARTITION BY dept_id) to add a column for total department salary for each employee.
2. Compute running sum of salaries with SUM() OVER (ORDER BY hire_date).
3. Calculate sum of salaries within the same hire year using SUM() OVER (PARTITION BY YEAR(hire_date)).

-- AVG()
1. Add a column for average department salary using AVG(salary) OVER (PARTITION BY dept_id).
2. Compute moving average of last 3 salaries ordered by emp_id using AVG() OVER (ORDER BY emp_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW).
3. Find overall average salary for each row using AVG(salary) OVER ().

-- MAX()
1. Find the maximum salary in each department using MAX(salary) OVER (PARTITION BY dept_id).
2. Compute the running maximum salary ordered by hire_date with MAX(salary) OVER (ORDER BY hire_date).
3. Get the max hire_date per manager using MAX(hire_date) OVER (PARTITION BY manager_id).

-- MIN()
1. Find the minimum salary per department with MIN(salary) OVER (PARTITION BY dept_id).
2. Compute running minimum hire_date (earliest so far) with MIN(hire_date) OVER (ORDER BY hire_date).
3. Get the min salary for employees with the same location via join and MIN() OVER (PARTITION BY location).

-- COUNT()
1. Count the number of employees per department with COUNT(*) OVER (PARTITION BY dept_id).
2. Compute running count of employees ordered by emp_id with COUNT(*) OVER (ORDER BY emp_id).
3. Count non-NULL salaries per department using COUNT(salary) OVER (PARTITION BY dept_id).

-- STDDEV()
1. Calculate the standard deviation of salaries per department with STDDEV(salary) OVER (PARTITION BY dept_id).
2. Compute running STDDEV of salaries ordered by salary with STDDEV(salary) OVER (ORDER BY salary).
3. Find STDDEV of salaries for all employees in the window with STDDEV(salary) OVER ().

-- VARIANCE()
1. Compute the variance of salaries per department using VARIANCE(salary) OVER (PARTITION BY dept_id).
2. Calculate running variance ordered by hire_date with VARIANCE(salary) OVER (ORDER BY hire_date).
3. Get variance of salaries within the same manager group using VARIANCE(salary) OVER (PARTITION BY manager_id).
