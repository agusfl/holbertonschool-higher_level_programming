-- Script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in my MySQL server.
-- The database name will be passed as an argument of the mysql command
-- Info DELETE command: https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php

DELETE FROM second_table
WHERE score <= 5;
