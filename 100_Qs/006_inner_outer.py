Write a SQL query using an
INNER JOIN that lists all employees along with their respective department names.
select
    e.*,
    d.DepartmentName
from
    e_lz e
    inner join d_lz d on e.DepartmentID = d.DepartmentID Formulate a SQL query that provides a list of departments along with the names of their managers using an
    INNER JOIN between the two tables.
select
    d.departmentName,
    e.EmployeeName
from
    e_lz e
    inner join d_lz d ON e.EmployeeID = d.ManagerID




