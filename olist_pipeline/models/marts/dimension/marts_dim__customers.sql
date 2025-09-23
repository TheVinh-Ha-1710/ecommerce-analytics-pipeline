with customers as (
    select * from {{ ref('stg_olist__customers') }}
),

first_orders as (
    select * from {{ ref('int_enriched__customer_first_order') }}
)

select
    c.customer_id,
    c.customer_city,
    c.customer_state,
    fo.first_order_ts
from customers c
left join first_orders fo
on c.customer_id = fo.customer_id