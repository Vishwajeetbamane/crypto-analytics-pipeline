
  
    

    create or replace table `dtc-course-486211`.`crypto_project1`.`agg_market_overview`
      
    
    

    
    OPTIONS()
    as (
      select
    timestamp_hour,

    sum(market_cap) as total_market_cap,
    sum(total_volume) as total_volume,
    avg(current_price) as avg_price,
    avg(price_change_percentage_24h) as avg_price_change_24h

from `dtc-course-486211`.`crypto_project1`.`fact_crypto_metrics`

group by timestamp_hour
    );
  