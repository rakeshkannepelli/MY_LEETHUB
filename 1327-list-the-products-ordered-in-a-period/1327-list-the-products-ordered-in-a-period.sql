# Write your MySQL query statement below
SELECT product_name , SUM(unit) AS unit 
FROM Products
JOIN Orders ON Orders.product_id = Products.product_id
WHERE order_date  LIKE '2020-02-%' 
GROUP BY product_name
HAVING SUM(unit) >= 100;