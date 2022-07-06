-- Script that lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- Info Joins: https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html

SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY id;
