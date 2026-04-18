select
    timestamp_hour,
    coin_id,
    name,
    symbol,

    current_price,
    market_cap,
    total_volume,
    high_24h,
    low_24h,
    price_change_percentage_24h,
    ath,
    atl,
    circulating_supply

from {{ ref('stg_crypto') }}