-- Script that lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server.
-- Results should display both the score and the name (in this order) --> see example in the intranet.
-- Records should be ordered by score (top first).
-- The database name will be passed as an argument of the mysql command
-- Use of "ORDER BY" in desdescending order by "score" column
-- Info of commands used: https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php

SELECT score, name FROM second_table ORDER BY score DESC;
