# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="Shopper Segmentation", layout="wide")

st.title("🛍️ Shopper Segmentation Dashboard")
st.markdown("Built by **Gargi Kadam**")

# --- Load Data ---
@st.cache_data
def load_data():
    file_path = os.path.join("data", "online_retail.csv")
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df.dropna(subset=["CustomerID"], inplace=True)
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Options")
country_filter = st.sidebar.multiselect("Select Country", df['Country'].unique(), default=['United Kingdom'])
date_range = st.sidebar.date_input("Select Date Range", [df['InvoiceDate'].min(), df['InvoiceDate'].max()])

# --- Apply Filters ---
filtered_df = df[
    (df['Country'].isin(country_filter)) &
    (df['InvoiceDate'] >= pd.to_datetime(date_range[0])) &
    (df['InvoiceDate'] <= pd.to_datetime(date_range[1]))
]

# --- Display Metrics ---
st.subheader("📊 Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Unique Customers", filtered_df['CustomerID'].nunique())
col2.metric("Total Revenue", f"£{filtered_df['Quantity'].mul(filtered_df['UnitPrice']).sum():,.2f}")
col3.metric("Transactions", filtered_df['InvoiceNo'].nunique())

# --- Data Preview ---
st.subheader("🧾 Transaction Data Preview")
st.dataframe(filtered_df.head(10), use_container_width=True)

# --- Optional Model Prediction Section ---
st.subheader("🤖 (Optional) Predict Segment")
st.markdown("*Enter sample transaction values to predict customer type (if model is integrated)*")

quantity = st.number_input("Quantity", value=10)
unit_price = st.number_input("Unit Price (£)", value=5.0)

if st.button("Predict (disabled - model not uploaded)"):
    st.warning("Prediction feature is currently disabled. You can integrate it later with a model.")

# --- Footer ---
st.markdown("---")
st.caption("Gargi Kadam · Shopper Segmentation · Streamlit Demo")
