
  
    

    create or replace table `dtc-course-486211`.`crypto_project1`.`top_10_crypto`
      
    
    

    
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
    price_change_percentage_24h,
    market_cap_rank

from `dtc-course-486211`.`crypto_project1`.`stg_crypto`

where market_cap_rank <= 10
    );
  