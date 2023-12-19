# Who reports to whom?
# Can you identify which employees directly report to each manager? For example, who are the direct reports of the employee with EmployeeID = 3?

# select e1.Name as manager_name, e2.ManagerID as m_id, 
# e2.Name as Report_name
# from A e1 right join A e2 
# ON e1.EmployeeID = e2.ManagerID 
# where e1.EmployeeID <> e2.EmployeeID
# and e2.ManagerID = 3

# SELECT 
#     e1.Name AS Manager_Name, 
#     e2.Name AS Report_Name
# FROM 
#     A e1 
# JOIN 
#     A e2 
# ON 
#     e1.EmployeeID = e2.ManagerID
# WHERE 
#     e2.ManagerID = 3;


# List of employees and their managers
# Could you create a list showing each employee alongside their respective manager's name? This requires linking employees with their managers based on the ManagerID

# Employees who are at a higher level than others in terms of position or salary
# Which employees hold a higher position or earn a higher salary compared to others? For instance, who are the employees with the highest salaries in each department?

# select 
# 	e1.Name as emp_name_1, 
# 	e2.Name as emp_name_2, 
# 	e1.salary as salary_1, 
# 	e2.salary as salary_2,
# 	e1.Department as d_name
# from A e1 inner join A e2 
# 	on e1.Department = e2.Department 
# 	where e1.Salary > e2.Salary

# SELECT 
#     e.Name AS Employee_Name,
#     e.Salary,
#     e.Department
# FROM 
#     A e
# INNER JOIN 
#     (SELECT 
#          Department, 
#          MAX(Salary) AS MaxSalary
#      FROM 
#          A
#      GROUP BY 
#          Department) AS DeptMax
# ON 
#     e.Department = DeptMax.Department AND e.Salary = DeptMax.MaxSalary;

# select Department, max(Salary)
# from A 
# group by Department 


