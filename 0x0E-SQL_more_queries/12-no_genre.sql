-- Script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- Info IS NULL: https://www.tutorialspoint.com/how-do-i-check-if-a-column-is-empty-or-null-in-mysql#:~:text=SELECT%20*%20FROM%20yourTableName%20WHERE%20yourSpecificColumnName,when%20there%20is%20empty%20value.
-- Esta task es muy similar a la task 10 pero usamos un LEFT JOIN para sacar todos los datos de "tv_shows" y
-- "filtramos" con el WHERE por los "genre_id" que sean NULL usando IS NULL.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
