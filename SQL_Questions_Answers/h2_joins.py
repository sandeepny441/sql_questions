# Write a query to list all employees along with their managers' names. For employees without a manager, the manager's name should appear as NULL.
# SELECT
#     e1.EmployeeID,
#     e1.EmployeeName as emp_name,
#     e2.EmployeeName AS Manager
# FROM
#     Y_Employees e1   LEFT JOIN Y_Employees e2 
#     ON e1.managerID = e2.EmployeeID;
===============================================================
# # Can you find pairs of employees who share the same manager? Include the names of the employees and their manager's name in your result.
    
# SELECT
#     e1.EmployeeName AS Employee1,
#     e1.EmployeeID as emp_ID, 
#     e2.EmployeeName AS Employee2, 
#      e2.EmployeeID as emp_ID_2,
#     m.EmployeeName AS Manager,
#     m.EmployeeID as m_ID
# FROM
#     y_employees e1
#     INNER JOIN y_employees e2 
#     ON e1.ManagerID = e2.ManagerID
#     AND e1.EmployeeID  < e2.EmployeeID
#     LEFT JOIN y_employees m ON e1.ManagerID = m.EmployeeID;
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

