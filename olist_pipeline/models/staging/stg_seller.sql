with states as (
    select * from {{ ref('brazil_states') }}
),

sellers as (
    select
        seller_id,
        initcap(seller_city) as seller_city,
        upper(seller_state) as seller_state
    from  {{ source('olist', 'seller') }}
)

select 
    s.seller_id,
    s.seller_city as seller_city,
    st.state_name as seller_state,
    s.seller_state as state_init
from sellers s left join states st
on s.seller_state = st.state_init