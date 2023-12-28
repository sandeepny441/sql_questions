# How many items in the ChipotleMenu table have a NULL value in the Category column?

# select count(*) from chipotleMenu where  
# category = NULL

# Retrieve all item names that have a NULL value for Price
# select names from chipoodooMenu where ItemName = NULL

# Which items were added to the menu (DateAdded) but don't have ProteinGrams specified (NULL)?
# SELECT ItemName 
# FROM ChipotleMenu 
# WHERE ProteinGrams IS NULL AND DateAdded IS NOT NULL;

# Find out the average Calories of items where FatGrams is not NULL.
# select avg(Calories) from chipoodooMenu where
# FatGrams is NOT NULL 



# How many items have neither ProteinGrams nor FatGrams specified?
# select * from chipotlemenu
# where ProteinGrams is NULL 
# AND 
# FatGrams is NULL


# Which items have a Price specified but have NULL values in both the Calories and DateAdded columns?
# SELECT * FROM chipotlemenu
# WHERE Price IS NOT NULL
# AND Calories IS NULL
# AND DateAdded IS NULL;


# List all the categories that have at least one item with a NULL DateAdded.
# select ItemName from chipotlemenu
# where DateAdded is NULL


# Find the total count of items that have any of the nutritional facts (Calories, ProteinGrams, or FatGrams) as NULL.

# select count(*) from chipotlemenu
# Where 
# Calories is NULL 
# OR 
# ProteinGrams is NULL 
# or 
# FatGrams is NULL


# Which Category has the most number of items with NULL FatGrams?
# select ItemName, count(*) as null_count
# from chipotlemenu
# where FatGrams is  NULL
# group by ItemName
# order by null_count desc 
# limit 1


# Retrieve the names of items that have a specified Price but have either ProteinGrams or FatGrams (or both) as NULL.

select Itemname from chipotleMenu
where Price > 0
and (ProteinGrams is NULL 
OR FatGrams is NULL)

select Itemname from chipotleMenu
where Price > 0
AND FatGrams is NOT NULL


