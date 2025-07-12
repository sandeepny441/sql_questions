-- SUBQUERY  Basics
1. Find employees who earn more than the average salary using a subquery in WHERE.
2. List departments along with the number of employees using a subquery in SELECT (correlated).
3. Retrieve the employee with the highest salary using a subquery in FROM (derived table).
==============================================
-- Scalar Subquery
1. Find employees who earn more than the average salary using a scalar subquery in WHERE.
2. List departments where the number of employees is greater than the overall average number of employees per department using a scalar subquery.
3. Retrieve the employee with the maximum salary using a scalar subquery to compare.

-- Row Subquery
1. Find the employee whose (emp_name, dept_id) matches the (manager's name, dept_id) of a specific employee, using a row subquery.
2. Retrieve details where (salary, hire_date) = (SELECT MAX(salary), MIN(hire_date) FROM emp) using a row subquery.
3. Compare (dept_id, location) from dept to a row subquery selecting specific values.

-- Column Subquery
1. List employees whose dept_id is in the list of departments with NULL locations using a column subquery with IN.
2. Find managers whose emp_id appears in the list of manager_ids from emp using a column subquery.
3. Retrieve employees hired in years that match the years of hires in Engineering using a column subquery.

-- Table Subquery (Derived Table)
1. Join emp to a derived table that computes average salary per dept_id and list employees above their dept average.
2. Use a table subquery to select max salary per department and join to dept for names.
3. Create a derived table of employees with manager_id NULL and join to emp to find their reports.

-- Non-Correlated Subquery
1. Find all employees with salary > (SELECT AVG(salary) FROM emp) using a non-correlated subquery.
2. List departments with dept_id IN (SELECT DISTINCT dept_id FROM emp) using non-correlated.
3. Retrieve the total count of employees minus (SELECT COUNT(*) FROM emp WHERE dept_id IS NULL).

-- Correlated Subquery
1. Find employees who earn more than the average salary in their own department using a correlated subquery.
2. List departments where the number of employees = (SELECT COUNT(*) FROM emp e WHERE e.dept_id = d.dept_id).
3. Retrieve managers who have at least one report hired after them using correlated subquery with EXISTS.

-- Nested Subquery
1. Find employees in departments located in cities where managers earn more than (nested: avg salary from another subquery).
2. List dept_ids IN (SELECT dept_id FROM emp WHERE salary > (SELECT AVG(salary) FROM emp)).
3. Retrieve names where manager_id = (SELECT emp_id FROM emp WHERE dept_id = (SELECT dept_id FROM dept WHERE dept_name = 'Engineering')).

-- Subquery in SELECT Clause
1. SELECT emp_name, (SELECT dept_name FROM dept d WHERE d.dept_id = e.dept_id) AS department FROM emp e.
2. Add a column for average salary: SELECT emp_name, salary, (SELECT AVG(salary) FROM emp) AS avg_salary FROM emp.
3. SELECT emp_name, (SELECT COUNT(*) FROM emp WHERE manager_id = e.emp_id) AS reports FROM emp e.

-- Subquery in FROM Clause
1. SELECT e.emp_name, avg_sal.avg_salary FROM emp e JOIN (SELECT dept_id, AVG(salary) AS avg_salary FROM emp GROUP BY dept_id) avg_sal ON e.dept_id = avg_sal.dept_id.
2. Use FROM (SELECT * FROM dept WHERE location IS NOT NULL) AS located_depts JOIN emp ON dept_id.
3. SELECT max_hire FROM (SELECT dept_id, MAX(hire_date) AS max_hire FROM emp GROUP BY dept_id) AS hires.

-- Subquery in WHERE Clause
1. SELECT * FROM emp WHERE dept_id IN (SELECT dept_id FROM dept WHERE location = 'New York').
2. SELECT emp_name FROM emp WHERE salary > (SELECT MIN(salary) FROM emp WHERE dept_id = 1).
3. SELECT * FROM dept WHERE dept_id NOT IN (SELECT DISTINCT dept_id FROM emp).

-- Subquery in HAVING Clause
1. SELECT dept_id, AVG(salary) FROM emp GROUP BY dept_id HAVING AVG(salary) > (SELECT AVG(salary) FROM emp).
2. SELECT manager_id, COUNT(*) FROM emp GROUP BY manager_id HAVING COUNT(*) > (SELECT AVG(COUNT(*)) FROM emp GROUP BY manager_id).
3. SELECT dept_id, MAX(salary) FROM emp GROUP BY dept_id HAVING MAX(salary) < (SELECT MAX(salary) FROM emp).

-- Single-Row Subquery
1. Find the employee with salary = (SELECT MAX(salary) FROM emp).
2. Retrieve the department where dept_id = (SELECT dept_id FROM emp WHERE emp_name = 'Alice Smith').
3. List employees hired on the date = (SELECT MIN(hire_date) FROM emp).

-- Multiple-Row Subquery
1. SELECT emp_name FROM emp WHERE dept_id IN (SELECT dept_id FROM dept WHERE location IS NULL).
2. Find salaries greater than ANY (SELECT salary FROM emp WHERE dept_id = 1).
3. Retrieve managers where emp_id NOT IN (SELECT manager_id FROM emp WHERE salary < 80000).

-- Multiple-Column Subquery
1. SELECT * FROM emp WHERE (dept_id, salary) IN (SELECT dept_id, MAX(salary) FROM emp GROUP BY dept_id).
2. Find pairs where (manager_id, dept_id) = (SELECT emp_id, dept_id FROM emp WHERE emp_name = 'Emma Davis').
3. Retrieve where (hire_date, salary) > (SELECT MIN(hire_date), AVG(salary) FROM emp).

-- Existential Subquery
1. SELECT * FROM dept d WHERE EXISTS (SELECT 1 FROM emp WHERE dept_id = d.dept_id).
2. Find employees where NOT EXISTS (SELECT 1 FROM emp WHERE manager_id = e.emp_id) for those without reports.
3. List departments where EXISTS (SELECT 1 FROM emp WHERE dept_id = d.dept_id AND salary > 90000).

