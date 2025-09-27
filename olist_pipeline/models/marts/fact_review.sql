select
    order_id,
    round(avg(review_score),0) as avg_score,
    min(creation_date) as creation_date
from  {{ ref('stg_review') }}
group by order_id