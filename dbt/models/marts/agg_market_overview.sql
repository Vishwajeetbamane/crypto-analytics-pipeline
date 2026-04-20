select
    ingestion_time,

    sum(market_cap) as total_market_cap,
    sum(total_volume) as total_volume,
    avg(current_price) as avg_price,
    avg(price_change_percentage_24h) as avg_price_change_24h,

from {{ ref('fact_crypto_metrics') }}

group by ingestion_time