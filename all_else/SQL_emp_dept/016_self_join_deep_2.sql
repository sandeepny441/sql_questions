1. List all employees and their direct managers, including the manager's salary and hire_date.
2. Find pairs of employees in the same department where one was 
hired before the other, using hire_date comparison and same dept_id.
3. List all employees and their reports, with NULL for employees without reports, and aggregate the count of reports.
4. Compute the salary difference between each employee and their manager using ABS on salaries.
5. Generate all possible employee-manager pairs within the same department, then filter to actual hierarchies.
6. Find the average salary of direct reports for each manager, grouped by manager's emp_id.
7. List all employees and match to those with lower emp_id in the same dept, calculating row numbers.
8. Show employee, manager, and grand-manager names in a two-level hierarchy.
9. Count how many employees earn less than each employee within their department.
10. Handle top-level managers and orphans in the hierarchy, combining employee and manager views.
11. Find pairs of employees with the same hire year and department, then include location from dept.
12. List all employees and the next hired employee in the same department using MIN on hire_date greater than current.
13. Generate all pairs with salary differences, then group by dept_id to find max difference per dept.
14. Find managers who earn less than at least one of their reports using salary comparison.
15. Include all employees, even with unique hire dates, and list pairs sharing the date.
16. Show the full chain for each employee up to 3 levels, including managers.
17. Pair each employee with higher earners, then count per employee.
18. Aggregate the total salary of all direct and indirect reports for top managers.
19. Find report-manager pairs, then use CASE to flag if report was hired after manager.
20. Get the previous salary ordered by hire_date per dept.
21. Generate all employee-dept combinations, filter to wrong depts, and count potential moves.
22. Find employees who are neither managers nor have managers using NULL checks.
23. List all reports grouped by manager, including average report hire year.
24. Find crowded hire dates by grouping by hire_date and filtering counts greater than 1, within same dept.
25. Pair employees with all later hires under the same manager, then sum their salaries per employee.
26. Find max salary per manager's reports, then compare to manager's salary.
27. List all employees and their department peers, concatenating names.
28. Find inter-dept pairs in the same city.
29. Flatten the entire org structure starting from top managers.
30. Find for each employee the closest hire date match, handling NULLs.
