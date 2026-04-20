with base as (

    select *
    from {{ ref('top_10_crypto') }}

),

latest as (

    select max(ingestion_time) as max_ts
    from base

)

select b.*
from base b
join latest l
    on b.ingestion_time = l.max_ts