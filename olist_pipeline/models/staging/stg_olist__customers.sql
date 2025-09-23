select 
    customer_id,
    lower(customer_city) as customer_city,
    upper(customer_state) as customer_state
from {{ source('olist', 'customers') }}