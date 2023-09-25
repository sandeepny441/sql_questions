==============================================================================
SELECT 
# How would you retrieve all the destinations from the Trips table?
# select Destination from trips
# Can you fetch the TripName and Price for all trips that have a duration of more than 5 days?
# select TripName, Price from trips
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

* 
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

How would you retrieve a list of unique destinations from the Trips table?
Can you get a list of unique DurationDays values from the table?
How do you find out the distinct price points for the trips?
If you wanted to see the different words used in the TripName column (assuming each trip name contains only one word), how would you fetch them?
What query would you write to see all the unique combinations of Destination and DurationDays?