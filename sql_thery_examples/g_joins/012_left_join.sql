-- BASIC LEFT
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- ALIAS and one CONDITION
SELECT o.OrderID, c.CustomerName
FROM Orders AS o
LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID;

-- ALIAS and TWO CONDITIONs
SELECT o.OrderID, c.CustomerName, p.ProductName
FROM Orders AS o
LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
LEFT JOIN Products AS p ON o.ProductID = p.ProductID;
