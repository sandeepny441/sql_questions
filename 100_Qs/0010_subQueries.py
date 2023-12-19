# Can you write a subquery to find the average ticket price and then use it in the main query to list all flights where the ticket price is above this average?

select BookingID, TicketPrice 
from navan where TicketPrice > 
(select avg(TicketPrice) from navan)

# How would you use a subquery to determine the maximum ticket price for flights to London and then select all bookings that have a ticket price equal to this maximum?

select BookingID, TicketPrice from navan 
where TicketPrice IN (
select max(TicketPrice) from navan 
where Destination = 'London')

# Could you create a subquery that identifies the earliest flight date in the dataset and then use it to find all flights that occurred on that date?s

select BookingID, FlightDate from navan 
where FlightDate IN (
select min(FlightDate) from navan 
where Destination = 'London')



