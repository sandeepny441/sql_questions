-- Fetch Employees and Their Managers
SELECT 
    E1.EmployeeName AS Employee,
    E2.EmployeeName AS Manager
FROM 
    Employee E1
JOIN 
    Employee E2 ON E1.ManagerID = E2.EmployeeID;
-----------------------------------------------------
-- Select Employees with salary higher than Manager's
SELECT 
    E1.EmployeeName AS Employee,
    E1.Salary AS EmployeeSalary,
    E2.EmployeeName AS Manager,
    E2.Salary AS ManagerSalary
FROM 
    Employee E1
JOIN 
    Employee E2 ON E1.ManagerID = E2.EmployeeID
WHERE 
    E1.Salary > E2.Salary;
-----------------------------------------------------
--Employee without Manager (CEO)
SELECT 
    E1.EmployeeName
FROM 
    Employee E1
WHERE 
    E1.ManagerID IS NULL;
-----------------------------------------------------
--emp sharing the same manager
SELECT 
    E1.EmployeeName AS Employee1,
    E2.EmployeeName AS Employee2,
    E1.ManagerID
FROM 
    Employee E1
JOIN 
    Employee E2 ON E1.ManagerID = E2.ManagerID
WHERE 
    E1.EmployeeID != E2.EmployeeID;
-----------------------------------------------------
--emp sharing the same salary
SELECT 
    E1.EmployeeName AS Employee1,
    E2.EmployeeName AS Employee2,
    E1.Salary
FROM 
    Employee E1
JOIN 
    Employee E2 ON E1.Salary = E2.Salary
WHERE 
    E1.EmployeeID != E2.EmployeeID;
------------------------------------------------------
--who are my reportees
SELECT 
    E1.EmployeeName AS Manager,
    E2.EmployeeName AS Subordinate
FROM 
    Employee E1
JOIN 
    Employee E2 ON E1.EmployeeID = E2.ManagerID;
------------------------------------------------------------- 
SELECT 
    E1.EmployeeName AS Employee,
    E2.EmployeeName AS x
FROM 
    Employee E1
JOIN 
    Employee E2 ON E1.ManagerID = E2.EmployeeID
WHERE 
    E2.ManagerID IS NULL;
------------------------------------------------------------
SELECT 
    E1.EmployeeName AS Manager
FROM 
    Employee E1
WHERE 
    E1.EmployeeID NOT IN (SELECT ManagerID FROM Employee WHERE ManagerID IS NOT NULL);
--------------------------------------------------------------
SELECT 
    E1.EmployeeName,
    E1.Salary
FROM 
    Employee E1
WHERE 
    E1.Salary > (SELECT AVG(Salary) FROM Employee);
--------------------------------------------------------------
SELECT 
    E1.EmployeeName AS Employee1,
    E2.EmployeeName AS Employee2,
    E1.Role
FROM 
    Employee E1
JOIN 
    Employee E2 ON E1.Role = E2.Role
WHERE 
    E1.EmployeeID != E2.EmployeeID;
--------------------------------------------------------------
select 
E1.empname as name, 
E1.salary,
E1.departmentID
from Employee E1
where E1.slary =  (select min(salary) from Employee E2 where E1.departmentID = E2.departmentID)
--------------------------------------------------------------