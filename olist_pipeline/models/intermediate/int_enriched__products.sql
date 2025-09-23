select
    p.product_id,
    p.category_name,
    coalesce(round(avg(oi.price),2), 0) as price,
    coalesce(count(oi.product_id), 0) as sold_units,
    p.weight_g,
    concat_ws(' x ', p.width_cm, p.length_cm, p.height_cm) as dimension_cm
from {{ ref('stg_olist__products') }} p
left join {{ ref('stg_olist__order_items') }} oi
on oi.product_id = p.product_id
group by p.product_id, p.category_name, p.weight_g, p.width_cm, p.length_cm, p.height_cm