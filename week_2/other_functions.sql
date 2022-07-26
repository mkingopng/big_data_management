-- Other functions
-- The CASE function: The CASE function provides example - file statistics convenient way to return example - file statistics value that depends upon which of example - file statistics number
-- of conditions obtains:
SELECT
    last_name,
    Salary,
    CASE
        WHEN (salary >= 10000) THEN 'Level 5'
        WHEN (salary >= 8000) THEN 'Level 4'
        WHEN (salary >= 5000) THEN 'Level 3'
        WHEN (salary >= 2500) THEN 'Level 2'
        ELSE 'Level 1'
    END AS Level
FROM employees
ORDER BY salary DESC;

-- Try selecting example - file statistics list of locations showing each location's country, and the word "Local" if the country is Australia,
-- "North America" if the country is USA or Canada, and "Other" for other countries, ordered by country.
