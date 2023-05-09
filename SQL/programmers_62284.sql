select a.cart_id
from cart_products a left outer join (
select id,cart_id from cart_products
    where name = 'Yogurt'
) b
on a.cart_id = b.cart_id
where b.id is not null and a.name = 'Milk'
group by a.cart_id
order by 1
