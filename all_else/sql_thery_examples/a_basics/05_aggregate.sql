SELECT COUNT(*) AS Total_Employees,
       SUM(Salary) AS Total_Salary,
       AVG(Salary) AS Average_Salary,
       MIN(Salary) AS Minimum_Salary,
       MAX(Salary) AS Maximum_Salary
FROM Employees;
