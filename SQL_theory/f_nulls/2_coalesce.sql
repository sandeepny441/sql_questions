SELECT COALESCE(NULL, NULL, 5, NULL) -- Returns 5
SELECT COALESCE(10, NULL, NULL, 5, NULL) -- Returns 10


-- Replace NULLs with a default 'N/A' value.
SELECT 
  COALESCE(null_column, 'N/A') AS filled_column
FROM table

select customerName, salesRepEmployeeNumber from customers
where salesRepEmployeeNumber is NULL 

SELECT 
  COALESCE(salesRepEmployeeNumber, 1000000000) AS filled_column
FROM customers


-- Return first non-NULL choice from a set of options.
SELECT
  COALESCE(first_choice, second_choice, third_choice)
FROM table

-- Create a new column using first non-NULL value.
SELECT
  COALESCE(col1, col2, col3) AS calculated_column
FROM table


-- Concatenate first and last name handling NULLs.
SELECT 
  COALESCE(first_name, '') || ' ' || COALESCE(last_name, '') as full_name
FROM table

--MySQL
SELECT 
  CONCAT_WS(' ', COALESCE(first_name, ''), COALESCE(last_name, '')) as full_name
FROM table;


-- Use default if passed value is NULL.
INSERT INTO table (column) 
VALUES (COALESCE(@insert_this_if_this_is_not_null, insert_this_if_there_is_no_value))