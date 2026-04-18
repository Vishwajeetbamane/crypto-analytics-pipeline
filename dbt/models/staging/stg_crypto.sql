SELECT 

cast(id as string) as coin_id,
cast(name as string) as name,
cast(symbol as string) as symbol,
cast(current_price as float64) as current_price,

cast(market_cap as float64) as market_cap,
cast(market_cap_rank as int) as market_cap_rank,
cast(total_volume as float64) as total_volume,

cast(high_24h as float64) as high_24h,
cast(low_24h as float64) as low_24h,
cast(price_change_percentage_24h as float64) as price_change_percentage_24h,

cast(ath as float64) as ath,
cast(atl as float64) as atl,
cast(circulating_supply as float64) as circulating_supply,

timestamp_trunc(last_updated, hour, "UTC") as timestamp_hour,
cast(year as int) as year,
cast(month as int) as month,
cast(day as int) as day,
cast(hour as int) as hour

FROM {{ source('src_crypto', 'crypto_data_ext') }}
