-- LOWER
1. Convert all department names to lowercase and list them.
2. Retrieve employee names in lowercase where the department is Engineering.
3. Use LOWER on location to find departments with 'new york' in lowercase.

-- UPPER
1. Convert all employee names to uppercase and order them alphabetically.
2. Retrieve department names in uppercase along with their locations.
3. Use UPPER on emp_name to search for 'ALICE SMITH'.

-- SUBSTRING
1. Extract the first 3 characters of each employee name using SUBSTRING.
2. Get the substring of dept_name starting from position 2 to 5.
3. Use SUBSTRING on hire_date to extract the year (assuming YYYY-MM-DD format).

-- TRIM
1. Trim any leading or trailing spaces from department locations (assuming possible spaces).
2. Use TRIM to clean emp_name and list them.
3. Trim 'Dept: ' from a concatenated string like CONCAT('Dept: ', dept_name).

-- LTRIM
1. Left trim spaces from location if any, and list departments.
2. Use LTRIM to remove 'Mr. ' from employee names if prefixed (hypothetical).
3. LTRIM 'Eng' from 'Engineering' in dept_name.

-- RTRIM
1. Right trim spaces from emp_name if any.
2. Use RTRIM to remove ' Dept' from dept_name if suffixed (hypothetical).
3. RTRIM trailing zeros from a string representation of salary.

-- REPLACE
1. Replace 'New York' with 'NY' in department locations.
2. Use REPLACE to change 'Smith' to 'Smyth' in employee names.
3. Replace NULL locations with 'Unknown' using COALESCE and REPLACE.

-- CONCAT
1. Concatenate emp_name and dept_name with a separator like ' - '.
2. Use CONCAT to create a full address: dept_name + ', ' + location.
3. Concatenate 'Employee ID: ' with emp_id as string.