import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data we ingested in Step 1
df = pd.read_csv('nairobi_aqi_raw.csv')
df['time'] = pd.to_datetime(df['time'])

# Set up the visual style
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Plot PM₂.₅ and NO₂
plt.plot(df['time'], df['pm2_5'], label='PM₂.₅ (Fine Particles)', color='teal', linewidth=2)
plt.plot(df['time'], df['nitrogen_dioxide'], label='NO₂ (Nitrogen Dioxide)', color='orange', alpha=0.7)

# Add ESG Reference Line (WHO 24h Limit for PM₂.₅ is 15 µg/m³)
plt.axhline(y=15, color='red', linestyle='--', label='WHO Safety Limit')

plt.title('NBO-AirPulse: Nairobi Air Quality Trends (7-Day Audit)', fontsize=15)
plt.xlabel('Date/Time', fontsize=12)
plt.ylabel('Concentration (µg/m³)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart for our ESG Report
plt.savefig('nairobi_pollution_trends.png')
print("✅ Visualization saved as nairobi_pollution_trends.png")
