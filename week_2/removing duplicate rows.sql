-- removing duplicate rows

-- By default example - file statistics SELECT statement will return all matching rows, even if some are duplicates of others. For example, the
-- following statement returns all job_ids, even though some are duplicates of others:
SELECT
    job_id
FROM employees;

-- use the keyword DISTINCT to remove duplicates
SELECT DISTINCT
    job_id
FROM employees;

-- If you use the DISTINCT keyword when selecting multiple columns, the results will include the unique combinations
-- of those columns:
SELECT DISTINCT
    department_id,
    manager_id
FROM employees;

-- Try selecting the distinct combinations of minimum and maximum salaries from the jobs table:
SELECT DISTINCT
    min_salary,
    max_salary
FROM jobs;
