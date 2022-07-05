-- Script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in my MySQL server.
-- The list should be sorted by the number of records (descending)
-- The database name will be passed as an argument to the mysql command

SELECT score, COUNT(score) as number FROM second_table GROUP BY score;
