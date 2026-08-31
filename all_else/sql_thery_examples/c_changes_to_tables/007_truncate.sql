-- No ROlling back, removes everything, Fastest
DROP TABLE Employees;

-- No Rolling back, retains structure, Fast
TRUNCATE TABLE Employees;


-- ROlls back, deletes slowly
DELETE FROM Employees WHERE Department = 'HR';


-- DROP >>>>>> TRUNCATE >>>>>>> DELETE 

