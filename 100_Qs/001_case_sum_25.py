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
# How would you use a CASE statement within the SUM function to calculate the total ticket sales for flights to London and Paris separately from the other destinations?
# select
# SUM(CASE WHEN Destination in ('London', 'Paris') THEN TicketPrice else 0 END) as total_price_PL, 
# SUM(CASE WHEN Destination NOT in ('London', 'Paris') THEN TicketPrice else 0 END) as total_price_not_PL 
# from navan 
# Can you write a query that uses CASE within the AVG function to determine the average ticket price for domestic flights (assuming flights within the same country are considered domestic) and international flights?
#  select AVG( CASE WHEN Destination ='London'THEN TicketPrice ELSE 0 END ) as L_Avg, AVG( CASE WHEN Destination ='Paris'THEN TicketPrice ELSE 0 END ) as P_avg from navan

# How would you use CASE and COUNT to count the number of bookings with a ticket price greater than $600, and another count for those with a ticket price of $600 or less?




# Can you create a query using CASE within the MIN and MAX functions to find the minimum and maximum ticket prices for flights departing before a certain date compared to those departing after that date?


# How would you write a query to sum the ticket prices for each destination, using CASE to apply a 10% discount to flights to Rome?


# Could you use CASE in conjunction with COUNT to differentiate between the number of flights to European destinations versus other destinations, given a list of European countries?



# Can you demonstrate how to use CASE with the SUM function to total ticket prices, categorizing them into price ranges (e.g., <$500, $500-$600, >$600)?
# How would you employ a CASE statement within AVG to find the average ticket price for flights on weekdays versus weekends?



# Can you use CASE and MIN to determine the earliest flight date for flights with a ticket price below the average price and flights with a ticket price above the average price?



# Could you write a query that uses CASE within the SUM function to calculate the total revenue from flights by quarter, assuming the fiscal year starts in April?
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


