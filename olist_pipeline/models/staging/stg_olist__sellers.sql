select 
    seller_id,
    lower(seller_city) as seller_city,
    upper(seller_state) as seller_state
from {{ source('olist', 'sellers') }}