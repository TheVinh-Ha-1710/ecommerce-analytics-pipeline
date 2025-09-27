with orders as (
    select
        order_id,
        customer_id,
        purchase_ts as order_date,
        order_status
    from {{ ref('stg_order') }}
),

order_items as (
    select
        order_id,
        round(sum(price),2) as total_item_value,
        round(sum(freight_value),2) as total_freight_value,
        count(*) as num_items
    from {{ ref('stg_order_item') }}
    group by order_id
),

payments as (
    select
        order_id,
        round(sum(payment_value),2) as total_payment_value
    from {{ ref('stg_payment') }}
    group by order_id
),

reviews as (
    select
        order_id,
        avg_score as avg_review_score
    from {{ ref('fact_review') }}
)

select
    o.order_id,
    o.customer_id,
    o.order_date,
    oi.num_items,
    p.total_payment_value as revenue,
    oi.total_freight_value as freight,
    r.avg_review_score
from orders o
left join order_items oi on o.order_id = oi.order_id
left join payments p on o.order_id = p.order_id
left join reviews r on o.order_id = r.order_id