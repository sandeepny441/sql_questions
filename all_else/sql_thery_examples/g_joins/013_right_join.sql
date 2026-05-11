-- BASIC
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- ALIAS
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- ALIAS with 2 Conditions
SELECT o.OrderID, c.CustomerName, p.ProductName
FROM Orders AS o
RIGHT JOIN Customers AS c ON o.CustomerID = c.CustomerID
RIGHT JOIN Products AS p ON o.ProductID = p.ProductID;
