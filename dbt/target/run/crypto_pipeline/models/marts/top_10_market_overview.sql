
  
    

    create or replace table `dtc-course-486211`.`crypto_project1`.`top_10_market_overview`
      
    
    

    
    OPTIONS()
    as (
      select
    timestamp_hour,

    sum(market_cap) as top_10_market_cap,
    sum(total_volume) as top_10_volume

from `dtc-course-486211`.`crypto_project1`.`stg_crypto`

where market_cap_rank <= 10

group by timestamp_hour
    );
  