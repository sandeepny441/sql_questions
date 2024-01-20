CREATE MATERIALIZED VIEW HighPaidEmployees AS
SELECT EmployeeName, EmployeeSalary
FROM Employees
WHERE EmployeeSalary > 100000;

REFRESH MATERIALIZED VIEW HighPaidEmployees;
