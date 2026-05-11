select Destination from Trips 

Select TripName, Price from Trips 
where DurationDays > 5; 

Select Destination,DurationDays from Trips 
where Price <1000

Select TripName,DurationDays from Trips 
where TripName  LIKE '%Tour%' 

Select TripName, DurationDays from Trips 
where Destination  IN ('Rome' , 'Maldives')

Select * from Trips

Select * from Trips 
where DurationDays = 7

Select * from Trips 
where TripName LIKE  '%Beach%'

Select * from Trips 
where Price > 1500  

Select * from Trips 
ORDER BY Price
LIMIT 1


SELECT COUNT(*) AS TotalTrips
FROM Trips

SELECT COUNT(*) AS TotalTrips
FROM Trips
where DurationDays > 5

SELECT COUNT(*) AS TotalTrips
FROM Trips
where Destination = 'Maldives'

SELECT COUNT(*) AS TotalTrips
FROM Trips
where Price < 1000; 

SELECT COUNT(*) AS TotalTrips
FROM Trips
where TripName LIKE '%Adventure%'

Select Distinct Destination
from Trips

Select Distinct DurationDays
from Trips

Select Distinct Price
from Trips 

Select Distinct DurationDays,Destination
from Trips 

Select * from Trips 
where Price BETWEEN 500 and 1500 

Select * from Trips 
where Destination ='Maldives' and DurationDays = 5

Select TripName,Price from Trips 
where Price > 1000 and DurationDays  < 7

Select * from Trips 
where Price < 1300 and TripName  Like '%Beach%'  

Select * from Trips 
where Destination = 'New York' and DurationDays = 3  

Select * from Trips 
where Price < 600 or Price > 1800   

SELECT *
FROM Trips
WHERE Destination IN ('Amazon', 'Sahara');

SELECT TripName, Destination
FROM Trips
WHERE DurationDays IN (3, 8);

SELECT *
FROM Trips
WHERE TripName LIKE '%Adventure%' OR Price > 1900.00;

SELECT *
FROM Trips
WHERE Destination IN ('Himalayas', 'Caribbean') OR DurationDays > 9;

SELECT MIN(Price) AS MinPrice
FROM Trips;

SELECT MAX(Price) AS MaxPrice
FROM Trips;

SELECT AVG(Price) AS AvgPrice
FROM Trips;

SELECT COUNT(Price) AS PriceCount
FROM Trips;

SELECT SUM(Price) AS TotalPrice
FROM Trips;
Select TripName,Price from Trips 
where Price  > 1000
Order by Price Desc

Select Destination, DurationDays from Trips 
where DurationDays  >= 5
Order by DurationDays 

SELECT TripName, Destination
FROM Trips
WHERE TripName LIKE '%Tour%'
ORDER BY Destination;

SELECT TripName, Price, DurationDays
FROM Trips
WHERE Destination IN ('Maldives', 'New York')
ORDER BY DurationDays DESC;

SELECT *
FROM Trips
WHERE Price BETWEEN 500.00 AND 1500.00
ORDER BY Price ASC, TripName DESC;

SELECT Destination, COUNT(*) AS TripCount
FROM Trips
GROUP BY Destination;

SELECT DurationDays,AVG(Price) As AveragePrice
FROM Trips
GROUP BY DurationDays;

SELECT Destination, MAX(Price) AS HighestPrice
FROM Trips
GROUP BY Destination;

SELECT Destination, COUNT(*) AS TripCount
FROM Trips
GROUP BY Destination
Having  Count(*) > 2 

SELECT DurationDays , AVG(Price) AS TripAVG
FROM Trips
GROUP BY DurationDays
Having  AVG(Price) > 1000 

SELECT Destination, MIN(Price) AS MinPrice
FROM Trips
GROUP BY Destination
HAVING MIN(Price) > 500.00;

Select Destination, Count(*) as TripCount from Trips 
where DurationDays >=5
Group By Destination
Having Count(*) >= 1  

SELECT Destination, AVG(Price) AS AveragePrice
FROM Trips
WHERE TripName LIKE '%Beach%'
GROUP BY Destination
HAVING AVG(Price) < 500.00;

SELECT Destination, MIN(DurationDays) AS MinDuration
FROM Trips
WHERE Price > 700.00
GROUP BY Destination
HAVING MIN(DurationDays) >= 4;

