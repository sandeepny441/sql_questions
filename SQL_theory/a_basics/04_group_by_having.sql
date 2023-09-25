SELECT Department, COUNT(*) 
FROM Employees 
GROUP BY Department
where saalary < 4000


SELECT Department, JobTitle, COUNT(*) 
FROM Employees 
GROUP BY Department, JobTitle;


SELECT Department, AVG(Salary) 
FROM Employees 
GROUP BY Department 
HAVING COUNT(*) > 5 AND AVG(Salary) > 50000;


-- In a SQL query, if you are using GROUP BY, then every column that is listed in the SELECT statement that is not an aggregate function (like COUNT, AVG, SUM, MIN, MAX) must be included in the GROUP BY clause.

SELECT Department, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5
ORDER BY Department ASC, EmployeeCount DESC;



