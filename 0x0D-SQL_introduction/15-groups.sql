-- script that lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) as 'number'
FROM second_table
GROUP BY 1
ORDER BY 2 DESC;
