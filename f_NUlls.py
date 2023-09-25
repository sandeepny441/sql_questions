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