# How would you retrieve the current date from the database?
# select sysdate() 

# Using the ChipotleMenu table, can you list the items added to the menu in the month of March? Hint: Use a function to extract the month from the DateAdded column.
# select ItemName from chipotlemenu
# where extract(month from DateAdded) = 3

# For analysis purposes, you want to know the day of the week for each DateAdded in the ChipotleMenu table. Can you extract and display the day of the week for each item's DateAdded value?
# select DateAdded, DAYOFWEEK(DateAdded) from chipotlemenu 


# Can you calculate and display the difference in days between the current date and the DateAdded for each item in the ChipotleMenu table?
# select Datediff(NOW(), DateAdded) from 
# chipotlemenu


# Assuming a scenario where the ChipotleMenu table also has a DateDiscontinued column, how would you calculate the number of days each item was available on the menu (i.e., the difference between DateDiscontinued and DateAdded)?
# select abs(Datediff(date_disc, dateAdded))
# from chipotlemenu


# You want to run a promotion on items added to the menu on the last day of any month. How would you identify such items from the ChipotleMenu table using date functions?
select itemName
from chipotlemenu
where Extract(day from DateAdded) = Extract(day from last_day(DateAdded))


# For a future marketing campaign, you want to see which items will have their 1-year anniversary from the DateAdded in the next 30 days. How would you retrieve such items from the ChipotleMenu table?
# SELECT Itemname 
# FROM chipotlemenu
# WHERE DATEDIFF(CURDATE(), DateAdded) BETWEEN 335 AND 365;


select datediff(DateAdded, Date_created) as date_diff
from 
(
select DateAdded, date_sub(DateAdded, interval 12 day) as Date_created
from chipotlemenu 
) as c1 

select last_day(DateAdded)
from chipotlemenu



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
=====================================================
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

