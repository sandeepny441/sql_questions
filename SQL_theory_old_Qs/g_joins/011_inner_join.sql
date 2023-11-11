-- BASIC
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers 
ON Orders.CustomerID = Customers.CustomerID;

-- ALIAS
SELECT o.OrderID, c.CustomerName
FROM Orders AS o
INNER JOIN Customers AS c 
ON o.CustomerID = c.CustomerID;

-- with Condition
SELECT o.OrderID, c.CustomerName, p.ProductName
FROM Orders AS o
INNER JOIN Customers AS c 
    ON o.CustomerID = c.CustomerID
INNER JOIN Products AS p 
    ON o.ProductID = p.ProductID;

-----------------------------------------------------------------------------------
-- Using COMMA
-----------------------------------------------------------------------------------

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders, Customers
WHERE Orders.CustomerID = Customers.CustomerID;


SELECT Orders.OrderID, Customers.CustomerName
FROM Orders, Customers
WHERE Orders.CustomerID = Customers.CustomerID;


SELECT o.OrderID, c.CustomerName, p.ProductName
FROM Orders o, Customers c, Products p
WHERE o.CustomerID = c.CustomerID 
AND o.ProductID = p.ProductID;

