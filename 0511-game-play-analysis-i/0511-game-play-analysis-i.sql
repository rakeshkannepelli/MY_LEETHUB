# Write your MySQL query statement below
SELECT player_id , MIN(event_date) AS first_login 
FROM ACtivity
GROUP BY player_id;