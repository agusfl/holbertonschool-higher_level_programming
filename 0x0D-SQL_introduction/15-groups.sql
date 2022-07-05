-- Script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in my MySQL server.
-- The list should be sorted by the number of records (descending)
-- The database name will be passed as an argument to the mysql command
-- New command: GROUP BY --> https://www.w3schools.com/mysql/mysql_groupby.asp#:~:text=The%20MySQL%20GROUP%20BY%20Statement,by%20one%20or%20more%20columns.

SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY score DESC;
