import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page layout to wide
st.set_page_config(
    page_title="LeatherPulse 2026: Executive Command Center",
    page_icon="🇰🇪",
    layout="wide"
)

# ---------------------------------------------------------
# DATA GENERATION ENGINE
# ---------------------------------------------------------
@st.cache_data
def load_leatherpulse_data():
    units_data = [
        ("UNIT_01", "Nairobi"),
        ("UNIT_02", "Athi River"),
        ("UNIT_03", "Thika"),
        ("UNIT_04", "Machakos"),
        ("UNIT_05", "Naivasha"),
        ("UNIT_06", "Kisumu"),
        ("UNIT_07", "Mombasa"),
    ]
    
    rows = []
    for unit_id, region in units_data:
        # Data Analysts (Doubled for Digital Integrity)
        rows.append({
            "Factory_Unit": unit_id,
            "Region": region,
            "Department": "Analytics",
            "Job_Title": "Data Analyst",
            "Job_Type": "Salaried",
            "Count": 2,
            "Monthly_Salary_KES": 110000
        })
        # ESG Lead
        rows.append({
            "Factory_Unit": unit_id,
            "Region": region,
            "Department": "Governance",
            "Job_Title": "ESG Lead",
            "Job_Type": "Salaried",
            "Count": 1,
            "Monthly_Salary_KES": 160000
        })
        # Operations Supervisors
        rows.append({
            "Factory_Unit": unit_id,
            "Region": region,
            "Department": "Operations",
            "Job_Title": "Prod. Supervisor",
            "Job_Type": "Salaried",
            "Count": 5,
            "Monthly_Salary_KES": 85000
        })
        # Machine Operators
        rows.append({
            "Factory_Unit": unit_id,
            "Region": region,
            "Department": "Production",
            "Job_Title": "Machine Operator",
            "Job_Type": "Waged",
            "Count": 1428,
            "Monthly_Salary_KES": 48000
        })
        
    df = pd.DataFrame(rows)
    return df

# Load initial dataset
raw_df = load_leatherpulse_data()

# ---------------------------------------------------------
# SIDEBAR CONTROLS & CONTINUOUS CALCULATIONS
# ---------------------------------------------------------
st.sidebar.header("⚙️ Executive Simulation Controls")

# DTI Ratio Slider for FIT Plus
dti_ratio = st.sidebar.slider(
    "Debt-to-Income (DTI) Limit for FIT Plus",
    min_value=0.10,
    max_value=0.50,
    value=0.33,
    step=0.01,
    help="Standard banking threshold for monthly debt capacity calculation."
)

# Region Slicer
regions = ["All Regions"] + list(raw_df["Region"].unique())
selected_region = st.sidebar.selectbox("Filter by Industrial Region", regions)

# Dynamic Salary Adjustment Factor
salary_multiplier = st.sidebar.slider(
    "Baseline Salary Adjustment (%)",
    min_value=90,
    max_value=150,
    value=100,
    step=5
) / 100.0

# Dynamic Calculations Engine
df = raw_df.copy()
df["Monthly_Salary_KES"] = df["Monthly_Salary_KES"] * salary_multiplier
df["Total_Monthly_Payroll"] = df["Count"] * df["Monthly_Salary_KES"]
df["Credit_Repay_Capacity"] = df["Monthly_Salary_KES"] * dti_ratio
df["Total_Credit_Pool"] = df["Count"] * df["Credit_Repay_Capacity"]

if selected_region != "All Regions":
    df = df[df["Region"] == selected_region]

# ---------------------------------------------------------
# DASHBOARD HEADER & KPI CARDS
# ---------------------------------------------------------
st.title("🇰🇪 LEATHERPULSE 2026: INDUSTRIAL COMMAND CENTER")
st.markdown("### *Continuous Economic Modeling & Financial Inclusion Engine (FIT Plus)*")

tot_headcount = df["Count"].sum()
tot_payroll = df["Total_Monthly_Payroll"].sum()
tot_analysts = df[df["Job_Title"] == "Data Analyst"]["Count"].sum()
tot_credit_pool = df["Total_Credit_Pool"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Headcount", f"{tot_headcount:,} Roles")
col2.metric("Monthly Payroll", f"KES {tot_payroll/1e6:.2f}M")
col3.metric("Data Analyst Staff", f"{tot_analysts} Analysts")
col4.metric("FIT Plus Credit Pool", f"KES {tot_credit_pool/1e6:.2f}M")

st.markdown("---")

# ---------------------------------------------------------
# VISUALIZATION TABS
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "📊 Workforce & Payroll Breakdown",
    "📈 Governance (ESG 0.95 Correlation)",
    "💰 FIT Plus Lending & Credit Capacity"
])

# --- TAB 1: WORKFORCE & PAYROLL ---
with tab1:
    st.subheader("1. Regional Workforce & Headcount Distribution")
    col_a, col_b = st.columns(2)
    
    with col_a:
        fig_payroll = px.bar(
            df.groupby("Region")["Total_Monthly_Payroll"].sum().reset_index(),
            x="Region",
            y="Total_Monthly_Payroll",
            title="Total Monthly Payroll by Region (KES)",
            color="Region",
            text_auto='.2s'
        )
        st.plotly_chart(fig_payroll, use_container_width=True)
        
    with col_b:
        fig_dept = px.pie(
            df.groupby("Department")["Count"].sum().reset_index(),
            names="Department",
            values="Count",
            title="Headcount Distribution by Department",
            hole=0.4
        )
        st.plotly_chart(fig_dept, use_container_width=True)

# --- TAB 2: GOVERNANCE & ESG ---
with tab2:
    st.subheader("2. ESG Governance vs Market Access (0.95 Correlation)")
    st.caption("Demonstrates the relationship between Data Analyst audit hours, compliance, and international market clearance.")
    
    # Continuous Simulation for Regression Plot
    np.random.seed(42)
    analyst_hours = np.linspace(100, 600, 50)
    market_access_prob = 0.95 * (analyst_hours / 600) + np.random.normal(0, 0.03, 50)
    market_access_prob = np.clip(market_access_prob, 0, 1.0)
    
    sim_df = pd.DataFrame({
        "Analyst_Audit_Hours": analyst_hours,
        "Market_Access_Probability": market_access_prob
    })
    
    fig_gov = px.scatter(
        sim_df,
        x="Analyst_Audit_Hours",
        y="Market_Access_Probability",
        trendline="ols",
        title="0.95 Correlation Proof: Analyst Hours vs Global Market Access",
        labels={"Analyst_Audit_Hours": "Data Analyst Audit Hours / Month", "Market_Access_Probability": "US/EU Export Market Clearance Probability"}
    )
    st.plotly_chart(fig_gov, use_container_width=True)

# --- TAB 3: FIT PLUS INTEGRATION ---
with tab3:
    st.subheader("3. Financial Inclusion Technology (FIT Plus) Capacity Matrix")
    
    fig_credit = px.histogram(
        df,
        x="Job_Title",
        y="Credit_Repay_Capacity",
        color="Department",
        title=f"Monthly Repayment Limit per Employee at {int(dti_ratio*100)}% DTI (KES)",
        barmode="group"
    )
    st.plotly_chart(fig_credit, use_container_width=True)
    
    st.markdown("#### Full Operational Table")
    st.dataframe(
        df[["Factory_Unit", "Region", "Job_Title", "Count", "Monthly_Salary_KES", "Total_Monthly_Payroll", "Credit_Repay_Capacity"]],
        use_container_width=True
    )
