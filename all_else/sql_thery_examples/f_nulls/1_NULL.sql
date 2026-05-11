SELECT NULL + 1 -- Returns NULL

SELECT column FROM table WHERE column IS NULL
SELECT salesRepEmployeeNumber FROM customers WHERE salesRepEmployeeNumber IS NULL


INSERT INTO table (column) VALUES (DEFAULT)
INSERT INTO customers (customerName)  VALUES (DEFAULT)
