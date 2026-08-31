-- t.ly/vYR0z
WITH
ManagerSalary AS (
    SELECT
        e.empl_id,
        e.salary
    FROM
        dim_employee e
    WHERE
        e.empl_id IN (
            SELECT DISTINCT
                manager_empl_id
            FROM
                map_employee_hierarchy
        )
),
EmployeeAverageSalary AS (
    SELECT
        m.manager_empl_id,
        AVG(e.salary) AS avg_salary
    FROM
        map_employee_hierarchy m
        INNER JOIN dim_employee e ON m.empl_id = e.empl_id
    GROUP BY
        m.manager_empl_id
    )
SELECT
    m.empl_id AS manager_id,
    m.salary AS manager_salary,
    e.avg_salary
FROM
    ManagerSalary m
    INNER JOIN EmployeeAverageSalary e ON m.empl_id = e.manager_empl_id
WHERE
    m.salary < (2 * e.avg_salary);

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
--t.ly/Vp4kS
select DISTINCT
    t1.number as num1,
    t2.number as num2
from
    transportation_numbers t1
    inner join transportation_numbers t2 ON t1.index <> t2.index
where
    t1.number < t2.number
    AND (t1.number * t2.number) > 11

--------------------
select DISTINCT
    t1.number as num1,
    t2.number as num2,
    t3.number as num3
from
    transportation_numbers t1
    inner join transportation_numbers t2 ON t1.number <> t2.number
    inner join transportation_numbers t3 ON t2.number <> t3.number
    AND t1.number <> t3.number
where
  (t1.number + t2.number + t3.number) = 8
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
--t.ly/pjmLC
select
    max(DATEDIFF(next_hire_date, hire_date)) as max_hire,
    max(DATEDIFF(next_term_date, termination_date)) as max_fire
from
    (
    select DISTINCT
        hire_date,
        termination_date,
        LEAD(hire_date) OVER (
            order by
                hire_date
        ) as next_hire_date,
        LEAD(termination_date) OVER (
            order by
                termination_date
        ) as next_term_date
    from
        uber_employees
    order by
        hire_date ASC,
        termination_date ASC
) as temp_Q
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
--t.ly/ueJuD
with
  x as (
    select
      loans.created_at as x_date,
      loans.user_id as user_id,
      submissions.balance as balance,
      RANK() over (partition by loans.user_id order by loans.created_at DESC) as this_rank
    from
      loans
      inner join submissions ON loans.id = submissions.loan_id
    where
      loans.type = 'Refinance'
  )
select
  user_id,
  balance
from
  x
where
  this_rank = 1
 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
-- some SQL engines do not allow the use of aliases in the HAVING clause. You have to repeat the aggregate expression instead
------------------------------------------------------------------

--10008

select 
sum(CASE WHEN `index` < 5 THEN number END) as sum
from transportation_numbers

UNION ALL 

select 
sum(number) as sum
from transportation_numbers
where `index` > 5

--  HAHA
 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

--10180
select 
facility_name, 
score from 
(select 
facility_name, 
score, 
DENSE_RANK() over(partition by facility_name order by score ASC) as den_rank
from los_angeles_restaurant_health_inspections
where facility_address LIKE "%Hollywood BLVD%"
) as temp_Q
where den_rank = 1
-----------------------------------------------------
select 
facility_name, 
score from 
(select 
facility_name, 
score, 
ROW_NUMBER() over(partition by facility_name order by score ASC) as rn
from los_angeles_restaurant_health_inspections
where facility_address LIKE "%Hollywood BLVD%"
) as temp_Q
where rn = 1
-----------------------------------------------------
SELECT
    facility_name,
    MIN(score) AS min_score
FROM
    los_angeles_restaurant_health_inspections
WHERE
    facility_address LIKE '%HOLLYWOOD BLVD%'
GROUP BY
    facility_name
ORDER BY
    min_score DESC,
    facility_name ASC;
 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

-- 9876
select 
hotel_name, count(negative_review) as n_count
from hotel_reviews
where negative_review NOT LIKE "%No Negative%"
group by hotel_name
order by n_count DESC
LIMIT 2

-----------------------------------------------------
select
hotel_name, n_count
from 
(
select 
hotel_name, count(negative_review) as n_count, 
ROW_NUMBER() over(order by count(negative_review) DESC) as row_n
from hotel_reviews
where negative_review NOT LIKE "%No Negative%"
group by hotel_name
) as temp_Q
where row_n <  3 
 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
 --9881
Make a report showing the number of survivors and non-survivors by passenger class.
Classes are categorized based on the pclass value as:
pclass = 1: first_class
pclass = 2: second_classs
pclass = 3: third_class
Output the number of survivors and non-survivors by each class.

==============================================================
select 
pclass, 
SUM(case when survived = 1 THEN 1 END) as 'survived', 
SUM(case when survived = 0 THEN 1 END) as 'not_survived'
from titanic
group by pclass
==============================================================
select 
survived, 
SUM(case when pclass = 1 THEN 1 END) as 'first_class', 
SUM(case when pclass = 2 THEN 1 END) as 'second_classs', 
SUM(case when pclass = 3 THEN 1 END) as 'third_class'
from titanic
where survived = 0

UNION ALL 

select 
survived, 
SUM(case when pclass = 1 THEN 1 END) as 'first_class', 
SUM(case when pclass = 2 THEN 1 END) as 'second_classs', 
SUM(case when pclass = 3 THEN 1 END) as 'third_class'
from titanic
where survived = 1
==============================================================
--2063 SELF JOIN comparing values at multiple dates on SELF 
select 
jan.source_currency, 
july.exchange_rate - jan.exchange_rate as diff
from sf_exchange_rate jan inner join sf_exchange_rate july
ON jan.source_currency = july.source_currency
where jan.date = '2020-01-01'
AND 
july.date = '2020-07-01'
==============================================================
--2154 -- comparing timeStamps part 
select dayName, session, total_sales
from
(
SELECT 
    DAYNAME(DATE(timestamp)) AS dayName,
    CASE 
        WHEN TIME(timestamp) >= '00:00:00' AND TIME(timestamp) < '12:00:00' THEN 'Morning'
        WHEN TIME(timestamp) >= '12:00:00' AND TIME(timestamp) < '15:00:00' THEN 'Early afternoon'
        WHEN TIME(timestamp) >= '15:00:00' THEN 'Late afternoon'
    END AS session,
    COUNT(order_id) AS total_sales, 
    DENSE_RANK() over(order by  COUNT(order_id) DESC) as den_rank
FROM 
    sales_log
GROUP BY 1, 2
) as temp_Q
where den_rank <=2
==============================================================
