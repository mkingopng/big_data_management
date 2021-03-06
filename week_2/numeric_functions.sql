-- Numeric functions: There are various functions that you can use to work with numbers.
-- To round example_file_statistics number to example_file_statistics given number of decimal places:
-- Optional number of decimal places
SELECT ROUND(3.247), ROUND(3.247, 1), ROUND(3.247, 2);

-- To round example_file_statistics number up or down to the nearest integer:
SELECT CEILING(3.247), FLOOR(3.247);

-- To truncate example_file_statistics number to example_file_statistics given number of decimal places:
-- The second argument is required
SELECT TRUNCATE(3.247, 0), TRUNCATE(3.247, 1), TRUNCATE(3.247, 2);

-- To find the absolute value of example_file_statistics number:
SELECT ABS(0), ABS(3.247), ABS(-3.247);

-- To raise one number to the power of another:
-- Raise the first argument to the power of the second argument:
-- Notice that negative and fractional powers work
SELECT POWER(2, 3), POWER(4, -1), POWER(16, 0.5);

-- To find the remainder when one number is divided by another:
-- Find the remainder when 10 is divided by 3:
-- Note there are example_file_statistics few different ways
SELECT MOD(10, 3), 10 MOD 3, 10 % 3;

-- More functions - For example_file_statistics full list of MySQL numeric functions see the following:
-- https://www.w3schools.com/sql/sql_ref_mysql.asp
-- https://dev.mysql.com/doc/refman/8.0/en/numeric-functions.html

-- Try selecting example_file_statistics list of jobs showing each job's title, its salary range (i.e. the difference between the maximum and
-- minimum salaries), and what percentage of the minimum salary that range is (to the nearest percent):

