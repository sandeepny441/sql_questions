==================================================================================================================
# Can you write a SQL query using a CASE statement to categorize each trip's price into 'Budget', 'Standard', or 'Premium', depending on whether the price is below 800, between 800 and 1500, or above 1500, respectively?
# select TripName, 
# CASE 
# WHEN price < 800 THEN 'Budget'
# WHEN price > 800 and Price < 1500 THEN 'Standard'
# ELSE 'Premium'
# END as Price_category 
# from trips
==================================================================================================================
# Can you write a SQL query to calculate the total sum of prices for all trips that have a duration longer than 5 days?
# select TripName,
# sum(case when  DurationDays > 5 THEN Price ELSE 0 END) as Price_this
# from trips
# group by TripName
==================================================================================================================
# Write a SQL query to calculate the total sum of prices for all 'Historical Tour' trips, and use a CASE statement to include a 10% discount on the original price for those with a duration of 4 days or less.

# select TripName, 
# sum(CASE When DurationDays <=4 THEN Price* 0.9 ELSE Price END) as total_price 
# from trips 
# where TripName = "Historical Tour"
=================================================================================================================
# Can you calculate the total price for trips where the duration is greater than 7 days using a CASE statement in SQL?
# select TripName, 
# SUM(CASE WHEN DurationDays > 7 THEN PRICE ELSE 0 END) as total_price 
# from trips 
# group by TripName
==================================================================================================================
# Can you write a SQL query to find the total revenue expected from all trips where the destination is either 'Maldives' or 'Himalayas', but apply a 5% increase in price for 'Maldives' trips and a 10% reduction for 'Himalayas' trips?

# select TripName, 
# SUM(CASE WHEN Destination = 'Maldives' THEN Price * 0.95
# ELSE Price * 0.9 END) as total_price
# from trips
# WHERE Destination IN ("Maldives", "Himalayas")
# group by TripName
================================================================================================================

================================================================================================================







================================================================================================================







================================================================================================================








================================================================================================================







================================================================================================================








================================================================================================================









================================================================================================================







================================================================================================================






================================================================================================================







================================================================================================================






================================================================================================================






================================================================================================================





================================================================================================================





================================================================================================================






================================================================================================================






================================================================================================================






================================================================================================================


