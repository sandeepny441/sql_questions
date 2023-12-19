second highest salary 



SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM A
) AS RankedSalaries
WHERE rnk = N;


select salary from A 
order by salary DESC 
LIMIT 1 offset 1


select max(salary) from A 
where salary NOT IN 
(select max(salary) in A)

select max(e1.salary) from A e1 join A e2 
on e1.salary < e2.salary 
