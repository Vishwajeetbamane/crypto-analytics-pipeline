select
    timestamp_hour,
    coin_id,
    name,
    symbol,

    current_price,
    market_cap,
    total_volume,
    price_change_percentage_24h,
    market_cap_rank

from {{ ref('stg_crypto') }}

where market_cap_rank <= 10