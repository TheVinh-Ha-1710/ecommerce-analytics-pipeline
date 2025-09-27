select
    product_id,
    category_name,
    weight_g,
    concat_ws(' x ', width_cm, height_cm, length_cm) as dimension_cm
from {{ ref('stg_product') }}