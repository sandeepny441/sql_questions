-- FIRST_VALUE()
1. Use FIRST_VALUE(salary) OVER (PARTITION BY dept_id ORDER BY hire_date) to show the salary of the first hired employee in each department for every employee.
2. Add a column with the first emp_name in alphabetical order per department using FIRST_VALUE(emp_name) OVER (PARTITION BY dept_id ORDER BY emp_name).
3. Compute FIRST_VALUE(hire_date) OVER (ORDER BY salary DESC) to show the hire_date of the highest paid employee for each row.

-- LAST_VALUE()
1. Use LAST_VALUE(salary) OVER (PARTITION BY dept_id ORDER BY hire_date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) to show the salary of the last hired in each department.
2. Add LAST_VALUE(emp_name) OVER (ORDER BY emp_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) to display the last employee's name in the entire table for each row.
3. Compute LAST_VALUE(manager_id) OVER (PARTITION BY dept_id ORDER BY salary DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) for the manager_id of the lowest paid in each dept.

-- LAG()
1. Use LAG(salary, 1) OVER (ORDER BY hire_date) to show the salary of the previously hired employee for each.
2. Compute LAG(emp_name, 1) OVER (PARTITION BY dept_id ORDER BY salary DESC) to display the name of the next highest paid in the department.
3. Find the difference in hire dates with DATEDIFF(hire_date, LAG(hire_date, 1) OVER (PARTITION BY manager_id ORDER BY hire_date)) for days between consecutive hires under the same manager.

-- LEAD()
1. Use LEAD(salary, 1) OVER (PARTITION BY dept_id ORDER BY salary ASC) to show the salary of the next higher paid employee in the department.
2. Compute LEAD(hire_date, 1) OVER (ORDER BY hire_date) to display the hire date of the next hired employee overall.
3. Find employees where salary > LEAD(salary, 1) OVER (ORDER BY emp_id) to identify where salary decreases in emp_id order.
