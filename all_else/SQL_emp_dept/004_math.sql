-- ROUND
1. Round the average salary of all employees to the nearest whole number.
2. Round each employee's salary to 2 decimal places, assuming salaries could have decimals.
3. Calculate the rounded difference in days between hire_date and current date for each employee.

-- ABS
1. Find the absolute difference in salary between Alice Smith and Bob Johnson.
2. Calculate the absolute value of (salary - 80000) for each employee.
3. Use ABS to find the absolute difference between min and max salaries.

-- MOD
1. Find employees whose emp_id modulo 2 equals 0 (even emp_id).
2. Calculate salary MOD 10000 for each employee to find remainder after dividing by 10000.
3. Use MOD on dept_id to group departments where dept_id % 3 = 1.

-- POWER
1. Calculate POWER(salary, 2) to find the square of each employee's salary.
2. Use POWER(2, dept_id) to compute 2 raised to the power of dept_id for each department.
3. Find POWER(10, 3) as a constant and add to total salary sum.

-- SQRT
1. Calculate the square root of each employee's salary.
2. Find the SQRT of the total number of employees.
3. Compute SQRT(AVG(salary)) for employees in Engineering.

-- FLOOR
1. Use FLOOR on salary / 1000 to find salary in thousands, floored.
2. FLOOR the average salary across all employees.
3. Calculate FLOOR(datediff(current_date, hire_date) / 365) to find floored years of service.

-- CEILING
1. Use CEILING on salary / 1000 to find salary in thousands, ceiled.
2. CEILING the average salary in the HR department.
3. Calculate CEILING(datediff(current_date, hire_date) / 30) for months of service, ceiled.

-- LOG
1. Calculate the natural logarithm of salary for each employee with salary > 0.
2. Find LOG(AVG(salary)) for all employees.
3. Use LOG(salary / 10000) to normalize salaries logarithmically.

-- EXP
1. Calculate EXP(LOG(salary)) to verify it returns salary for each employee.
2. Find EXP(1) * SUM(salary) as a scaled total salary.
3. Use EXP(dept_id) to compute e raised to dept_id for departments.