
ROW_NUMBER
RANK
DENSE_RANK 
CUME_DIST
PERCENT_RANK 
NTILE
--------------------------------------
# ROW_NUMBER
# select saleID, 
# row_number() over(order by saleAmount) as row_number
# from bestbuySales 
--------------------------------------
# RANK
# select saleID, 
# rank() over(order by saleAmount) as rank_sale_amount
# from bestbuySales
--------------------------------------
# DENSE_RANK 
# select saleID, 
# dense_rank() over(order by saleAmount) as dense_rank_amount
# from bestbuySales
--------------------------------------
# CUME_DIST
# select saleID, 
# cume_dist() over(order by saleAmount) as cume_dist_amount
# from bestbuySales
--------------------------------------
# PERCENT_RANK 
# select saleID, 
# percent_rank() over(order by saleAmount) as percent_rank_amount
# from bestbuySales
--------------------------------------
# NTILE
select saleID, 
Ntile(4) over(order by saleamount) as ntile_amount
from bestbuysales
--------------------------------------



# SELECT 
#     SaleID, 
#     ProductCategory, 
#     SaleAmount,
#     NTILE(2) OVER (ORDER BY SaleAmount) AS SaleGroup
# FROM 
#     BestBuySales;


ROW_NUMBER
RANK
DENSE_RANK 
CUME_DIST
PERCENT_RANK 
NTILE
# ============================
# How would you write a SQL query to assign a unique sequential integer to rows within each category of products sorted by price in ascending order?
# select ProductID, category, 
# ROW_NUMBER() over(partition by category order by Price ASC) as rn 
# from products1

# Can you create a SQL query to display a list of orders for each customer, numbered sequentially based on the order date?
# select ProductID, Price, 
# ROW_NUMBER() over(order by Price DESC) as rn 
# from products1

# ==========================================
# RANK

# select ProductID, Category,Price, 
# rank() over(partition by category order by Price) as rank_this
# from products1


# DENSE_RANK

# Write a SQL query to rank products by price within each category such that products with the same price have the same rank and there are no gaps in ranking sequence.

# select ProductID,  Price, category, 
# rank() over(partition by category order by Price) as normal_R,
# dense_rank() over(partition by category order by Price) as desne_R
# from products1


# CUME_DIST

# How would you formulate a SQL query to determine the cumulative distribution of employee salaries within the company to understand salary dispersion?

# select ProductID, Category, Price, 
# cume_dist() over(partition by Category order by Price) as CD 
# from products1


# PERCENT_RANK
# How would you use SQL to calculate the percent rank of products' prices within each category
# select ProductID, Category, Price, 
# PERCENT_RANK() over(partition by Category order by Price) as percent_R
# from products1

# NTILE
# select ProductID, Price, 
# NTILE(4) over(partition by Category order by Price) as nt 
# from products1

# Rank Window Functions:
# How can you create a rank for each booking based on the TicketPrice within each DepartureAirport, with the highest price being rank 1?

# select BookingID, TicketPrice, DepartureAirport, 
# rank() over(partition by DepartureAirport order by TicketPrice DESC) as rank1
# from navan 

# # Can you write a SQL query that assigns a dense rank to each booking within each Destination based on the FlightDate?

# select BookingID, Destination, FlightDate, 
# DENSE_RANK() over(partition by Destination order by FlightDate) as rank1 
# from Navan 

# # How would you use window functions to give a row number to each booking, ordered by TicketPrice descending, partitioned by DepartureAirport?

# select bookingID, DepartureAirport, TicketPrice, 
# ROW_NUMBER() over(PARTITION by DepartureAirport order by TicketPrice DESC) as rn 
# from navan 

# # Could you write a query that finds the rank of each booking based on TicketPrice for flights departing in July, using a window function?

# select BookingID, DepartureAirport,
# rank() over(order by TicketPrice) as rank1 
# from navan
# where month(FlightDate) = 7 




# General Window Function Questions:
# How can you modify the dataset to include a column that shows the percent rank of each TicketPrice within its DepartureAirport?

# select BookingID, TicketPrice, DepartureAirport, 
# PERCENT_RANK() over(PARTITION by DepartureAirport
# order by FlightDate) as pct_Rank 
# from navan 


# # Can you display a list of bookings with a column that shows the rank of each flight's TicketPrice when compared within the same month of FlightDate?

# select TicketPrice, FlightDate, month(FlightDate) as month,
# rank() over(partition by month(FlightDate) order by TicketPrice DESC) as rank_p from navan 



# # How would you generate a column that lists the TicketPrice as a percentage of the total price of all tickets in the dataset?

# select BookingID, TicketPrice, 
# concat(CUME_DIST() over(order by TicketPrice)* 100, "%") as pct_price  
# from navan 


# SELECT 
#   BookingID, 
#   TicketPrice, 
#   (TicketPrice / SUM(TicketPrice) OVER ()) * 100 AS PctOfTotalPrice
# FROM navan;


# # Could you create a query that shows the TicketPrice as a running total percentage of the overall sum of TicketPrice for the dataset?
# SELECT 
#   BookingID, 
#   TicketPrice, 
#   (SUM(TicketPrice) OVER (order by BookingID
#   rows BETWEEN UNBOUNDED PRECEDING and CURRENT ROW)
#    /  SUM(TicketPrice) OVER ())* 100 AS PctOfTotalPrice
# FROM navan;

