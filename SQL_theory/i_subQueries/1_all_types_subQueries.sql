-- Scalar subquer
SELECT ProductName, 
       (SELECT AVG(UnitPrice) FROM Products) AS AveragePrice
FROM Products

-- Column subquery 
SELECT ProductName
FROM Products
WHERE ProductID IN (SELECT ProductID 
                    FROM OrderDetails
                    WHERE Quantity > 100)

-- Row subquery
SELECT *
FROM Products
WHERE (ProductID, Name) = (SELECT ProductID, Name  
                           FROM NewProducts
                           WHERE ProductID = 10)

-- Table subquery
SELECT A.ProductID, A.ProductName, B.AveragePrice
FROM Products A,
     (SELECT ProductID, AVG(UnitPrice) AS AveragePrice
      FROM OrderDetails
      GROUP BY ProductID) B
WHERE A.ProductID = B.ProductID

-- EXISTS subquery
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName 
              FROM Products 
              WHERE Products.SupplierID = Suppliers.supplierID)
              
-- Correlated subquery
SELECT CustomerName,
       (SELECT COUNT(*) 
        FROM Orders
        WHERE Orders.CustomerID = Customers.CustomerID) AS OrderCount
FROM Customers
