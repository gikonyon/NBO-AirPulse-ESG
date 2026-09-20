# 🇰🇪 Nairobi Air Quality Analytics Engine

An open-source, interactive Streamlit dashboard for real-time and historical air quality monitoring across **Nairobi, Kenya**. This application fetches data from public environmental sensor networks (OpenAQ v3, AirQo, and Sensor.Community) to visualize $PM_{2.5}$, $PM_{10}$, and Air Quality Index (AQI) levels across Nairobi's sub-counties.

---

## 🌟 Features

* **Live Public Data Ingestion:** Connects directly to OpenAQ & AirQo REST APIs for near real-time sensor measurements.
* **Geospatial Mapping:** Interactive PyDeck / Folium heatmaps showing micro-climate pollution hot spots (e.g., Industrial Area, CBD, Eastlands, Westlands).
* **Diurnal & Historical Trends:** Analyzes hourly traffic peak hours ($PM_{2.5}$ spikes) vs. WHO global safety thresholds ($15\ \mu g/m^3$ 24-hr average).
* **Zero Heavy Dependencies:** Fully cloud-executable via Streamlit Cloud and GitHub Actions—leaving local developer machines completely clean.

---

## 🏗️ Repository Architecture

```text
nairobi-air-quality/
├── .gitignore               # Protects API secrets, virtualenvs, and data dumps
├── .streamlit/
│   ├── config.toml          # Custom dark UI styling & page layout
│   └── secrets.toml         # Local API keys (OpenAQ / AirQo tokens)
├── app.py                   # Main Streamlit Dashboard application
├── requirements.txt         # Dependencies for Streamlit Cloud
└── README.md                # Project Overview & Setup
