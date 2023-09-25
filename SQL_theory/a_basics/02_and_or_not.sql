-- AND 
SELECT * 
FROM Employees 
WHERE Salary > 50000 
AND Age < 30;

--OR 
SELECT * 
FROM Employees 
WHERE Department = 'Sales' 
OR Department = 'Marketing';

--NOT 
SELECT * 
FROM Employees 
WHERE NOT Department = 'HR';

--AND / OR 
SELECT * 
FROM Employees 
WHERE (Department = 'Sales' 
OR Department = 'Marketing') 
AND Age < 30;

--AND OR NOT 
SELECT * 
FROM Employees 
WHERE (Department = 'Sales' 
OR Department = 'Marketing') 
AND NOT Age > 50

