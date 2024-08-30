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

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib


