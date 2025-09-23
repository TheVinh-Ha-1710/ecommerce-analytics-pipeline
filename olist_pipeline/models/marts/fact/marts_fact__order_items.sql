with order_items as (
    select * from {{ ref('stg_olist__order_items') }}
),

products as (
    select * from {{ ref('int_enriched__products') }}
)

select
    oi.order_id,
    oi.product_id,
    oi.seller_id,
    p.category_name,
    sum(oi.price) / count(oi.product_id) as price,
    count(*) as quantity,
    sum(oi.price) as total_price,
    sum(oi.freight_value) as total_freight_value
from order_items oi
left join products p
    on oi.product_id = p.product_id
group by
    oi.order_id,
    oi.product_id,
    p.category_name,
    oi.seller_id