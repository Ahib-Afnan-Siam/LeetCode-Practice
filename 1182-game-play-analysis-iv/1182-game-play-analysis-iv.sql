# Write your MySQL query statement below
WITH first_logins AS (
    SELECT 
        player_id, 
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT 
    ROUND(AVG(CASE 
                WHEN a.event_date IS NOT NULL THEN 1 
                ELSE 0 
             END), 2) AS fraction
FROM first_logins f
LEFT JOIN Activity a 
    ON f.player_id = a.player_id 
    AND a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);