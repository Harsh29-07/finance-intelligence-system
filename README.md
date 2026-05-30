# Personal Finance Intelligence System

## Overview

The Personal Finance Intelligence System is an end-to-end financial analytics platform designed to help users monitor, analyze, and forecast personal spending behavior.

The system combines financial KPI tracking, anomaly detection, expense forecasting, and interactive dashboarding into a single analytics application built using Python and Streamlit.

This project demonstrates practical applications of:

* Financial analytics
* KPI engineering
* Predictive analytics
* Anomaly detection
* Dashboard development
* Business intelligence workflows

---

## Problem Statement

Many individuals struggle to:

* Track monthly spending patterns
* Understand financial behavior
* Detect abnormal expenses
* Forecast future liabilities
* Maintain healthy savings habits

Traditional budgeting tools often provide only raw transaction logs without meaningful analytical insights.

This system addresses that gap by transforming transaction data into actionable financial intelligence.

---

## Features

### Financial KPI Dashboard

* Total income tracking
* Total expense tracking
* Net savings calculation
* Financial health scoring

### Spending Analytics

* Category-wise expense analysis
* Expense distribution visualization
* Monthly spending trends
* Interactive filtering

### Anomaly Detection

* Isolation Forest based anomaly detection
* Detection of suspicious or unusual expenses
* Outlier visualization dashboard
* High-risk transaction audit table

### Forecasting Engine

* Expense trend forecasting
* Moving-average prediction modeling
* Future expense projection dashboard

### Interactive Dashboard

* Built with Streamlit
* Interactive Plotly visualizations
* Multi-page navigation
* Dynamic filtering and analytics

---

## Tech Stack

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn

### Visualization

* Plotly
* Matplotlib

### Dashboard

* Streamlit

### Forecasting

* Moving Average Trend Forecasting

---

## Project Structure

```text
finance-intelligence-system/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   │   └── Personal_Finance_Dataset.csv
│   │
│   └── processed/
│       └── cleaned_finance_data.csv
│
├── notebooks/
│   └── 01_data_loading.ipynb
│
├── reports/
│   ├── business_case.md
│   └── screenshots/
│
├── src/
│   ├── preprocessing.py
│   ├── kpi_engine.py
│   ├── anomaly_detection.py
│   ├── forecasting.py
│   └── scoring.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Key Functionalities

### Financial Health Index

A custom scoring engine evaluates monthly financial health based on:

* Savings rate
* Cash flow consistency
* Expense behavior

### Anomaly Detection Engine

Machine learning based Isolation Forest model identifies:

* Abnormally large expenses
* Suspicious transactions
* Unusual spending behavior

### Expense Forecasting

Forecasting logic estimates future monthly expenses using historical trends and moving averages.

---

## Dashboard Modules

### Overview & KPIs

* Financial summary metrics
* Health score visualization
* Ledger audit trail

### Spending Analytics

* Category-level analysis
* Expense distribution charts
* Historical trend analysis

### Anomaly Detection

* Suspicious transaction identification
* Outlier visualization
* Risk transaction table

### Expense Forecasting

* Future expense projections
* Trend visualization
* Forecast summary metrics

---

## Business Value

This system helps users:

* Improve financial visibility
* Detect abnormal spending patterns
* Forecast future liabilities
* Support budgeting decisions
* Monitor long-term financial behavior

---

## How to Run

### 1. Clone Repository

```bash
git clone <repository-link>
cd finance-intelligence-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Streamlit Application

```bash
streamlit run app/streamlit_app.py
```

---

## Future Improvements

Potential future enhancements include:

* SQL database integration
* User authentication
* Real-time bank transaction APIs
* Advanced forecasting models
* Cloud deployment
* Personalized financial recommendations

---

## Author

Harsh Saini

Financial Analytics & Business Intelligence Enthusiast
