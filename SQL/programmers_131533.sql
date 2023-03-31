SELECT PRODUCT_CODE, PRICE * SUM(A) AS SALES
FROM PRODUCT AS P
JOIN (SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS A FROM OFFLINE_SALE GROUP BY PRODUCT_ID ) AS O  ON P.PRODUCT_ID = O.PRODUCT_ID 
GROUP BY PRODUCT_CODE
ORDER BY 2 DESC, 1 
