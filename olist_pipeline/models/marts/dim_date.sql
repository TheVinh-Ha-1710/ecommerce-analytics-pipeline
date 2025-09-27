with date_spine as (

    {{ dbt_utils.date_spine(
        datepart="day",
        start_date="cast('2016-01-01' as date)",
        end_date="cast('2030-12-31' as date)"
    ) }}

)

select
    date_day::date as date_key,              -- primary key for joining
    extract(year from date_day) as year,
    extract(quarter from date_day) as quarter,
    extract(month from date_day) as month,
    initcap(to_char(date_day, 'Month')) as month_name,
    extract(week from date_day) as week,
    extract(dow from date_day) as day_of_week,
    to_char(date_day, 'Day') as weekday_name,

    case
        when extract(month from date_day) in (12,1,2) then 'Winter'
        when extract(month from date_day) in (3,4,5) then 'Spring'
        when extract(month from date_day) in (6,7,8) then 'Summer'
        when extract(month from date_day) in (9,10,11) then 'Fall'
    end as season,

    date_trunc('month', date_day)::date as month_start,
    date_trunc('quarter', date_day)::date as quarter_start,
    date_trunc('year', date_day)::date as year_start

from date_spine