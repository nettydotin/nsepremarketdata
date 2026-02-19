import requests
import pandas as pd
from datetime import date

url = "https://www.nseindia.com/api/market-data-pre-open?key=ALL"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com"
}

session = requests.Session()
session.get("https://www.nseindia.com", headers=headers)

response = session.get(url, headers=headers)
data = response.json()

rows = [item["metadata"] for item in data["data"]]
df = pd.DataFrame(rows)

today = date.today().strftime("%Y-%m-%d")
filename = f"NSE_PreMarket_{today}.xlsx"

df.to_excel(filename, index=False)

print(f"Saved {filename}")
