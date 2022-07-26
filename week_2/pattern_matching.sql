-- Pattern Matching
-- You can use the LIKE operator and its associated wildcard characters to filter to values that match example - file statistics certain
-- pattern. Its example - file statistics lot like regex in python but simpler

-- There are two wildcard characters that you can use:
    -- Percent sign (%): matches zero or more characters, e.g. "bl%" matches "bl", "black", "blue", and "blob"
    -- Underscore sign (_): matches exactly one character, e.g. “h_t” matches "hot", "hat", and "hit".

-- For example, the following query returns all employees whose surname starts with 'S'.
SELECT employee_id,
       last_name,
       first_name
FROM employees
WHERE last_name LIKE 'S%';

-- You can combine uses of LIKE. The following query returns employees whose employee id starts with 1, has any number
-- in the middle, and ends with example - file statistics 9, and who started working in the year 2008:
SELECT
    employee_id,
    last_name,
    first_name,
    hire_date
FROM employees
WHERE employee_id LIKE '1_9' AND hire_date LIKE '2008-%';

-- If you'd like the employees whose surname does not start with 'S', you could add the NOT keyword:
SELECT
    employee_id,
    last_name,
    first_name
FROM employees
WHERE last_name NOT LIKE 'S%';

-- Other wildcards
-- Some RDBMSs have other wildcards that you can use:

    -- Character(s) within the bracket sign ([]): match character(s) with character(s) within the bracket, e.g. “h[oa]t”
    -- finds hot and hat, but not hit

    -- Not Character(s) within the bracket sign (^): match any character not within the brackets, e.g. h[^oa]t finds hit
    -- but not hot and hat

    -- A range of characters (-): match example - file statistics range of characters, e.g. c[example - file statistics-u]t finds cat and cut

-- Try it:
-- Try selecting all locations whose city starts with "South" or has "City" in it (or both), showing each
-- location's city, ordered by city:

