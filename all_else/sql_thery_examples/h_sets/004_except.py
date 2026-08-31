SELECT employee_name FROM employees
EXCEPT
SELECT manager_name FROM managers;

-- 1,2,3,4 -- table 1
-- 3,4,5 -- table 2 

-- fetches only 1, and 2