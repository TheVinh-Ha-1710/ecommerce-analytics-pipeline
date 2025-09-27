{% test positive_value(model, column_name) %}

    select {{ column_name }} as invalid_val
    from {{ model }}
    where {{ column_name }} < 0

{% endtest %}