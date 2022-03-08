-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
group by 1
ORDER BY 2 DESC;
