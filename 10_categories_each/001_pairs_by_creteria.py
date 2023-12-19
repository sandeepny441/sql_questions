# Which employees share the same job title?
# Can you identify pairs of employees who have the same job title? For example, which employees are both 'Analysts' or 'Developers'?

# select e1.Name, e2.Name, e1.JobTitle from A e1 
# join A e2 
# ON e1.JobTitle = e2.JobTitle 
# where e1.EmployeeID < e2.EmployeeID 
# -- and e1.JobTitle in ('Analyst')
# ============================================================
# Who has the same manager?
# Which employees report to the same manager? Look for pairs of employees who have the same ManagerID. For instance, who are the employees managed by the person with ManagerID = 3?
# select e1.Name, e2.Name, e2.ManagerID from A e1 
# join A e2 
# ON e1.ManagerID = e2.ManagerID 
# where e1.EmployeeID < e2.EmployeeID
# and e2.ManagerID = 3
# -- select * from A
# ============================================================
# Employees who joined in the same year
# Can you find employees who joined the company in the same year? For example, which employees started working at the company in 2019?

# select e1.Name, e2.Name, e2.ManagerID from A e1 
# join A e2 
# ON extract(year from e1.BirthDate) = extract(year from e2.BirthDate)
# where e1.EmployeeID < e2.EmployeeID
# ============================================================
# Share same MANAGER
# select e1.Name as emp_name, 
# e2.Name as manager_name 
# from A e1 join A e2 
# ON e1.ManagerID = e2.EmployeeID
# where e1.EmployeeID < e2.EmployeeID
# ============================================================