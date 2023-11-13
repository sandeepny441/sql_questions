# FIRST_VALUE
# LAST_VALUE
# LAG
# LEAD 
# NTH_VALUE

# select SaleID, SaleAmount, 
# first_value(SaleAmount) over(partition by saleID order by SaleID) as f_value
#  from bestbuysales

# select SaleID, SaleAmount, 
# last_value(SaleAmount) over(partition by saleID order by SaleID) as f_value
#  from bestbuysales

# select saleID, saleAmount,
# lead(saleAmount) over(order by saleID) as next_value 
# from bestbuysales

# select saleID, saleAmount,
# lag(saleAmount) over(order by saleID) as prev_value 
# from bestbuysales

# SELECT 
#     SaleID, 
#     SaleAmount,
#     NTH_VALUE(SaleAmount, 3) OVER (ORDER BY SaleID) AS SecondSaleAmount
# FROM 
#     BestBuySales;