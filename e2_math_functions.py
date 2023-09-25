# Average Price: What is the average price of all items on the menu?
# select avg(Price) from chipotlemenu

# Highest Calorie Count: Which item has the highest calorie count?
# select  ItemName, max(Calories)
# from chipotlemenu
# group by ItemName
# LIMIT 1


# Minimum Protein Content: Which item has the least amount of protein?
# select  ItemName, min(ProteinGrams)
# from chipotlemenu
# group by ItemName
# LIMIT 1

# Total Calories of Burritos: What's the total calorie count for all types of burritos on the menu?
# --NOT so better than WHERE 
# select category, sum(calories)
# from chipotlemenu
# group by Category
# having Category = "Burrito"

# --Better 
# select category, sum(calories)
# from chipotlemenu
# where Category = "Burrito"
# group by Category

# Absolute Value:
# What's the absolute difference in price between the 'Chicken Burrito' and the 'Veggie Bowl'?
# SELECT ABS(c1.Price - c2.Price) AS price_difference
# FROM ChipotleMenu c1
# JOIN ChipotleMenu c2 
# ON 
# c1.ItemName = 'Chicken Burrito'  
# AND 
# c2.ItemName = 'Veggie Bowl';


# Power:
# If you were to raise the price of the 'Steak Tacos' to the power of 2, what value would you get?
# select POWER(Price, 2) FROM chipotlemenu
# WHERE ItemName = 'Steak Tacos'

# Square Root:
# What's the square root of the calories for the 'Chips & Guacamole'?
# select sqrt(calories) from chipotlemenu
# where itemname = 'Chips & Guacamole'


# Ceiling:
# What's the ceiling value of the price for 'Barbacoa Salad'?

# select ceiling(Price) from chipotlemenu
# where ItemName = "Barbacoa Salad"


# Floor:
# What's the floor value of the calories of 'Carnitas Quesadilla'?
# select floor(Calories) from chipotlemenu
# where ItemName = "Carnitas Quesadilla"


# Round:
# Round the price of the 'Sofritas Burrito Bowl' to the nearest whole number.

# select round(Price) from chipotlemenu
# where ItemName = "Sofritas Burrito Bowl"


# Round to Decimals:
# Round the price of 'Chicken Burrito' to 2 decimal places.
# select round(Price, 2) from chipotlemenu
# where ItemName = "Chicken Burrito"

# Modulo:
# If you divide the calories of 'Chicken Burrito' by the calories of 'Veggie Bowl', what's the remainder?

# select c1.calories % c2.calories 
# from chipotlemenu c1 join chipotlemenu c2 
# where c1.ItemName = "Chicken Burrito"
# AND 
# c2.ItemName = "Veggie Bowl"


# Random:
# Generate a random number between 0 and 1 and multiply it by the price of 'Chicken Burrito'. What's the resulting value?

# select RAND() * Price
# from chipotlemenu
# where ItemName = 'Chicken Burrito'

# Trig Functions:
# What's the sine value of the price of 'Chicken Burrito' when treated as an angle in radians?

# select sin(Price) from chipotlemenu
# where ItemName = 'Chicken Burrito'




