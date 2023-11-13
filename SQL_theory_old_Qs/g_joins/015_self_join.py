SELECT e.employee_name AS employee, 
       m.employee_name AS manager
FROM employees e
JOIN employees m 
    ON e.manager_id = m.employee_id;
