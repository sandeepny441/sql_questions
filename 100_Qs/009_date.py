=================================================
# SELECT SYSDATE() 
# SELECT NOW() 
# SELECT CURRENT_TIME() 
# SELECT CUURENT_DATE()
==================================================
# DATE_ADD DATE_SUB DATEDIDD
==================================================
# select paymentDate, y_Date, m_date,datediff(paymentDate, y_date) as z_date 
# from 
# (
# select paymentDate, 
# DaTE_SUB(paymentDate, INTERVAL 220 DAY) as y_date, 
# DaTE_ADD(paymentDate, INTERVAL 20 DAY) as m_date
# from x 
# ) as temp_Q 
==================================================
# SELECT DAY('2023-07-08') 
# SELECT MONTH('2023-07-08')
# SELECT YEAR('2023-07-08')
# SELECT hour("2023-11-16 20:43:48") 
# SELECT MINUTE("2023-11-16 20:43:48") 
# SELECT second("2023-11-16 20:43:48") 
# SELECT MINUTE('2023-07-08')
# SELECT YEAR('2023-07-08')
# select extract(DAY from '2023-07-08')
# select extract(MONTH from '2023-07-08')
# select extract(HOUR from '2023-11-16 20:43:48')
==================================================
# SELECT DAYNAME('2023-07-08')
# SELECT MONTHNAME('2023-07-01')
# SELECT DAYOFWEEK('2023-07-12')
# SELECT DAYOFYEAR('2023-07-08')
# SELECT WEEK('2023-07-08')
# SELECT LAST_DAY("2023-07-08")
==================================================

# How would you query to find all records where the payment was made in the year 2004?
# Can you write a SQL query to count the number of payments made in each month of the year 2003?
# How would you extract the month and year from the paymentDate column in a SQL select statement?
# Could you demonstrate how to calculate the average payment amount for each quarter of the year 2004?
# Is it possible to list all customers with their most recent payment date using a SQL query?
# How can you determine the number of days between each payment and the current date?
# Can you write a SQL statement that shows the year with the highest total payment amount?
# What SQL function would you use to group payments by the day of the week they were made?
# Can you sort the records by the day of the month the payment was made, regardless of the month and year?
# How would you use SQL to find the first and last payment dates for each customer?

