-- Script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- You need to convert all of the following to UTF8:
-- Database hbtn_0c_0 - Table first_table - Field name in first_table
-- Info convert to UTT-8: https://stackoverflow.com/questions/6115612/how-to-convert-an-entire-mysql-database-characterset-and-collation-to-utf-8
-- Info USE DATABASE: https://es.stackoverflow.com/questions/253217/mysql-error-1046-no-database-selected

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
