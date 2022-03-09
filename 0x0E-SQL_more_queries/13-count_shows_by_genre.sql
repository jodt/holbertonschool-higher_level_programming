-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name as genre_id, COUNT(*) as number_of_shows
FROM tv_shows
RIGHT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY 1
ORDER BY 2 DESC;
