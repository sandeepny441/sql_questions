SELECT * 
FROM Employees 
ORDER BY Salary DESC;


SELECT * 
FROM Employees 
WHERE Department = 'Sales' AND JobTitle = 'Manager'
ORDER BY Salary ASC, Age DESC;

SELECT * 
FROM Employees 
WHERE Salary / 12 > 5000;

SELECT FirstName, LastName, LENGTH(FirstName) AS NameLength 
FROM Employees 
ORDER BY NameLength DESC;


