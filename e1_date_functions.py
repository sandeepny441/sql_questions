# How would you retrieve the current date from the database?
# select sysdate() 

# Using the ChipotleMenu table, can you list the items added to the menu in the month of March? Hint: Use a function to extract the month from the DateAdded column.
# select ItemName from chipotlemenu
# where extract(month from DateAdded) = 3

# For analysis purposes, you want to know the day of the week for each DateAdded in the ChipotleMenu table. Can you extract and display the day of the week for each item's DateAdded value?
# select DateAdded, DAYOFWEEK(DateAdded) from chipotlemenu 


# Can you calculate and display the difference in days between the current date and the DateAdded for each item in the ChipotleMenu table?
# select Datediff(NOW(), DateAdded) from 
# chipotlemenu


# Assuming a scenario where the ChipotleMenu table also has a DateDiscontinued column, how would you calculate the number of days each item was available on the menu (i.e., the difference between DateDiscontinued and DateAdded)?
# select abs(Datediff(date_disc, dateAdded))
# from chipotlemenu


# You want to run a promotion on items added to the menu on the last day of any month. How would you identify such items from the ChipotleMenu table using date functions?
# select itemName from chipotlemenu
# where DateAdded = last_day(DateAdded)
# last_day expects DATE as an argument, not a month


# For a future marketing campaign, you want to see which items will have their 1-year anniversary from the DateAdded in the next 30 days. How would you retrieve such items from the ChipotleMenu table?
# SELECT Itemname 
# FROM chipotlemenu
# WHERE DATEDIFF(CURDATE(), DateAdded) = 335;
