
import requests
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd


url = "https://api.coingecko.com/api/v3/coins/markets"

all_data = []

for page in range(1, 7):
    response = requests.get(url, params= {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": page,
    })
    data = response.json()
    
    if isinstance(data, list):
        all_data.extend(data)


df = pd.DataFrame(all_data)

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
df = df.dropna()


#converting to valid pandas datetime object
df["last_updated"] = pd.to_datetime(df["last_updated"])

# saving parquet locally 

project_path = Path(__file__).resolve().parent.parent.parent
path = Path(f"{project_path}/parquet/data.parquet")
path.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(path, index=False)




