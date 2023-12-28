SUM
AVG 
MAX
MIN 
COUNT 
STDEV 
VARIANCE


# select saleID, saleamount,ProductCategory,
# sum(saleamount) over(partition by ProductCategory order by saleamount) as running_total
# from bestbuysales

# select saleID, saleamount,ProductCategory,
# avg(saleamount) over(partition by ProductCategory order by saleamount) as running_average
# from bestbuysales

# select saleID, saleamount,ProductCategory,
# max(saleamount) over(partition by ProductCategory order by saleamount) as running_max
# from bestbuysales


# select saleID, saleamount,ProductCategory,
# min(saleamount) over(partition by ProductCategory order by saleamount) as running_min
# from bestbuysales

# select saleID, saleamount,ProductCategory,
# count(saleamount) over(partition by ProductCategory order by saleamount) as running_count
# from bestbuysales


# SELECT 
# SaleID, 
# ProductCategory, 
# SaleAmount,
# STDDEV(SaleAmount) OVER (PARTITION BY ProductCategory) AS StdDevByCategory
# FROM 
# BestBuySales


# SELECT 
# SaleID, 
# ProductCategory, 
# SaleAmount,
# variance(SaleAmount) OVER (PARTITION BY ProductCategory) AS variance_by_Category
# FROM 
# BestBuySales



