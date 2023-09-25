# How would you classify trips into two categories: 'Expensive' if the price is above $1000 and 'Affordable' otherwise? Display the TripName and its category.

# select Tripname, 
# CASE 
# when Price > 1000 THEN 'Expensive' 
# ELSE 'Affordable'
# END AS category 
# from trips

# select Tripname, 
# if(price> 1000, 'Expensive', 'Affordable') as category 
# from trips 

# Can you determine whether each trip is 'Short' if its duration is less than 5 days, 'Medium' if its duration is between 5 and 7 days, and 'Long' otherwise? Show the TripName and its duration category.
# select TripName, DurationDays, 
# CASE 
# when DurationDays < 5 then 'short'
# when DurationDays >= 5 and DurationDays< 7 then 'medium'
# else 'long'
# END as category 
# from trips 

# How would you display trips with their names and a label 'Popular' if the destination is 'Maldives', and 'Regular' for all other destinations?
# select TripName,
# case 
# when Tripname LIKE '%maldives%' then 'Popular'
# ELSE 'Regular'
# END as category 
# from trips 

# Can you label each trip based on its name containing 'Beach'? If it contains 'Beach', label it 'Beach Trip', otherwise label it 'Other Trip'. Show the TripName and its type.
# select TripName,
# case 
# when Tripname LIKE '%Beach%' then 'BeachTrip'
# ELSE 'Other'
# END as category 
# from trips 
=============================================================
# For each trip, can you display its name and classify its price range as 'Low' for prices below $500, 'Medium' for prices between $500 and $1500, and 'High' for prices above $1500?
# select tripname, 
# if(price < 500, 'low', 'high') as category
# from trips
How would you categorize each trip's duration as 'Weekend' if it lasts for 2 or 3 days, 'Weeklong' if it lasts for 7 days, and 'Variable' for other durations? Show the TripName and its duration type.
Based on the destinations, can you label each trip as 'Tropical' if it's either 'Maldives' or 'Caribbean', and 'Other' for all other destinations? Display the Destination and its category.
Can you categorize each trip based on its name containing the word 'Tour'? If it contains 'Tour', label it 'Tour Package', and if it contains 'Adventure', label it 'Adventure Package'. For all other trips, label them 'Standard Package'. Show the TripName and its package type.


=============================================================
USE if else, when there are only 2 conditions
USE case when then else, when there are more than 2 conditions
=============================================================