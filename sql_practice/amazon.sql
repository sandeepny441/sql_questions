select
  amazon_books.book_id,
 sum(ifnull(amazon_books.unit_price * amazon_books_order_details.quantity,0)) as total_rev
from
  amazon_books
  LEFT JOIN amazon_books_order_details ON amazon_books.book_id = amazon_books_order_details.book_id
group by
  amazon_books.book_id
---------------------------------------------
select
  users_training.u_name,
  DATE(training_details.training_date) as tr_Date,
  training_details.training_id as training_id,
  count(training_details.training_id) as tc
from
  users_training
  inner join training_details ON users_training.u_id = training_details.u_id
group by
  1,
  2,
  3
having
  tc >= 2
  ---------------------------------------------
--2132
WITH FirstLastCalls AS (
    SELECT
        caller_id,
        DATE(date_called) as call_date,
        MIN(date_called) as first_call_time,
        MAX(date_called) as last_call_time
    FROM
        caller_history
    GROUP BY
        caller_id,
        DATE(date_called)
),
FirstCallRecipient AS (
    SELECT
        f.caller_id,
        f.call_date,
        c.recipient_id as first_call_recipient_id
    FROM
        FirstLastCalls f
    JOIN
        caller_history c ON f.caller_id = c.caller_id AND f.first_call_time = c.date_called
),
LastCallRecipient AS (
    SELECT
        f.caller_id,
        f.call_date,
        c.recipient_id as last_call_recipient_id
    FROM
        FirstLastCalls f
    JOIN
        caller_history c ON f.caller_id = c.caller_id AND f.last_call_time = c.date_called
)
SELECT
    f.caller_id,
    f.first_call_recipient_id as recipient_id,
    f.call_date
FROM
    FirstCallRecipient f
JOIN
    LastCallRecipient l ON f.caller_id = l.caller_id AND f.call_date = l.call_date
WHERE
    f.first_call_recipient_id = l.last_call_recipient_id;
---------------------------------------------
SELECT 
  employee_id, 
  COUNT(CASE WHEN customer_response ~ '(^|[^0-9])[0-9]{10}([^0-9]|$)' THEN 1 END) AS phone_number_count 
  --MYSQL COUNT(CASE WHEN customer_response REGEXP '(^|[^0-9])[0-9]{10}([^0-9]|$)' THEN 1 END) AS phone_number_count 

FROM 
  customer_responses 
GROUP BY 
  employee_id;

-----------------------------------------------
with x as 
(
SELECT 
  employee_id, 
  COUNT(CASE WHEN customer_response ~ '(^|[^0-9])[0-9]{10}([^0-9]|$)' THEN 1 END) AS phone_number_count 
FROM 
  customer_responses 
GROUP BY 
  employee_id
 )
 
select employee_id, phone_number_count
from 
(
select employee_id, phone_number_count, 
DENSE_RANK() over(order by phone_number_count DESC) as den_RANK
from x ) as temp_Q
where den_RANK = 1
-----------------------------------------------
with x as 
(select 
EXTRACT(MONTH from book_orders.order_date) as month_x, 
SUM(amazon_books.unit_price *  book_orders.quantity) AS total_price
from amazon_books INNER JOIN book_orders
ON amazon_books.book_id = book_orders.book_id
WHERE EXTRACT(YEAR from book_orders.order_date) = 2022 
group by 1 
order by 1)

select month_x, total_price, 
round(AVG(total_price) over(order by month_x ASC)) as rolling_avg_price
from x
-----------------------------------------------
with x1 as 
(
select 
product_category, 
product_name, 
CAST(REGEXP_SUBSTR(price, '(([0-9]+.)[0-9]+)') AS float) as new_price 
from innerwear_amazon_com), 
x2 as 
(
select 
product_category, 
product_name, new_price, 
DENSE_RANK() over(partition by product_category order by new_price DESC) as den_rank
from x1 
) 
select product_category, 
product_name, new_price
from x2
where den_rank = 1
---------------------------------------------
