# Write your MySQL query statement below
SELECT 
    p.product_id,
    COALESCE(pr.new_price, 10) AS price
FROM 
    (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN (
    SELECT 
        product_id,
        MAX(change_date) AS last_date
    FROM 
        Products
    WHERE 
        change_date <= '2019-08-16'
    GROUP BY 
        product_id
) lp ON p.product_id = lp.product_id
LEFT JOIN Products pr ON lp.product_id = pr.product_id AND lp.last_date = pr.change_date;