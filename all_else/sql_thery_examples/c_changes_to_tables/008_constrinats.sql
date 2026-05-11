NOTNULL
DEFAULT
UNIQUE 

PRIMARY KEY
FORIEGN KEY 
REFERENCES

CHECK




CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  salary DECIMAL DEFAULT 10000,
  EMP_ID INT CHECK (EMP_ID > 0),
  department VARCHAR(20),
  hire_date DATE CHECK (hire_date <= CURRENT_DATE),
  INDEX name_idx (name),
  FOREIGN KEY (department) REFERENCES departments(department_name) 
);
