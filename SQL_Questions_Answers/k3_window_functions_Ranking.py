Ranking=========================	
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