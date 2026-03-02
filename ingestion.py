import pandas as pd
import requests

def fetch_nairobi_data():
url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {
"latitude": -1.2864,
"longitude": 36.8172,
"hourly": ["pm2_5", "nitrogen_dioxide"],
"timezone": "Africa/Nairobi",
"past_days": 7
}
r = requests.get(url, params=params)
if r.status_code == 200:
df = pd.DataFrame(r.json()['hourly'])
print(f"✅ Ingested {len(df)} rows of Nairobi data.")
return df
return None

if name == 'main':
df = fetch_nairobi_data()
if df is not None:
df.to_csv('nairobi_aqi_raw.csv', index=False)
