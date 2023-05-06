select A.car_id AS CAR_ID, CASE WHEN max(A.b) = 1 THEN '대여중' ELSE '대여 가능' END as AVAILABILITY
from (
    select CAR_ID, CASE WHEN START_DATE <= '2022-10-16' AND '2022-10-16' <= END_DATE Then 1 else 0 END as b
    from car_rental_company_rental_history
    group by car_id, b
) AS A
group by A.car_id
ORDER BY 1 DESC
