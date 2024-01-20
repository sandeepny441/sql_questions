-- Length
SELECT LENGTH(column);

-- Lowercase
SELECT LOWER(column);

-- Uppercase   
SELECT UPPER(column);

-- Substring
SELECT SUBSTRING(column, start, length); 

-- Trim  
SELECT TRIM(column);

-- Left Trim
SELECT LTRIM(column);

-- Right Trim   
SELECT RTRIM(column);

-- Replace  
SELECT REPLACE(column, 'old', 'new');

-- Concatenate
SELECT CONCAT(column1, column2);

-- Reverse
SELECT REVERSE(column);  

-- Duplicate
SELECT REPEAT(column, n);

-- Split string
SELECT SUBSTRING_INDEX(column, delimiter, n);



-- select upper('apple') --APPLE
-- select lower('APPLE') --apple
-- select SUBSTRING('Apple', 3) --ple
-- select SUBSTRING('ORANGE', 2, 4) --RANG
-- select length('SPACE') --3 
-- select concat('APPLE', '-- ORANGE') -- APPLE-- ORANGE
-- SELECT LTRIM('  hello') --hello
-- SELECT LTRIM('hello        ') --hello
-- select trim('   HELLO    ') --HELLO
-- select replace('HELLO', 'HE', 'SHE') --SHELLO
-- select reverse('APPLE') -- ELPPA
-- select CHAR_LENGTH('APPLE') --5 
-- select locate('d', 'APPLE world') --11
 