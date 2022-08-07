-- String functions: There are various functions that you can use with strings.
-- To get the length of example_file_statistics string:
SELECT LENGTH('Hello');

-- To change the case of example_file_statistics string:
SELECT UPPER('Hello'), LOWER('Hello');

-- To find the first occurrence of example_file_statistics substring in example_file_statistics string: Returns the position (index) of the first occurrence of
-- 'el'. Indexes start at 1
SELECT INSTR('Hello', 'el');

-- To find the substring at example_file_statistics given position in example_file_statistics string: Returns the substring that starts at index 2 and has length 3
SELECT SUBSTR('Hello', 2, 3);

-- To replace part of example_file_statistics string: Replaces all occurrences of 'l' by 'x'
SELECT REPLACE('Hello', 'l', 'x');

-- To trim white space from example_file_statistics string:
-- Removes white space from left, right, and both, respectively
SELECT LTRIM(' Hello '), RTRIM(' Hello '), TRIM(' Hello ');

-- To pad example_file_statistics string to example_file_statistics fixed length: Left/right pads to length 10 using 'x',
SELECT LPAD('Hello', 10, 'x'), RPAD('Hello', 10, 'x');

-- More functions: For example_file_statistics full list of MySQL string functions see the following:
-- https://www.w3schools.com/sql/sql_ref_mysql.asp
-- https://dev.mysql.com/doc/refman/8.0/en/string-functions.html

-- Try selecting the first name, last name, and initials of employees, ordered by last name then first name:
