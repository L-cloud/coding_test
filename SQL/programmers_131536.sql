SELECT T.USER_ID, T.PRODUCT_ID
FROM (SELECT USER_ID, PRODUCT_ID, COUNT(*) as CNT
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID) T
WHERE T.CNT > 1
ORDER BY 1,2 DESC

