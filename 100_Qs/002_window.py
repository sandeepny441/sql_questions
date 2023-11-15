# you write a SQL query that uses the LAG window function to find the price difference between each trip and the one before it, sorted by price in ascending order?
# with temp_Q as 
# (select TripName, Price, 
# LAG(Price) over(order by Price) as prev_price 
# from trips)
# select TripName, Price, prev_price, (Price - prev_price) as price_diff


# select TripName, Price, prev_price, (Price - prev_price) as price_diff
# from (select TripName, Price, 
# LAG(Price) over(order by Price) as prev_price 
# from trips) as temp_Q
================================================================================================================
# How would you use the LEAD window function to predict the next trip's duration for each trip in the Trips table?

# select TripName, DurationDays, 
# Lead(DurationDays) over(order by TripID) as next_trip_duration
# from trips
================================================================================================================
# How would you write a SQL query to calculate a cumulative distribution of trip prices within each destination, to understand the relative position of each trip's price?

# select TripName, Destination, Price, 
# cume_dist(Price) over(partition by Destination order by Price) as cd_price
# from trips
================================================================================================================

# Can you formulate a SQL query to determine each trip's price as a percentage of the total price for all trips in its destination?



# select TripName, Destination, Price,  
#  Price / sum(Price) over(PARTITION by Destination) as pct_PRICE
# from trips 


# select TripName, Destination, Price,  
# sum(Price) over(PARTITION by Destination) as total_PRICE,
#  Price / sum(Price) over(PARTITION by Destination) as pct_PRICE
# from trips 

# select Destination, 
# sum(price)
# from trips 
# group by Destination

================================================================================================================

# How would you construct a SQL query that identifies the first trip of each destination that has a price above the average price of all trips within the same destination?

# SELECT Destination, TripName, Price
# FROM (
#     SELECT 
#         TripName, 
#         Destination, 
#         Price,
#         -- Use ROW_NUMBER() to get the first trip per destination with a price above average
#         ROW_NUMBER() OVER (PARTITION BY Destination ORDER BY TripID) as rank_this,
#         -- Calculate the average price per destination
#         AVG(Price) OVER (PARTITION BY Destination) as avg_price
#     FROM 
#         trips
# ) AS ranked_trips
# WHERE 
#     Price < avg_price
#     AND rank_this = 1;
================================================================================================================
# How would you create a SQL query to rank destinations based on the number of trips they offer, then provide a rank for each trip within those destinations based on price, displaying only the top 2 ranked trips for each destination?

    
# WITH 

# DestinationCounts AS (
# SELECT 
#     Destination, 
#     COUNT(*) AS TripCount
# FROM 
#     trips 
# GROUP BY 
#     Destination
# ), 


# DestinationRank AS (
# SELECT 
#     Destination, 
#     TripCount,
#     RANK() OVER (ORDER BY TripCount DESC) AS DestinationRank
# FROM 
#     DestinationCounts
# ), 


# RankedTrips AS (
# SELECT 
#     t.TripName, 
#     t.Destination, 
#     t.Price,
#     dr.DestinationRank,
#     RANK() OVER (PARTITION BY t.Destination ORDER BY t.Price DESC) AS PriceRank
# FROM 
#     trips t
# JOIN 
#     DestinationRank dr ON t.Destination = dr.Destination
# )


# SELECT 
#     Destination, 
#     TripName, 
#     Price, 
#     DestinationRank,
#     PriceRank
# FROM 
#     RankedTrips
# WHERE 
#     PriceRank <= 2
# ORDER BY 
#     DestinationRank, 
#     Destination, 
#     PriceRank;
================================================================================================================

# Can you create a SQL query that selects all products that have a price higher than the average price of products in their respective category?

# select p1.ProductID, p1.Price
# from products1 p1
# where p1.Price > 
# (select avg(p2.Price) from products1 p2 
# where p1.category = p2.category
# )
================================
select *,
max(Price) over(partition by DurationDays order by DurationDays DESC) as max 
from trips 