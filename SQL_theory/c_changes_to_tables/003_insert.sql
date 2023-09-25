INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);

INSERT INTO Employees (FirstName, LastName, Salary)
VALUES ('John', 'Doe', 50000);

INSERT INTO Employees (FirstName, LastName, Salary)
VALUES ('John', 'Doe', 50000),
       ('Jane', 'Smith', 60000),
       ('Bob', 'Johnson', 55000);


INSERT INTO new_employees (first_name, last_name, hire_date)
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date > '2023-01-01';


INSERT IGNORE INTO employees (employee_id, first_name, last_name, hire_date)
VALUES (1, 'John', 'Doe', '2023-01-01');



