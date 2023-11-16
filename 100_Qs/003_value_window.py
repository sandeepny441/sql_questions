# FIRST_VALUE
# LAST_VALUE
# LAG
# LEAD 
# NTH_VALUE


# select *, 
# first_value(Price) over() as c
# from trips

# select *, 
# last_value(Price) over() as c
# from trips

# select *, 
# lead(Price) over(order by Price) as c 
# from trips 

# select *, 
# lag(Price) over(order by Price) as c 
# from trips 

# select *, 
# NTH_VALUE(Price, 4) over(order by Price) as c 
# from  trips

# SELECT 
#     TripName, 
#     Price,
#     NTH_VALUE(Price, 4) OVER (
#         ORDER BY Price 
#         ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
#     ) AS FourthPrice
# FROM 
#     trips;

==============================================
LEAD
==============================================
# Can you write a SQL query that displays the current product's price along with the price of the next product in the same category? This will help in comparing the price differences within the same category.
# select Price, Category, 
# lead(Price) over(partition by Category order by ProductID) as next_price 
# from products1
------------------------------------------------------------------
# How would you create a SQL query that shows each product along with the next higher priced product within the same category? This could be useful to analyze the price trend within each category.

# select ProductID, Price, 
# lead(Price) over(partition by category order by Price DESC) as next_p 
# from products1
------------------------------------------------------------------
# Can you formulate a SQL query that lists each product's price and the price of the following product in the dataset, regardless of the category, to understand how prices transition from one product to another across categories?

# select productID, Price, 
# lead(Price) over(order by ProductID) as next_p
# from products1
------------------------------------------------------------------
==============================================
LAG
==============================================

# Price Difference Analysis:
# How would you write a SQL query using the LAG function to find the difference in price between each product and its predecessor within the same category? This would be useful to track price changes or discounts in product pricing over time.
# select Category, Price, 
# lag(Price) over(partition by category order by ProductID) as prev_p, 
# Price - lag(Price) over(partition by Category order by ProductID) as pr_diff
# from products1

------------------------------------------------------------------
# Historical Price Comparison:
# Can you create a SQL query to display each product along with its current price and the price it had the last time it appeared in the inventory? Assume that the ProductID reflects the chronological order of the inventory stock updates.

# select ProductID, Price, 
# lag(Price) over(order by ProductID) as prev_P
# from products1
------------------------------------------------------------------
# Sequential Category Trend:
# Formulate a SQL query that uses the LAG function to list each product's category and price, as well as the category and price of the product that was added to the inventory immediately before it, regardless of the category. This might reveal trends or shifts in the types of products being stocked.

# select ProductID, Category, Price, 
# lag(Category) over(order by ProductID) as prev_cat,
# lag(Price) over(order by ProductID) as prev_pr
# from products1
------------------------------------------------------------------
==============================================
LAG
==============================================



# How can you use a window function to show the difference in TicketPrice between each booking and the previous booking for the same DepartureAirport?

# select DepartureAirport, TicketPrice, 
# TicketPrice - LAG(TicketPrice, 1, 0) over(PARTITION by DepartureAirport ORDER by FlightDate) as price_diff
# from navan

# # Can you write a query that displays each booking with the TicketPrice of the next booking for the same Destination?

# select BookingID, TicketPrice,
# lead(TicketPrice) over(partition by Destination order by BookingID) as next_p 
# from navan


# # How would you use a window function to calculate a three-booking moving average of TicketPrice for each DepartureAirport?
# SELECT 
#   BookingID, 
#   DepartureAirport, 
#   TicketPrice, 
#   AVG(TicketPrice) OVER (
#     PARTITION BY DepartureAirport 
#     ORDER BY BookingID 
#     ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
#   ) AS MovingAvg3Booking
# FROM navan;


# # Could you show how to display each booking with an additional column that shows the TicketPrice increase compared to the first booking in the dataset?
# select BookingID, FlightDate, TicketPrice, 
# lead(TicketPrice)  over(order by FlightDate)  - TicketPrice as price_diff 
# from navan 

