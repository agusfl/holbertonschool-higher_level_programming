-- Import in hbtn_0c_0 database this table dump (temperatures.sql)
-- To download the script "temperatures.sql" we can use the linux commands: "wget" or "curl".
-- Once we download the "temperatures.sql" file we can run the following command: mysql -u root -p hbtn_0c_0
-- and after runing that command and we are inside mysql we can run this command to import the file into
-- the "hbtn_0c_0" database: source temperatures.sql
-- Once we have done this steps, we can run: cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- Info how to import a file: https://www.youtube.com/watch?v=oSqKjvWs0GQ&ab_channel=Gestionatuweb-DanielS%C3%A1nchez
-- Info wget command: https://www.fastwebhost.in/blog/10-examples-of-linux-wget-command/#:~:text=Wget%20command%20is%20a%20Linux,will%20run%20in%20the%20background.
-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
