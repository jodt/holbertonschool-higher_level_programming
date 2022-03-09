-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id = 8
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY 1
ORDER BY 1;
