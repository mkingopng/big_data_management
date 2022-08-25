CREATE TABLE orders (
    OrderDate DATE,
    ISBN STRING,
    Title STRING,
    Category STRING,
    PriceEach DECIMAL(5,2),
    Quantity INT,
    FirstName STRING,
    LastName STRING,
    City STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'orders.csv' OVERWRITE INTO TABLE orders;

SELECT City, SUM(PriceEach * Quantity) as TotalAmount
FROM Orders
GROUP BY City;