==============================================================================
SELECT 
# How would you retrieve all the destinations from the Trips table?
# select Destination from trips

# Can you fetch the TripName and Price for all trips that have a duration of more than 5 days?
# select TripName, Price from trips
# where DurationDays > 5

# How would you display the Destination and DurationDays for trips priced below $1000?
# select Destination, DurationDays from trips
# where Price < 1000

# What query would you use to get the TripName and DurationDays for all trips whose name contains the word "Tour"?
# select Destination, DurationDays from trips
# where TripName like '%Tour%'

# How do you select trips where the destination is either 'Rome' or 'Maldives'?
# select *from trips
# where Destination in ('Rome', 'Maldives')

==============================================================================

STAR  * 
# How would you fetch all columns and all rows from the Trips table?
# select * from trips

# If you wanted to view the entire record for trips with a duration of 7 days, how would you write the query?
# select * from trips
# where DurationDays = 7

# How can you see all details for trips that have 'Beach' in their TripName?
# select * from trips
# where TripName LIKE "%Beach%"

# Write a query that shows every column for trips that cost more than $1500.
# select * from trips
# where Price > 1500

# How would you retrieve the full details of the cheapest trip in the Trips table?
# select*from trips 
# where Price IN ( select min(Price) from trips)

================================================================================

COUNT 


# What query would give you the total number of trips offered in the Trips table?
# select count(*) from trips 

# How would you determine the number of trips that have a duration longer than 5 days?
# select count(*) from trips 
# where DurationDays > 5


# How can you count the number of trips with a destination of 'Maldives'?
# select count(*) from trips 
# where Destination = 'Maldives'


# Can you find out how many trips cost less than $1000?
# select count(*) from trips 
# where Price < 1000


# What would the query be to count the number of trips that have 'Adventure' in their TripName?
# select count(*) from trips 
# where TripName LIKE '%adventure%'

================================================================================
DISTINCT 

# How would you retrieve a list of unique destinations from the Trips table?
# select DISTINCT(TripName) from trips

# Can you get a list of unique DurationDays values from the table?
# select DISTINCT(DurationDays) from trips

# How do you find out the distinct price points for the trips?
# select DISTINCT(Price) from trips

# If you wanted to see the different words used in the TripName column (assuming each trip name contains only one word), how would you fetch them?
# select DISTINCT(TripName) from trips

# What query would you write to see all the unique combinations of Destination and DurationDays?
# select DISTINCT Destination, DurationDays from trips

=====================================================================
AND 
# How would you fetch trips that are priced between $500 and $1500?
select TripName 
from trips 
where Price between 500 and 1500


# Can you retrieve all trips with a destination of 'Maldives' that have a duration of 5 days?
select * 
from trips 
where Destination In ("Maldives")
and DurationDays < 7 

# Write a query to get the TripName and Price of trips that are priced above $1000 and have a duration less than 7 days.
select TripName, Price
from trips 
where Price > 1000
AND DurationDays < 7


# How do you select trips where the TripName contains the word "Beach" and the price is less than $1300?
select TripName, Price
from trips 
where TripName LIKE "%Beach%"
AND 
Price < 1300


# Can you find trips where the destination is 'New York' and the duration is exactly 3 days?
select TripName, Price
from trips 
where Destination in ("New York")
and DurationDays = 3 

=====================================================================
OR 
# How would you retrieve trips that are either priced below $600 or above $1800?
select * 
from Trips 
where Price < 600 
OR
Price > 1800


# Write a query to fetch trips that have a destination of either 'Amazon' or 'Sahara'.
select * 
from Trips 
where Destination IN ('Amazon', "Sahara")


# Can you get the TripName and Destination of trips that last for either 3 days or 8 days?
select TripName, Destination
from Trips 
where 
DurationDays = 3 


OR
DurationDays = 8

# How do you select trips where the TripName contains the word "Adventure" or the price is more than $1900?
select TripName 
from Trips 
where TripName like "%Adventure%"
or Price > 1900


# Write a query to retrieve all trips where the destination is either 'Himalayas' or 'Caribbean', or the duration is more than 9 days.
select * from
Trips 
where Destination in ("Himalayas", "Caribbean")
OR 
DurationDays = 9 


=====================================================================
aggregates

# Compute min, max, avg, count, sum of Price column.
select min(Price) from trips
select max(Price) from trips
select avg(Price) from trips
select sum(Price) from trips
select count(Price) from trips
select std(Price) from trips

=====================================================================

WHERE and ORDER BY

# How would you retrieve the TripName and Price for all trips priced above $1000, ordered by Price in descending order?
select TripName, Price 
from Trips 
where Price > 1000 
order by Price DESC


# Can you list the Destination and DurationDays for trips that have a duration of 5 days or more, ordered by the duration in ascending order?
select Destination, DurationDays from trips 
where DurationDays > 5 
order by DurationDays 

# Write a query to fetch the TripName and Destination for trips whose name contains the word "Tour", and order the results alphabetically by Destination.
select TripName, Destination from trips 
where TripName like "%Tour%"
order by TripName

# How do you select the TripName, Price, and DurationDays for trips where the destination is either 'Maldives' or 'New York', ordered by DurationDays in descending order?
select TripName, Price, DurationDays from trips 
where Destination IN ("New York", "Maldives")
order by DurationDays desc


# Can you retrieve all details about trips priced between $500 and $1500, sorted first by Price in ascending order and then by TripName in descending order?
select * from trips 
where Price BETWEEN 500 and 1500
order by Price ASC, TripName DESC

==================================================

GROUP BY 

# How would you count the number of trips for each destination?
select Destination, count(Tripname) from trips 
group by Destination

# How would you list the destinations and the count of trips for each destination?
select Destination, count(Tripname) from trips 
group by Destination

# Can you determine the average price of trips, grouped by their DurationDays?
select DurationDays, avg(Price) from trips 
group by DurationDays

# How would you retrieve the destinations with their highest trip prices, grouping by the Destination?
select Destination, max(Price) from trips 
group by Destination

==================================================
GROUP BY + HAVING 

# How would you find destinations that have more than 2 trip offerings, grouping by the Destination?
select Destination, count(TripName) 
from trips 
group by Destination
having count(TripName)>2

# Can you list the DurationDays values that have an average trip price greater than $1000, grouping by the duration?
select DurationDays, avg(Price) 
from trips 
group by DurationDays
having avg(Price) > 1000 


# Retrieve the destinations where the minimum trip price is above $500, grouping by the Destination.
select Destination, min(Price) 
from trips 
group by Destination
having min(Price)  >= 1000 


==================================================
GROUP BY + HAVING + WHERE 

# How would you identify destinations with more than 1 or more trip offering, but only considering trips that last 5 days or more? Group the results by Destination.
# select Destination, count(TripName) 
# from trips 
# where DurationDays >= 5
# group by Destination
# having count(TripName)  >= 1
 

# For trips that have 'Beach' in their TripName, can you determine the average price for each destination, but only include destinations where the average price is below $1500? Group the results by Destination.
# select Destination, avg(Price) 
# from trips 
# where TripName LIKE "%Beach%"
# group by Destination
# having avg(Price)   > 500
 

# Considering only trips that are priced above $700, how would you list the destinations with their minimum trip duration, but only include destinations where the minimum duration is 4 days or more? Group the results by Destination.
# select Destination, min(DurationDays) 
# from trips 
# where Price > 700
# group by Destination
# having min(DurationDays)   >= 4
==================================================
==================================================
==================================================


 


