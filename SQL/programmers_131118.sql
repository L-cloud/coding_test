SELECT A.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
FROM REST_INFO
A JOIN (SELECT REST_ID, ROUND(SUM(REVIEW_SCORE)  / COUNT(REST_ID), 2) AS SCORE
FROM REST_REVIEW
       group by REST_ID) B ON A.REST_ID = B.REST_ID
WHERE ADDRESS LIKE "서울%"
ORDER BY SCORE DESC , FAVORITES DESC