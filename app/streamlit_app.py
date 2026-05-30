import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# --- 1. GLOBAL SETTINGS & STYLES ---
st.set_page_config(page_title="Finance Intelligence System", layout="wide")

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title(" Navigation")
section = st.sidebar.radio(
    "Go to page:",
    ["Overview & KPIs", "Spending Analytics", "Anomaly Detection", "Expense Forecasting"]
)

# --- 3. DATA STORAGE LAYER ---
# Streamlit runs from the root folder, so relative pathing is clean
@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/Personal_Finance_Dataset.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    return df

df = load_data()
# Clean dates globally for time-based features
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Global Sidebar Filter (Only visible/relevant for data slicing pages)
if section in ["Overview & KPIs", "Spending Analytics"]:
    st.sidebar.header("⚙️ Global Filters")
    categories = st.sidebar.multiselect(
        "Select Categories",
        options=df['Category'].unique(),
        default=df['Category'].unique()
    )
    filtered_df = df[df['Category'].isin(categories)].copy()
else:
    filtered_df = df.copy()


# --- 4. PAGE ROUTING LOGIC ---

# ==========================================
# PAGE 1: OVERVIEW & KPIS
# ==========================================
if section == "Overview & KPIs":
    st.title("Personal Finance Intelligence System")
    st.write("Welcome to your financial command center. Monitor health indicators and raw logs below.")
    st.write("---")
    
    # Financial Analytics Math
    total_income = filtered_df[filtered_df['Type'] == 'Income']['Amount'].sum()
    total_expense = filtered_df[filtered_df['Type'] == 'Expense']['Amount'].sum()
    net_savings = total_income - total_expense
    
    # KPI Grid cards
    col1, col2, col3 = st.columns(3)
    col1.metric(" Total Income", f"${total_income:,.2f}")
    col2.metric(" Total Expense", f"${total_expense:,.2f}")
    col3.metric(" Net Savings", f"${net_savings:,.2f}")
    st.write("---")
    
    # Financial Health Scoring Logic
    st.subheader(" Financial Health Index")
    monthly_summary = filtered_df.groupby('Month').apply(lambda x: pd.Series({
        'Income': x[x['Type'] == 'Income']['Amount'].sum(),
        'Expense': x[x['Type'] == 'Expense']['Amount'].sum()
    })).reset_index()
    
    if not monthly_summary.empty:
        monthly_summary['Savings'] = monthly_summary['Income'] - monthly_summary['Expense']
        monthly_summary['Savings Rate'] = (monthly_summary['Savings'] / monthly_summary['Income'].replace(0, 1)) * 100
        
        def calculate_score(row):
            score = 50
            if row['Savings Rate'] > 20: score += 30
            elif row['Savings Rate'] > 10: score += 15
            if row['Savings'] > 0: score += 20
            return min(score, 100)
            
        monthly_summary['Health Score'] = monthly_summary.apply(calculate_score, axis=1)
        avg_score = monthly_summary['Health Score'].mean()
        
        st.metric("Overall Financial Health Score", f"{avg_score:.1f} / 100")
        fig_health = px.line(monthly_summary, x='Month', y='Health Score', title="Health Status Trajectory", markers=True)
        st.plotly_chart(fig_health, use_container_width=True)
    
    st.write("---")
    st.subheader("Recent Ledger Audit Trail")
    st.dataframe(filtered_df.sort_values(by='Date', ascending=False).head(100), use_container_width=True)


# ==========================================
# PAGE 2: SPENDING ANALYTICS
# ==========================================
elif section == "Spending Analytics":
    st.title(" Expense Breakdown & Slicing")
    st.write("Dig into where your money is traveling monthly across your selected categories.")
    
    expense_df = filtered_df[filtered_df['Type'] == 'Expense']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Category Totals")
        category_spending = expense_df.groupby('Category')['Amount'].sum().reset_index()
        fig_bar = px.bar(category_spending, x='Category', y='Amount', color='Category', title="Total Outflow By Type")
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with col2:
        st.subheader("Structural Proportions")
        fig_pie = px.pie(category_spending, values='Amount', names='Category', title="Expense Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)
        
    st.write("---")
    st.subheader(" Over-Time Trend Analysis")
    monthly_expense = expense_df.groupby('Month')['Amount'].sum().reset_index()
    fig_trend = px.line(monthly_expense, x='Month', y='Amount', title="Historical Monthly Cost Fluctuations", markers=True)
    st.plotly_chart(fig_trend, use_container_width=True)


# ==========================================
# PAGE 3: ANOMALY DETECTION
# ==========================================
elif section == "Anomaly Detection":
    st.title(" Suspicious Outflow Detection")
    st.write("Using ML Isolation Forests to auto-flag high-risk or unusual transaction volatility.")
    
    expense_df = df[df['Type'] == 'Expense'].copy()
    
    if not expense_df.empty:
        # Run ML engine isolation algorithms
        model = IsolationForest(contamination=0.03, random_state=42)
        expense_df['anomaly'] = model.fit_predict(expense_df[['Amount']])
        expense_df['Status'] = expense_df['anomaly'].apply(lambda x: 'Suspicious' if x == -1 else 'Normal')
        
        anomalies = expense_df[expense_df['anomaly'] == -1]
        
        st.metric("Total Flagged Transactions", len(anomalies))
        
        # Plotly Scatter chart for visualization
        fig_anom = px.scatter(
            expense_df, x='Date', y='Amount', color='Status',
            color_discrete_map={'Normal': '#636EFA', 'Suspicious': '#EF553B'},
            title="Outlier Detection Boundary Map"
        )
        st.plotly_chart(fig_anom, use_container_width=True)
        
        st.subheader(" Suspicious Audit Log")
        st.dataframe(
            anomalies[['Date', 'Transaction Description', 'Category', 'Amount']].sort_values(by='Amount', ascending=False),
            use_container_width=True
        )
    else:
        st.info("No expense data available to execute structural outlier calculations.")

# ==========================================
# PAGE 4: EXPENSE FORECASTING
# ==========================================

elif section == "Expense Forecasting":

    st.title("🔮 Predictive Budget Projections")

    st.write(
        "Forecasting future expenses using moving-average trend analysis."
    )

    expense_df = df[df['Type'] == 'Expense'].copy()

    monthly_expense = (
        expense_df.groupby('Month')['Amount']
        .sum()
        .reset_index()
    )

    # Create moving average forecast
    monthly_expense['Forecast'] = (
        monthly_expense['Amount']
        .rolling(window=3)
        .mean()
    )

    # Plot interactive chart
    fig_forecast = px.line(
        monthly_expense,
        x='Month',
        y=['Amount', 'Forecast'],
        title="Historical Expense Trend & Forecast"
    )

    st.plotly_chart(fig_forecast, use_container_width=True)

    st.subheader("📅 Forecast Table")

    st.dataframe(
        monthly_expense.tail(12),
        use_container_width=True
    )

    latest_forecast = monthly_expense['Forecast'].iloc[-1]

    st.metric(
        "Projected Expense Trend",
        f"${latest_forecast:,.2f}"
    )
       