SELECT
  TripName,
  CASE
    WHEN Price < 500.00 THEN 'Low'
    WHEN Price BETWEEN 500.00 AND 1500.00 THEN 'Medium'
    ELSE 'High'
  END AS PriceRange
FROM Trips;

SELECT
  TripName,
  CASE
    WHEN DurationDays = 2 OR DurationDays = 3 THEN 'Weekend'
    WHEN DurationDays = 7 THEN 'Weeklong'
    ELSE 'Variable'
  END AS DurationType
FROM Trips;

SELECT
  Destination,
  CASE
    WHEN Destination IN ('Maldives', 'Caribbean') THEN 'Tropical'
    ELSE 'Other'
  END AS Category
FROM Trips;

SELECT
  TripName,
  CASE
    WHEN TripName LIKE '%Tour%' THEN 'Tour Package'
    WHEN TripName LIKE '%Adventure%' THEN 'Adventure Package'
    ELSE 'Standard Package'
  END AS PackageType
FROM Trips;

SELECT ItemName
FROM YourTableName
WHERE Price > 7.00 AND Price < 8.00;

SELECT ItemName
FROM YourTableName
WHERE Category = 'Bowl' AND Calories < 600;

SELECT *
FROM YourTableName
WHERE Category = 'Burrito' AND Price < 8.00 AND Calories > 600;

SELECT *
FROM YourTableName
WHERE Category = 'Sides' AND Price < 4.00 AND Calories > 700;

SELECT *
FROM YourTableName
WHERE Category = 'Tacos' OR Price > 9.00;

SELECT ItemName
FROM YourTableName
WHERE Calories < 550 OR Calories > 750;

SELECT *
FROM YourTableName
WHERE Category = 'Salad' OR Category = 'Quesadilla';

SELECT *
FROM YourTableName
WHERE ItemName = 'Chicken Burrito' OR Price = 7.80;

SELECT *
FROM YourTableName
WHERE Category <> 'Bowl';

SELECT ItemName
FROM YourTableName
WHERE Price <> 8.00;

SELECT *
FROM YourTableName
WHERE ItemName <> 'Chips & Guacamole';

SELECT *
FROM YourTableName
WHERE Calories < 600 OR Calories > 700;


SELECT *
FROM YourTableName
WHERE Price = 7.50;

SELECT *
FROM YourTableName
WHERE Calories > 650;

SELECT *
FROM YourTableName
WHERE Price <= 7.80;


SELECT *
FROM YourTableName
WHERE Calories < 500;

SELECT *
FROM YourTableName
WHERE Category IN ('Burrito', 'Salad', 'Sides');

SELECT *
FROM YourTableName
WHERE Price IN (7.50, 8.00, 9.00);


SELECT *
FROM YourTableName
WHERE ItemName IN ('Chicken Burrito', 'Steak Tacos', 'Veggie Bowl');

SELECT *
FROM YourTableName
WHERE Calories IN (645, 570, 520);

SELECT *
FROM YourTableName
WHERE Price BETWEEN 7.00 AND 8.00;

SELECT *
FROM YourTableName
WHERE Calories BETWEEN 500 AND 600;

SELECT *
FROM YourTableName
WHERE ItemID BETWEEN 2 AND 5;

SELECT *
FROM YourTableName
WHERE Price BETWEEN 3.00 AND 9.00;

SELECT *
FROM YourTableName
WHERE Price > (SELECT AVG(Price) FROM YourTableName);

SELECT *
FROM YourTableName
WHERE Category = 'Salad' AND Calories > 500;

SELECT *
FROM YourTableName
WHERE Category = 'Bowl' AND Price > (SELECT Price FROM YourTableName WHERE ItemName = 'Chicken Burrito');

SELECT *
FROM YourTableName
WHERE ItemName LIKE '%Veggie%';

SELECT *
FROM YourTableName
WHERE ItemName LIKE 'Chicken%';

SELECT *
FROM YourTableName
WHERE ItemName LIKE '%Bowl';

SELECT *
FROM YourTableName
WHERE ItemName LIKE '%Tacos%';

SELECT *
FROM YourTableName
WHERE ItemName LIKE '_ritos%';





