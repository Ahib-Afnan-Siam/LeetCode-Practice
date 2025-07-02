# Write your MySQL query statement below
WITH daily_totals AS (
    SELECT 
        visited_on, 
        SUM(amount) AS total_amount
    FROM Customer
    GROUP BY visited_on
),
windowed AS (
    SELECT 
        visited_on,
        SUM(total_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(
            SUM(total_amount) OVER (
                ORDER BY visited_on 
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ) / 7, 
            2
        ) AS average_amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
    FROM daily_totals
)
SELECT 
    visited_on,
    amount,
    average_amount
FROM windowed
WHERE rn >= 7
ORDER BY visited_on;