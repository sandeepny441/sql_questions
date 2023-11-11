UPDATE employees
SET SALARY = 200

UPDATE table_name
SET column1 = value1, 
    column2 = value2
WHERE condition;

UPDATE Employees
SET Salary = 60000, LastName = 'Smith'
WHERE FirstName = 'Jane';


UPDATE employees e1
SET salary = (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e1.job_title = e2.job_title
);
