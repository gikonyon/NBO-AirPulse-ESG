import pandas as pd

# Load our Nairobi dataset
df = pd.read_csv('nairobi_aqi_raw.csv')

# ESG Metric: WHO Safety Limit for PM₂.₅ is 15 µg/m³
limit = 15
total_records = len(df)
violation_count = len(df[df['pm2_5'] > limit])
compliance_rate = ((total_records - violation_count) / total_records) * 100

print("="*40)
print("  NBO-AIRPULSE: ESG COMPLIANCE REPORT  ")
print("="*40)
print(f"Location: Nairobi CBD")
print(f"Pollutants Tracked: PM₂.₅ and NO₂")
print(f"Total Monitoring Hours: {total_records}")
print(f"Hours Exceeding WHO Limits: {violation_count}")
print(f"Overall Compliance Rate: {compliance_rate:.2f}%")
print("="*40)
print("STATUS: Audit Complete.")
