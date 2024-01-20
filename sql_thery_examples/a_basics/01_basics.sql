-- basic select
SELECT * FROM Employees

-- two columns 
SELECT FirstName, LastName FROM Employees;

-- sekect and rename 
SELECT FirstName AS Name FROM Employees;

-- Distinct 
SELECT DISTINCT Country FROM Customers;

-- where 
SELECT * FROM Employees WHERE Salary > 50000;
SELECT * FROM Employees WHERE Salary > 50000 AND Age < 30;

--sort
SELECT * FROM Employees ORDER BY Salary DESC;

--limit 
SELECT * FROM Employees LIMIT 5;

--count 
SELECT COUNT(DISTINCT Country) FROM Customers;


