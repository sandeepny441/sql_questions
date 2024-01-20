create view customer_details_view as 
select  customerName, salesRepEmployeeNumber, country, city 
from customers

select * from customer_details_view