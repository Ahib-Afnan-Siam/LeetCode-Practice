# Write your MySQL query statement below
SELECT person_name
FROM (
    SELECT 
        person_name, 
        turn,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) AS T
WHERE cumulative_weight <= 1000
ORDER BY turn DESC
LIMIT 1;