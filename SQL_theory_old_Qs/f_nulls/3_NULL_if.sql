SELECT NULLIF(10, 10); -- Returns NULL because 10 is equal to 10


SELECT NULLIF(status, 'ACTIVE') FROM accounts; -- Returns NULL for all rows where status is 'ACTIVE'
SELECT NULLIF(salesRepEmployeeNumber, 4) FROM customers


SELECT dividend / NULLIF(denominator,0) FROM calculations; 
-- Returns NULL instead of failing on divide by zero errors

select Price, Calories, Price/ NULLIF(Calories, 570)
from chipotlemenu

select Price, Calories, Price/ Calories
from chipotlemenu
SELECT creditLimit / NULLIF(creditLimit,0) FROM customers;

SELECT NULLIF(TRIM(col),'') FROM data; -- Returns NULL for all rows where col is blank (after trimming)
 
 SELECT NULLIF(revenue, 0) FROM sales; -- Returns NULL for all rows where revenue is 0
SELECT NULLIF(creditLimit, 0) from customers

-- END OF NULLS :) 
