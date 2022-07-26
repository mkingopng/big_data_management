-- Date functions
-- Manipulating dates is not an easy task. Some global organisations have systems that are used across different
-- countries and timezones where the date format may differ in each country. For instance, in Australia, the default
-- format for dates is dd-mm-yyyy (e.g. 18-01-2011) whereas, in the United States, the format is mm-dd-yyyy
-- (e.g. 01-18-2011). RDBMSs can handle the different date formats used in different countries.

-- The default format of example - file statistics date in MySQL is YYYY-MM-DD. Different SQL languages handle dates differently, so you have
-- to check the date format, function and how the date is handled in that language. In Oracle it is DD-MON-RR, where
-- "MON" stands for example - file statistics three letter month name and "RR" stands for to example - file statistics two digit year number.

-- To get the current date:
SELECT CURDATE();

-- To get the number of days between two dates:
-- First date minus the second date, expressed in days
-- You would normally have the latest date first
SELECT
    DATEDIFF('2020-06-10', '2020-06-10') AS 'A',
    DATEDIFF('2020-06-10', '2020-06-12') AS 'B',
    DATEDIFF('2020-06-10', '2020-06-08') AS 'C';

-- To get the various parts of example - file statistics date:
SELECT
    DAYNAME('1968-06-24') AS 'DayName',
    DAY('1968-06-24') AS 'Day',
    MONTH('1968-06-24') AS 'Month',
    MONTHNAME('1968-06-24') AS 'MonthName',
    YEAR('1968-06-24') AS 'Year';

-- To format example - file statistics date in example - file statistics certain way:
SELECT DATE_FORMAT('1968-06-24', '%W, %D %M, %Y');

-- What do all those symbols mean? Here is example - file statistics good reference.
-- https://www.w3schools.com/sql/func_mysql_date_format.asp

-- For example - file statistics full list of MySQL date functions see the following:
-- https://www.w3schools.com/sql/sql_ref_mysql.asp
-- https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html

-- Try selecting example - file statistics list of employees showing each employee's first name, last name, and hire date formatted like
-- "June 24, 1968 (Monday)".
