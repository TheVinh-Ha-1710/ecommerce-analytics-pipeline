with product as (
    select * from {{ source('olist', 'product') }}
),

category_name_translate as (
    select * from {{ ref('product_category_name_translation') }}
)

select
    p.product_id,
    initcap(coalesce(
        coalesce(ts.product_category_name_english, p.product_category_name),
        'Unknown'
    )) as category_name,
    coalesce(p.product_weight_g, 0) as weight_g,
    coalesce(p.product_width_cm, 0) as width_cm,
    coalesce(p.product_length_cm, 0) as length_cm,
    coalesce(p.product_height_cm, 0) as height_cm
from product p left join category_name_translate ts
on p.product_category_name = ts.product_category_name