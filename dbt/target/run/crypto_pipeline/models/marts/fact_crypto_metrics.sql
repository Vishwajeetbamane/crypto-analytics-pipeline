
  
    

    create or replace table `dtc-course-486211`.`crypto_project1`.`fact_crypto_metrics`
      
    
    

    
    OPTIONS()
    as (
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

from `dtc-course-486211`.`crypto_project1`.`stg_crypto`
    );
  