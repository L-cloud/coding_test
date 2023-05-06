select A.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR
A join (SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE month(START_DATE) = "10") B on
A.CAR_ID = B.CAR_ID
where car_type = "세단"
group by A.car_id
order by 1 desc
