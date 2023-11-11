# ---AND-----

# Which items have a price greater than $7.00 AND less than 8.00?
# select itemname from chipotlemenu
# where Price >7 and Price < 8

# Can you list the ItemNames that belong to the 'Bowl' category AND have calories less than 600?
# select itemname from chipotlemenu
# where Category = 'Bowl'
# and Calories < 600 

Which items from the 'Burrito' category have a price less than $8.00 AND calories more than 600?

Which 'Sides' items cost less than $4.00 AND have more than 700 calories?


---OR-----

# Which items are either from the 'Tacos' category OR priced above $9.00?
# Can you retrieve ItemNames that have either less than 550 calories OR more than 750 calories?
# select itemname from chipotlemenu
# where Calories < 550 or Calories > 750

Which items belong to either the 'Salad' category OR the 'Quesadilla' category?
List the items that are either 'Chicken Burrito' OR have a price of $7.80.
--NOT---

# Which items are NOT in the 'Bowl' category?
# select itemname from chipotlemenu
# where Category NOT in ('Bowl')
List the ItemNames that do NOT have a price of $8.00.
Can you retrieve items that are NOT 'Chips & Guacamole'?
Which items do NOT have calories between 600 and 700?


--COMPARISON---

Which items have a price equal to $7.50?
List the items that have calories greater than 650.
Can you find items with a price less than or equal to $7.80?
Which items from the menu have calories less than 500?
--IN------

Which items belong to either the 'Burrito', 'Salad', or 'Sides' category?
List the items that have prices IN $7.50, $8.00, and $9.00.
Which ItemNames are either 'Chicken Burrito', 'Steak Tacos', or 'Veggie Bowl'?
Can you retrieve items that have calories either 645, 570, or 520?
---BETWEEN----

# Which items have a price BETWEEN $7.00 and $8.00?
# select itemname from chipotlemenu
# where price BETWEEN 7 and 8
List the items with calories BETWEEN 500 and 600.
Can you find items with ItemID BETWEEN 2 and 5?
Which items have a price BETWEEN $3.00 and $9.00?

---EXISTS---
(For EXISTS, we typically need sub-queries or another table for context.
I'll frame a hypothetical question based on the given table.)

Are there items on the menu where the price is greater than the average price of all items?
Does a 'Salad' category item exist with calories above 500?
Is there a 'Bowl' item that costs more than the 'Chicken Burrito'?
Do any items exist with a name containing the word 'Veggie'?


--LIKE --WILDCARD--

Which items on the menu have names that start with 'Chicken'?
select itemname from chipotlemenu where name
like 'Chicken%'
Can you list the items that end with 'Bowl'?
select itemname from chipotlemenu where name
like '%Chicken'
Find items that have the word 'Tacos' anywhere in their name.
select itemname from chipotlemenu where name
like '%Tacos%'
Which items have a name pattern where there's any character followed by the word 'ritos'?
select itemname from chipotlemenu where name
like '_riots'