



select * from KFC_menu
LEFT JOIN KFC_orders
on KFC_menu.itemID = KFC_orders.itemID

UNION 

SELECT * FROM KFC_menu
RIGHT JOIN KFC_orders
ON KFC_menu.itemID = KFC_orders.itemID;





-- used when we need to store all historical data 