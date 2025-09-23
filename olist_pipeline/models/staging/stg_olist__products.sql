with product as (
    select * from {{ source('olist', 'products') }}
),

category_name_translate as (
    select * from {{ ref('product_category_name_translation') }}
)

select
    p.product_id,
    coalesce(ts.product_category_name_english, p.product_category_name) as category_name,
    p.product_weight_g as weight_g,
    p.product_width_cm as width_cm,
    p.product_length_cm as length_cm,
    p.product_height_cm as height_cm
from product p left join category_name_translate ts
on p.product_category_name = ts.product_category_name