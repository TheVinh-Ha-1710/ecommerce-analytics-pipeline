with orders as (
    select customer_id, order_id, purchased_ts
    from {{ ref('stg_olist__orders') }}
),

first_order as (
    select
        customer_id,
        min(purchased_ts) as first_order_ts
    from orders
    group by customer_id
)

select
    customer_id,
    first_order_ts
from first_order 