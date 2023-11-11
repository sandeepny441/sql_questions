ALTER TABLE table_name
DROP COLUMN column_name


DELETE FROM table_name


DELETE FROM employees
WHERE id = 101


DELETE target_table 
FROM target_table
INNER JOIN source_table 
ON target_table.id = source_table.id
WHERE condition


DELETE FROM table_name
WHERE id IN (SELECT id FROM table_name WHERE condition)


DELETE FROM table_name 
OUTPUT DELETED.*
WHERE condition

TRUNCATE TABLE table_name

DROP TABLE table_name

