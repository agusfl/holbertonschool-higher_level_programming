-- Script that lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server.
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order) --> see example in the intranet.
-- Records should be listed by descending score
-- The database name will be passed as an argument to the mysql command
-- Info about IS NOT NULL: https://chartio.com/resources/tutorials/how-to-select-records-with-no-null-values-in-mysql/

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
