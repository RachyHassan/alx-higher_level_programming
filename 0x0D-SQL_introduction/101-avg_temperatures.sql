-- A script that displays the average temperature (in Fahrenheit) by city ordered by descending temperature.
SELECT 'city', AVG('value') AS 'avg_temp'
FROM 'temperature'
GROUP BY 'city'
ORDER BY 'avg_temp' DESC;
