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





