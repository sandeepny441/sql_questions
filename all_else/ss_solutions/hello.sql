select 
sum(cost_in_dollars * units_sold)
from online_orders oo
inner join 


online_customers oc
ON oo.customer_id = oc.id 
AND oc.state = 'Oregon'
where month(date) = 4
group by  oc.state