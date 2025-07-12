-- CURRENT_DATE
1. Use CURRENT_DATE to calculate how many days ago each employee was hired.
2. Find employees hired exactly one year before the current date.
3. List departments and count employees hired after the current date minus 3 years.

-- CURRENT_TIME
1. Retrieve the current time and concatenate it with the current date.
2. Use CURRENT_TIME to check if it's after noon (12:00:00).
3. Calculate the seconds since midnight using CURRENT_TIME.

-- DATE_ADD
1. Add 6 months to each employee's hire_date and list the new dates.
2. Find employees whose hire_date plus 2 years is before the current date.
3. Use DATE_ADD to project hire_date forward by 100 days.

-- DATE_SUB
1. Subtract 1 year from each hire_date and order by the result.
2. Find the difference after subtracting 30 days from the current date and compare to hire_dates.
3. Use DATE_SUB to find hire_dates within 3 months before a specific date like '2023-01-01'.

-- YEAR
1. Extract the year from each hire_date and group employees by hire year.
2. Find the number of employees hired in the year 2021.
3. List employees where the hire year is greater than 2020.

-- MONTH
1. Extract the month from hire_date and find hires in January.
2. Group employees by the month of their hire_date and count per month.
3. Find the average salary for employees hired in months 1 through 6.

-- DAY
1. Extract the day of the month from hire_date and list employees hired on the 15th.
2. Find hires where the day of hire_date is even.
3. Group by day of hire_date and count hires on each day.

-- HOUR
1. Assuming a datetime column, extract the hour from CURRENT_TIMESTAMP.
2. Use HOUR on CURRENT_TIME to determine if it's business hours (9-17).
3. Calculate total hours since a fixed time like '00:00:00'.

-- MINUTE
1. Extract minutes from CURRENT_TIME and see if it's on the hour (minute=0).
2. Use MINUTE on a time value to add minutes to a date.
3. Find if CURRENT_TIME minute is greater than 30.

-- SECOND
1. Extract seconds from CURRENT_TIME.
2. Use SECOND to check if seconds are even.
3. Add seconds to CURRENT_TIMESTAMP using DATE_ADD with INTERVAL.

-- DAYNAME
1. Find the day name of each hire_date and list employees hired on Mondays.
2. Group hires by DAYNAME(hire_date) and count per weekday.
3. Find if the current date is a Friday using DAYNAME(CURRENT_DATE).

-- MONTHNAME
1. Extract the month name from hire_date and find hires in March.
2. Group employees by MONTHNAME(hire_date) and calculate average salary.
3. List distinct month names of hire dates in the table.

-- DAYOFYEAR
1. Calculate DAYOFYEAR for each hire_date and find those in the first quarter (1-90).
2. Find the maximum DAYOFYEAR among hire_dates.
3. Compare DAYOFYEAR(CURRENT_DATE) to DAYOFYEAR(hire_date) for each employee.

-- DAYOFWEEK
1. Use DAYOFWEEK to find employees hired on weekends (1=Sunday, 7=Saturday).
2. Group by DAYOFWEEK(hire_date) and count hires per day of week.
3. Check if hire_date DAYOFWEEK is 2 (Monday).

-- WEEK
1. Extract the week number from hire_date and group by week.
2. Find hires in week 1 of any year.
3. Calculate the week difference between CURRENT_DATE and hire_date.

-- LAST_DAY
1. Find the last day of the month for each hire_date.
2. Use LAST_DAY(CURRENT_DATE) to get the end of the current month.
3. Find employees hired in the last week of their hire month by comparing to LAST_DAY.

-- DATEDIFF
1. Calculate DATEDIFF between CURRENT_DATE and hire_date to find days employed.
2. Find employees where DATEDIFF(hire_date, '2020-01-01') > 365.
3. Use DATEDIFF to order employees by tenure in years (divide by 365).