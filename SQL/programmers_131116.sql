select a.category, a.price as max_price, product_name
from food_product a join (SELECT CATEGORY	, max(price) as price
from food_product
where CATEGORY	 = '과자' or CATEGORY	 = '국' or CATEGORY	 = '김치' or CATEGORY	 ='식용유'
group by category) as b  on
a.category = b.category and a.price = b.price
order by 2 desc
