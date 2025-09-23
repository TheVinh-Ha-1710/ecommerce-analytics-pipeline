select
    review_id,
    order_id,
    review_score,
    cast(review_creation_date as date) as creation_date,
    cast(review_answer_timestamp as timestamp) as review_answer_ts 
from {{ source('olist', 'reviews') }}