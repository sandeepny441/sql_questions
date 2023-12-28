====================================================
----SELF JOINS--------------------------------------
# Write a query to list all employees along with their managers' names. For employees without a manager, the manager's name should appear as NULL.
# SELECT
#     e1.EmployeeID,
#     e1.EmployeeName as emp_name,
#     e2.EmployeeName AS Manager
# FROM
#     Y_Employees e1   LEFT JOIN Y_Employees e2 
#     ON e1.managerID = e2.EmployeeID;
===============================================================
# Can you find pairs of employees who share the same manager? Include the names of the employees and their manager's name in your result.
    
SELECT
    e1.EmployeeName AS Employee1,
    e1.EmployeeID as emp_ID, 
    e2.EmployeeName AS Employee2, 
     e2.EmployeeID as emp_ID_2,
    m.EmployeeName AS Manager,
    m.EmployeeID as m_ID
FROM
    y_employees e1
    INNER JOIN y_employees e2 
    ON e1.ManagerID = e2.ManagerID
    AND e1.EmployeeID  < e2.EmployeeID
    LEFT JOIN y_employees m ON e1.ManagerID = m.EmployeeID;
===============================================================
# Write a query to list all managers and the number of direct reports (employees they manage) they have.


# select e1.employeeName as Manager, 
# count(e2.employeeName) as reports_count
# from y_Employees e1
# inner join y_employees e2 
# on e1.employeeID = e2.managerID 
# group by e1.employeeName
===============================================================
# Can you write a query to list employees who do not manage anyone? These are employees who are not listed as a ManagerID for anyone else.

# select manager from 
# (select e1.employeeName as manager, 
# e2.employeeName as Reportee
# from y_employees e1 
# left join 
# y_employees e2 
# on  e1.employeeID = e2.managerID) as temp_table
# where temp_table.Reportee is NULL 

# SELECT e.EmployeeName
# FROM y_employees e
# LEFT JOIN y_employees m ON e.EmployeeID = m.ManagerID
# WHERE m.ManagerID IS NULL;
===============================================================

# Write a query to display each employee's name along with the name of their manager's manager (grandmanager). If they don't have a grandmanager, it should show as NULL.


# select
#     e1.employeeName as employee,
#     e2.EmployeeName as manager,
#     e3.EmployeeName as grand_manager
# from
#     y_employees e1
#     left join y_employees e2 on e1.managerID = e2.EmployeeID
#     left join y_employees e3 on e2.managerID = e3.EmployeeID

=================================================================
List all the employees who share the same grandmanager. Exclude any employees who do not have a grandmanager.




================================================
# Natural Joins 

# SELECT *
# FROM Employees
# NATURAL JOIN Departments;
================================================
# CROSS JOINS 

# SELECT *
# FROM Colors
# CROSS JOIN Shapes;

# SELECT *
# FROM Colors, Shapes;

===============================================
# select * from T


# Question 1:
# Who are the managers of each employee? (Assuming that ManagerID corresponds to EmployeeID in the same table)


# Question 2:
# Which employees are peers within the same department? (Employees who share the same DepartmentID)

# Question 3:
# Find the names of all employees who do not manage anyone. (Employees whose EmployeeIDs do not appear in anyone else's ManagerID column)

# Question 4:
# Which managers have more than one employee reporting to them?

# Question 5:
# List all employees along with the names of their managers. (Assuming that managers are also listed as employees in the same table)

# Question 6:
# Are there any departments where the manager is also listed as an employee within the same department? If so, list those departments and manager names.

# Question 7:
# Find the employee names along with the names of their immediate subordinates.

# Question 8:
# Determine if there are any employees who share a manager but are from different departments.

# Question 9:
# Identify employees who are also managers of other departments (i.e., their EmployeeID appears in the ManagerID column for a different DepartmentID).

# Question 10:
# Identify any managers who report to other managers within the organization (assuming a hierarchy exists where some managers may also have managers).

# Question 11:
# List all employees who do not report to a manager within their own department (indicating a cross-department management structure).

# Question 12:
# For each department, find the employee with the longest name.

# Question 13:
# Can you identify any indirect reporting structures? For instance, an employee who reports to a manager who in turn reports to another manager.

# Question 14:
# Are there any employees who have the same name as their manager?

# Question 15:
# Which departments have a hierarchy depth greater than one, indicating that there are multiple levels of management within the department?

# Question 16:
# Which employees are managed by someone with a higher employee ID number?

# Question 17:
# Find the names of managers who are managing more than one department.

# Question 18:
# List all employees who have a manager in the same department and their manager has a manager in a different department.

# Question 19:
# Identify any managers who also act as an employee under another manager in a different department.

# Question 20:
# Determine if there are any employees who share the same manager and have the same name (excluding the manager themselves).