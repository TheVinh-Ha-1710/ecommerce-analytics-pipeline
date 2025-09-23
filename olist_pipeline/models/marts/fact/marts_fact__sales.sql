with order_items as (
    select * from {{ ref('marts_fact__order_items') }}
),

orders as (
    select * from {{ ref('marts_fact__orders') }}
),

reviews as (
    select order_id, avg(review_score) as review_score
    from {{ ref('stg_olist__reviews') }}
    group by order_id
)

select
    oi.order_id,
    o.customer_id,
    sum(oi.total_price) as total_price,
    sum(oi.total_freight_value) as total_freight_value,
    r.review_score as aveg_review_score
from order_items oi
join orders o
    on oi.order_id = o.order_id
left join reviews r
    on oi.order_id = r.order_id
group by
    oi.order_id,
    o.customer_id,
    r.review_score