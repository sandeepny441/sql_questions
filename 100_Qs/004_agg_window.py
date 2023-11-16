# SUM
# AVG 
# MAX
# MIN 
# COUNT 
# STDEV 
# VARIANCE

# select * from trips

# select *, 
# sum(Price) over(order by DurationDays) 
# from trips 

# select *, 
# min(Price) over(order by DurationDays) 
# from trips 

# select TripName, Price, 
# STDDEV_POP(DurationDays) over(order by Price) as c
# from trips 

# select TripName, Price, 
# variace(DurationDays) over(order by Price) as c
# from trips 


# How would you use an aggregate window function to calculate the running total of TicketPrice for flights departing from each DepartureAirport while listing all bookings?
# Can you write a query to display the average TicketPrice for flights to each Destination, along with each individual booking?
# How would you calculate the cumulative count of bookings made for each Destination up to and including each row in the result set?
# Could you demonstrate a window function that shows the maximum TicketPrice paid for each DepartureAirport alongside each booking, without using a GROUP BY clause?



# SELECT 
#   FlightDate,
#   TicketPrice,
#   QUARTER(FlightDate) AS Quarter,
#   AVG(TicketPrice) OVER (PARTITION BY QUARTER(FlightDate) ORDER BY FlightDate) AS MovingAvgQuarterly
# FROM navan;