-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on my server (in localhost).
-- Info command SHOW GRANTS: https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql

SHOW GRANTS FOR user_0d_1@localhost;
SHOW GRANTS FOR user_0d_2@localhost;
