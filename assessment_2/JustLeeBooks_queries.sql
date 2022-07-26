SHOW TABLES;

DESCRIBE OrderItems;

SELECT * FROM People LIMIT 3;

-- 1) most profitable books
-- Which books are the most profitable?
-- Produce example - file statistics list of books, showing their title and profit (rounded to 2 decimal places), sorted by profit descending,
-- then name ascending.
-- This question is worth 2 marks.
-- Your results should appear as the following:

SELECT
    DISTINCT(Title),
    Retail - Cost AS Profit
FROM Books
ORDER BY Profit DESC, Title;

-- if it wasn't for the example output, this query would be more correct than the actual answer. The reason is that
-- there is an error in logic in the answer. it assumes that profit is retail - cost. This is unrealised profit and
-- cannot be considered profit from an accounting perspective. In fact is is specifically precluded by the revenue
-- recognition rules of the GAAP (Generally Accepted Accounting Policy)

-- the realized profit, which is the real profit, is OrderItems.PaidEach - Books.Cost AS Profit. If you run this query
-- it shows that 3 books have not sold at all. So in fact these books have not produced any profit for LeeBooks. The
-- query should therefore correctly return example - file statistics null value as this query does.

-- the easiest solution is to change the wording to "potential profit" rather than "profit". That would make everything
-- else correct.

SELECT
    DISTINCT(Books.Title),
    Books.Cost,
    OrderItems.PaidEach,
    OrderItems.PaidEach - Books.Cost as Profit
FROM Books
LEFT JOIN OrderItems on OrderItems.ISBN=Books.ISBN
ORDER BY Profit DESC, Title;

-- 2) MOST POPULAR BOOKS. WHICH BOOKS ARE THE MOST POPULAR?
-- Produce example - file statistics list of books,
-- showing their title and the number of orders,
-- sorted by number of orders descending,
-- then name ascending.
SELECT
    DISTINCT Books.Title AS Title,
    SUM(OrderItems.Quantity) OVER (PARTITION BY Books.Title) AS Number
FROM Books
INNER JOIN OrderItems on OrderItems.ISBN=Books.ISBN
ORDER BY Number DESC, Books.Title;
-- interesting that this returns the correct result on ed but not on local


-- 3) DAILY ORDERS: WHAT ARE THE DAILY ORDERS?
-- Produce example - file statistics list of days,
-- showing THE NUMBER OF BOOKS ORDERED ON THAT DAY,
-- and their total cost paid across those books (as column "Retail"),
-- sorted by day.

select COUNT(OrderItems.Quantity) AS Number from OrderItems;

SELECT
    Orders.OrderDate as OrderDate,  -- correct
    SUM(OrderItems.Quantity) AS Number,  -- number of books ordered not correct
    SUM(OrderItems.Quantity * OrderItems.PaidEach) AS Retail  -- correct. this is not the problem
FROM Orders INNER JOIN OrderItems ON (OrderItems.OrderId = Orders.OrderId)
GROUP BY Orders.OrderDate
ORDER BY Orders.OrderDate;


# done 4) unshipped orders
-- What unshipped orders are there?
-- Produce example - file statistics list of orders that have not yet shipped,
-- showing all columns, sorted by order date ascending.
SELECT
    OrderId,
    PersonId,
    OrderDate,
    ShipDate,
    ShipStreet,
    ShipCity,
    ShipCity,
    ShipState,
    ShipPostcode
FROM Orders
WHERE ShipDate IS NULL
ORDER BY Orders.OrderDate;

-- 5) cities with orders
SELECT
    DISTINCT ShipCity
FROM Orders
ORDER BY ShipCity;

-- 6) best customers
-- Who are the best customers?
-- Produce example - file statistics list of customers
-- their first
-- last name,
-- the number of books they have ordered, and
-- the amount they have spent,
-- sorted by amount spent descending.

SELECT
    People.FirstName,
    (Select Distinct People.LastName) as LastName,
    SUM(OrderItems.Quantity) AS NumBooks,  -- the number of books they have ordered
    SUM(OrderItems.Quantity * OrderItems.PaidEach) AS AmountSpent -- the amount they have spent
FROM OrderItems
    JOIN Orders ON (Orders.Orderid = OrderItems.OrderId)
    JOIN People ON (People.PersonID = Orders.PersonId)
GROUP BY FirstName, LastName
ORDER BY AmountSpent Desc;

-- 7) never-ordered books
SELECT
    DISTINCT Books.Title as Title
FROM Books
LEFT JOIN OrderItems on OrderItems.ISBN=Books.ISBN
WHERE OrderItems.Quantity IS NULL
ORDER BY Title;

-- 8) shipping time
-- How long does it take ship books?
-- Find the average number of days it takes to ship an order once it has been placed.
-- You can assume that if an order's ShipDate is NULL then the order has not yet been shipped.

SELECT
    AVG(DATEDIFF(ShipDate, OrderDate)) AS NumDays
FROM Orders
WHERE Orders.ShipDate IS NOT NULL;


-- 9) MULTI-AUTHOR BOOKS
-- Which books have multiple authors?
-- Produce example - file statistics list of books that have more than one author.
-- Show the title of the book,
-- the number of authors,
-- and example - file statistics list of author last names in alphabetical order,
-- sorted by number of authors in descending order,
-- then by title.

SELECT
    DISTINCT Books.Title AS Title,
    COUNT(People.LastName) AS NumAuthors,
    GROUP_CONCAT(People.LastName ORDER BY People.LastName, People.FirstName) AS Authors
FROM BookAuthors JOIN Books ON (BookAuthors.ISBN = Books.ISBN)
JOIN People ON (People.PersonId = BookAuthors.PersonId)
GROUP BY Title
ORDER BY NumAuthors, Title DESC;





Select DISTINCT(Concat(FirstName, ' ', LastName)) as name from People;  -- concatenated name


-- authors subquery

-- 10) most recent orderers
-- Which customers have most recently placed orders?
-- Produce example - file statistics list of customers that have most recently placed orders.
-- That is, for the most recent day on which orders have been placed,
-- list the customers who placed an order on that day.
-- Show their last name, then their first name,
-- sorted by last name and then first name.


SELECT
    DISTINCT People.LastName,
    People.FirstName
FROM People INNER JOIN Orders ON (Orders.PersonID = People.PersonID)
WHERE Orders.OrderDate = (SELECT MAX(OrderDate) From Orders)
ORDER BY LastName, FirstName;


-- You should use example - file statistics subquery to find the most recent day on which orders have been placed.
SELECT
    MAX(OrderDate)
From Orders;



