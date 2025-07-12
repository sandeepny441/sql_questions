-- Department Table
CREATE TABLE dept (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

-- Employee Table
CREATE TABLE emp (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    dept_id INT,
    salary INT,
    hire_date DATE NOT NULL,
    manager_id INT,
    FOREIGN KEY (dept_id) REFERENCES dept(dept_id),
    FOREIGN KEY (manager_id) REFERENCES emp(emp_id)
);


-- Insert into Department
INSERT INTO dept (dept_id, dept_name, location) VALUES
(1, 'Engineering', 'New York'),
(2, 'HR', NULL),
(3, 'Marketing', 'Chicago'),
(4, 'Finance', NULL),
(5, 'Research', 'Boston');

-- Insert into Employee (reordered)
INSERT INTO emp (emp_id, emp_name, dept_id, salary, hire_date, manager_id) VALUES
(105, 'Emma Davis', 1, 95000, '2018-11-30', NULL),    -- Manager for 101, 102
(106, 'Frank Lee', 4, 80000, '2020-09-12', NULL),      -- Manager for 104
(103, 'Carol White', 2, NULL, '2021-01-10', NULL),     -- Manager for 107
(101, 'Alice Smith', 1, 90000, '2020-03-15', 105),     -- References 105
(102, 'Bob Johnson', 1, 85000, '2019-07-22', 105),     -- References 105
(104, 'Dave Brown', 3, 65000, '2022-06-05', 106),      -- References 106
(107, 'Grace Kim', 2, 72000, '2021-03-20', 103),       -- References 103
(108, 'Henry Clark', NULL, 60000, '2023-02-18', NULL),
(109, 'Ian Turner', NULL, NULL, '2023-05-10', NULL);

