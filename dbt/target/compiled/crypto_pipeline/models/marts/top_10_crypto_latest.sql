with base as (

    select *
    from `dtc-course-486211`.`crypto_project1`.`top_10_crypto`

),

latest as (

    select max(timestamp_hour) as max_ts
    from base

)

select b.*
from base b
join latest l
    on b.timestamp_hour = l.max_ts