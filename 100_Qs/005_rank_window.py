ROW_NUMBER
RANK
DENSE_RANK 
CUME_DIST
PERCENT_RANK 
NTILE
# ============================
# How would you write a SQL query to assign a unique sequential integer to rows within each category of products sorted by price in ascending order?
# select ProductID, category, 
# ROW_NUMBER() over(partition by category order by Price ASC) as rn 
# from products1

# Can you create a SQL query to display a list of orders for each customer, numbered sequentially based on the order date?
# select ProductID, Price, 
# ROW_NUMBER() over(order by Price DESC) as rn 
# from products1

# ==========================================
# RANK

# select ProductID, Category,Price, 
# rank() over(partition by category order by Price) as rank_this
# from products1


# DENSE_RANK

# Write a SQL query to rank products by price within each category such that products with the same price have the same rank and there are no gaps in ranking sequence.

# select ProductID,  Price, category, 
# rank() over(partition by category order by Price) as normal_R,
# dense_rank() over(partition by category order by Price) as desne_R
# from products1


# CUME_DIST

# How would you formulate a SQL query to determine the cumulative distribution of employee salaries within the company to understand salary dispersion?

# select ProductID, Category, Price, 
# cume_dist() over(partition by Category order by Price) as CD 
# from products1


# PERCENT_RANK
# How would you use SQL to calculate the percent rank of products' prices within each category
# select ProductID, Category, Price, 
# PERCENT_RANK() over(partition by Category order by Price) as percent_R
# from products1

# NTILE
# select ProductID, Price, 
# NTILE(4) over(partition by Category order by Price) as nt 
# from products1
