select
    last_updated,
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
    circulating_supply,
    ingestion_time

from {{ ref('stg_crypto') }}