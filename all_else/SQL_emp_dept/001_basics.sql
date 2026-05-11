-- WHERE
1. List all employees who work in the Engineering department.
2. Find the employees hired after January 1, 2021.
3. Retrieve the details of the employee with emp_id 105.

-- AND OR NOT
1. Find employees in the Engineering department who earn more than 80000 or were hired before 2020.
2. List employees who are not in HR and have a manager_id that is not NULL.
3. Retrieve employees with salary greater than 70000 and located in New York or Chicago.

-- BETWEEN
1. Find employees with salaries between 70000 and 90000.
2. List employees hired between '2020-01-01' and '2022-12-31'.
3. Retrieve departments with dept_id between 2 and 4.

-- ORDER BY
1. List all employees ordered by their salary in descending order.
2. Retrieve departments ordered by dept_name alphabetically.
3. Find all employees ordered by hire_date ascending and then by emp_name.

-- DISTINCT
1. List distinct department names from the employee table (considering joins if needed).
2. Find distinct locations from the department table.
3. Retrieve distinct manager_ids from the employee table.

-- LIMIT
1. List the top 3 highest paid employees.
2. Retrieve the first 5 departments ordered by dept_id.
3. Find the 2 most recently hired employees.

-- OFFSET
1. List employees ordered by emp_id, skipping the first 3.
2. Retrieve departments starting from the 2nd one ordered by dept_name.
3. Find employees hired after 2020, ordered by hire_date, skipping the first 2.

-- COUNT
1. Count the number of employees in each department.
2. Count the total number of employees with a salary.
3. Count the number of departments with a location.

-- GROUP BY
1. Group employees by department and find the average salary per department.
2. Group departments by location and count the number in each.
3. Group employees by hire year and count hires per year.

-- HAVING
1. Find departments with more than 1 employee.
2. Group by department and find those with average salary > 80000.
3. Group by manager_id and find managers with at least 2 reports.