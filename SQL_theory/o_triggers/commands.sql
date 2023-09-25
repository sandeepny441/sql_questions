-- In SQL, a trigger is a type of stored procedure that automatically executes or fires when a specified event occurs in the database. These events could be changes like insertion, deletion, or updation of rows in a table. Triggers are commonly used to maintain the integrity of the information on the database and are often used to perform tasks that are triggered by database operations.

-- There are three main types of triggers:

-- 3 types of Triggers
INSERT 
UPDATE 
DELETE 

CREATE TRIGGER after_employee_insert
AFTER INSERT
ON employees FOR EACH ROW
BEGIN
    INSERT INTO audit_logs (action, emp_id, change_date) 
    VALUES ('Insert', NEW.id, now());
END;



Here is a basic example of an "AFTER INSERT" trigger:

sql

CREATE TRIGGER after_employee_insert
AFTER INSERT
ON employees FOR EACH ROW
BEGIN
    INSERT INTO audit_logs (action, emp_id, change_date) 
    VALUES ('Insert', NEW.id, now());
END;
-- In this example, the trigger is named "after_employee_insert" and it's set to run after any INSERT operation on the "employees" table. When an insertion event happens, the trigger adds a new row to an "audit_logs" table, recording the action, the id of the new employee, and the current date and time.zz
