# NBO-AirPulse-ESG
# NBO-AirPulse: Nairobi Environmental & ESG Intelligence

## 🌍 Overview
NBO-AirPulse is a high-volume data analytics project designed to validate the "Environmental" pillar of ESG in Nairobi. Using real-time data from the **Nairobi City County Public Portal (supported by Breathe Cities)** and historical data (2022-2026), this project tracks $PM_{2.5}$ and $NO_2$ levels across 50+ urban sensors.

## 🚀 Objectives
* **Real-time Monitoring:** Ingesting hourly air quality data from Nairobi's city-owned sensor network.
* **Integrity Auditing:** Comparing corporate sustainability claims against physical air quality sensors in industrial zones (e.g., Baba Dogo, Industrial Area).
* **Predictive Analytics:** Forecasting "Hazardous Air Days" using LSTM neural networks.

## 🛠️ Tech Stack
* **Data:** Open-Meteo Air Quality API, Zenodo (Nairobi Dataset v1.0).
* **Processing:** Python (Pandas, NumPy).
* **Viz:** Plotly, Folium (Geospatial maps), Streamlit.
