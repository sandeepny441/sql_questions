
SELECT CURRENT_DATE()
SELECT SYSDATE()

SELECT CURRENT_TIME()
SELECT NOW()


SELECT DATEDIFF('2023-12-31', '2023-01-01')
SELECT DATE_ADD('2023-01-01', INTERVAL 1 MONTH)
SELECT DATE_SUB('2023-12-31', INTERVAL 1 MONTH)

SELECT YEAR('2023-07-08')   SELECT EXTRACT(YEAR FROM order_date) 
SELECT MONTH('2023-07-08')
SELECT DAY('2023-07-08')
SELECT HOUR('15:30:45')
SELECT MINUTE('15:30:45')
SELECT SECOND('15:30:45')

SELECT DAYNAME('2023-07-08')
SELECT MONTHNAME('2023-07-01')
SELECT DAYOFWEEK('2023-07-08')
SELECT DAYOFYEAR('2023-07-08')
SELECT WEEK('2023-07-08')

--===========================================================================
--===========================================================================
--===========================================================================


SELECT CURRENT_DATE


SELECT CURRENT_TIMESTAMP


SELECT EXTRACT(YEAR FROM order_date) 
FROM orders


SELECT DATE_ADD(order_date, INTERVAL 30 DAY) 
FROM orders


SELECT DATE_SUB(order_date, INTERVAL 1 MONTH)
FROM orders


SELECT DATEDIFF(order_date, shipped_date) 
FROM orders


SELECT DATE_FORMAT(order_date,'%m-%d-%Y') 
FROM orders 

SELECT ADD_MONTHS(order_date, 3)
FROM orders

SELECT LAST_DAY(order_date) 
FROM orders

-- select orderDate, MONTHNAME(orderDate) from orders
-- select orderDate, DAYNAME(orderDate) from orders
-- SELECT orderDate, DAYOFYEAR(orderDate) from orders
-- ORDER BY DAYOFYEAR(orderDate) DESC
SELECT WEEK('2023-1-2')


