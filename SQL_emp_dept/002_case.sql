-- CASE
1. Use a CASE statement to categorize employees as 'Senior' if hired before 2020, 'Mid' if between 2020 and 2022, and 'Junior' if after 2022.
2. Write a query to assign a bonus of 10000 to employees in Engineering using CASE, else 5000.

-- SUM(CASE WHEN) / COUNT(CASE WHEN)
3. Calculate the total salary for employees in departments with known locations using SUM(CASE WHEN).
4. Use SUM(CASE WHEN) to sum salaries only for employees who have a manager_id.
5. Count the number of employees earning more than 80000 using COUNT(CASE WHEN).
6. Use COUNT(CASE WHEN) to count employees hired in 2021 or later.

-- SUM / COUNT
7. Compute the total sum of all salaries, and explain how SUM handles NULL values.
8. Find the count of employees per department using GROUP BY and COUNT.

-- NULL vs Zero
9. Write a query to replace NULL salaries with 0 and then calculate the average salary.
10. Compare the results of COUNT(salary) vs SUM(CASE WHEN salary IS NULL THEN 0 ELSE 1 END) to highlight differences between NULL and zero in aggregations.
