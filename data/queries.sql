SELECT * FROM customers;
SELECT * FROM customers ORDER BY companyname ASC;
SELECT * FROM customers ORDER BY companyname DESC;

-- Aggregate functions
SELECT * FROM products;

-- Select the most expensive product
SELECT MAX(UnitPrice) FROM products;
-- ALIAS (ændrer navnet fra UnitPrice til most_expensive_product
SELECT MAX(UnitPrice) AS most_expensive_product FROM products;

-- Select the most cheap product
SELECT MIN(UnitPrice) FROM products;
-- ALIAS
SELECT MIN(UnitPrice) AS least_expensive_product FROM products;

-- Select the average price from all products
SELECT AVG(UnitPrice) FROM products;
-- ALIAS
SELECT AVG(UnitPrice) AS average_product_price FROM products;

-- Give me the total number of products in the table
SELECT COUNT(*) FROM products;
-- ALIAS
SELECT COUNT(*) AS total_products FROM products;



-- Pagination
SELECT * FROM products LIMIT 0, 5;

-- Get 5 products, ordered by the cheapest to highest
SELECT * FROM products ORDER BY UnitPrice ASC LIMIT 0, 5;

-- LIKE with wildcard, every user which contactname starts with 'mar'
SELECT * FROM customers WHERE ContactName LIKE "mar%";
-- LIKE with wildcard, every user which contactname ends with 'r'
SELECT * FROM customers WHERE ContactName LIKE "%r";
-- LIKE with wildcard, I don't remember the whole name, so I search only for the few letters that I remember
SELECT * FROM customers WHERE ContactName LIKE "%wa%";

-- You have a tweet that Elon wrote + a message with the word Elon + users with Elon
-- FULL TEXT SEARCH

-- JOIN
SELECT * FROM customers;
SELECT * FROM orders;
-- JOIN with a limit of 2
SELECT * FROM orders JOIN customers ON orders.CustomerID = Customers.OrderID WHERE Customers.CustomerID="VINET" LIMIT 4,2;
-- Create a command that gives all the orders AND PRODUCTS from the user the customerID 'VINET'
