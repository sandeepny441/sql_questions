==============================================
with x as 
(
select 
rc_users.company_id as company_id,
count(CASE WHEN 
  MONTH(rc_calls.date) = 3 and
  YEAR(rc_calls.date) = 2020
THEN rc_calls.user_id END) as march_count, 
count(CASE WHEN 
  MONTH(rc_calls.date) = 4 and
  YEAR(rc_calls.date) = 2020
THEN
rc_calls.user_id END) as april_count
from rc_calls inner join rc_users
ON rc_calls.user_id = rc_users.user_id
group by rc_users.company_id
)

select company_id, decline from 
(
select company_id, 
april_count - march_count as decline, 
DENSE_RANK() over(order by (april_count - march_count) ASC) as den_RANK
from x 
) as temp_Q
where den_RANK = 1
==============================================
select avg(call_duration)
from 
(
select 
request_id, 
created_on, 
call_duration,
ROW_NUMBER() over(partition by request_id order by created_on ASC) as row_num
from redfin_call_tracking
) as temp_Q
where row_num = 1
==============================================
select COUNT(request_id)
from 
(
select 
request_id, count(created_on)
from 
redfin_call_tracking
where HOUR(created_on) between 15 and 18
group by request_id
having count(created_on) >= 3 
) as temp_Q
==============================================
SELECT 
    plans.billing_cycle, 
    signups.signup_id,
    AVG(transactions.amt) as avg_txn_amt
FROM 
    plans 
INNER JOIN 
    signups ON plans.id = signups.plan_id
INNER JOIN 
    transactions ON signups.signup_id = transactions.signup_id
WHERE 
    transactions.transaction_start_date < DATE_SUB('2021-03-01', INTERVAL 10 MONTH)
GROUP BY 
    plans.billing_cycle, 
    signups.signup_id
ORDER BY 
    plans.billing_cycle DESC, 
    signups.signup_id ASC 
==============================================
select
  DAYNAME(customer_placed_order_datetime) as dayname,
  HOUR(customer_placed_order_datetime) as HOUR,
  round(
    avg(
      order_total + tip_amount - discount_amount - refunded_amount
    ), 2) as acg_earenings
from
  doordash_delivery
group by
  1,
  2
==============================================
select
  HOUR(customer_placed_order_datetime) as HOUR,
  AVG(order_total + tip_amount - discount_amount - refunded_amount)  as total_order
from
  doordash_delivery
  where 
  HOUR(customer_placed_order_datetime) BETWEEN 15 and 17 
  AND 
  delivery_region = "San Jose"
group by 1
==============================================
select 
QUARTER(sf_sales_amount.sales_date) as Quarter, 
sum(sf_sales_amount.sales_amount * sf_exchange_rate.exchange_rate) as total_sales
from sf_exchange_rate inner join sf_sales_amount
ON sf_exchange_rate.source_currency = sf_sales_amount.currency
AND 
sf_exchange_rate.date = sf_sales_amount.sales_date
where QUARTER(date) between 1 and 2 
and YEAR(date) = 2020
group by 1
==============================================
with
  x as (
    select
      linkedin_city.city_name as city_nam,
      linkedin_country.country_name as country,
      count(linkedin_customers.id) as cust_count
    from
      linkedin_country
      inner join linkedin_city ON linkedin_city.country_id = linkedin_country.id
      inner join linkedin_customers ON linkedin_city.id = linkedin_customers.city_id
    group by
      1,
      2
  )
select
  country,
  city_nam,
  cust_count
from
  x
where
  cust_count > (
    select
      avg(cust_count)
    from
      x
  )
==============================================
with temp as 
(
select *, 
DENSE_RANK() over(order by net_time ASC) as den_RANK
from marathon_male
)

select 
x.net_time - y.net_time
from temp x inner join temp y
where 
x.person_name = 'Chris Doe'
AND y.den_RANK = 10
LIMIT 1
==============================================
select
  postmates_partners.name,
  AVG(postmates_orders.amount) as avg_amount
from
  postmates_orders
  inner join postmates_markets ON postmates_orders.city_id = postmates_markets.id
  inner join postmates_partners ON postmates_orders.seller_id = postmates_partners.id
where
  postmates_partners.name LIKE '%Pizza%'
  AND postmates_markets.name = 'Boston'
group by
  postmates_partners.name
==============================================
==============================================
==============================================