SELECT 
CASE 
    WHEN AGE < 30 THEN 'young'
    WHEN AGE > 30 AND AGE < 50 THEM 'MIDDLE AGED'
    ELSE 'OLD'
END AS AGE_CATEGORY, 
AVG(AGE)
FROM PEOPLE
GROUP BY AGE_CATEGORY

-- CASE is useful when we have more than 1 condition

SELECT NAME, IF(IF AGE < 30, 'young', 'OLD') AS AGE_CATEGORY FROM PEOPLE

--if is useful when we have only ONE condition to check 