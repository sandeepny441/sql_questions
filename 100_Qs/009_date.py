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