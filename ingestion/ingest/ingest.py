import requests
import time
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

def run_ingest():
    url = "https://api.coingecko.com/api/v3/coins/markets"


    all_data = []

    for page in range(1, 4):
        response = requests.get(url, params= {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 100,
            "page": page,
        })
        data = response.json()
        
        if isinstance(data, list):
            all_data.extend(data)
        time.sleep(1)


    df = pd.DataFrame(all_data)
    print(df.shape)

    # selecting only the required columns
    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "market_cap_rank",
        "total_volume",
        "price_change_percentage_24h",
        "high_24h",
        "low_24h",
        "circulating_supply",
        "ath",
        "atl",
        "last_updated"
    ]]

    # drop rows with any NA value
    # df = df.dropna()

    df = df.astype({
    'current_price': float,
    'market_cap': float,
    'market_cap_rank': float,
    'total_volume': float,
    'price_change_percentage_24h': float,
    'high_24h': float,
    'low_24h': float,
    'circulating_supply': float,
    'ath': float,
    'atl': float,
    'id': str,
    'symbol': str,
    'name': str,
    })

    # Convert 'last_updated' to a pandas datetime object and round to the nearest minute
    df["last_updated"] = pd.to_datetime(df["last_updated"]).dt.floor('min')

    # Add a new column 'ingestion_time' with the current timestamp
    df["ingestion_time"] = datetime.now(timezone.utc).replace(second=0, microsecond=0)


    # saving parquet locally 

    path = Path("/tmp/parquet/data.parquet")
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)


if __name__ == "__main__":
    run_ingest()

