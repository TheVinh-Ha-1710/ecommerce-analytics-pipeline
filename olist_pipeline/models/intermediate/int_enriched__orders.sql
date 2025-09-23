with orders as (
    select * from {{ ref('stg_olist__orders') }}
),

payments as (
    select
        order_id,
        sum(payment_value) as payment_total,
        count(*) as count_payments,
        array_agg(distinct payment_type) as payment_types
    from {{ ref('stg_olist__payments') }}
    group by order_id
)

select
    o.order_id,
    o.customer_id,
    o.order_status,
    o.purchased_ts,
    o.delivered_customer_ts,
    o.estimated_delivery_dt,
    p.payment_total,
    p.count_payments,
    p.payment_types,
    case when o.order_status = 'delivered' then 1 else 0 end as is_delivered,
    (o.delivered_customer_ts::date - o.purchased_ts::date) as delivery_waiting_period
from orders o
left join payments p
on o.order_id = p.order_id
