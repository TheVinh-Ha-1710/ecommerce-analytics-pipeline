with states as (
    select * from {{ ref('brazil_states') }}
),

customers as (
    select
        customer_id,
        initcap(customer_city) as customer_city,
        upper(customer_state) as customer_state
    from  {{ source('olist', 'customer') }}
)

select 
    c.customer_id,
    c.customer_city as customer_city,
    s.state_name as customer_state,
    c.customer_state as state_init
from customers c left join states s
on c.customer_state = s.state_init