# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 21:48:37 2025

@author: Tonsbray
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
df = pd.read_csv("dashboard/hour.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

st.set_page_config(page_title="Bike Sharing Dashboard",
                   page_icon=":bike:",
                   layout="wide")

# Sidebar - Date filter
st.sidebar.header("Filter:")
min_date = df["dteday"].min()
max_date = df["dteday"].max()
start_date, end_date = st.sidebar.date_input("Date Filter", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filter dataset
filtered_df = df[(df["dteday"] >= pd.to_datetime(start_date)) & (df["dteday"] <= pd.to_datetime(end_date))]

# Metrics
total_rides = filtered_df['cnt'].sum()
total_casual = filtered_df['casual'].sum()
total_registered = filtered_df['registered'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Rides", total_rides)
col2.metric("Total Casual Rides", total_casual)
col3.metric("Total Registered Rides", total_registered)

st.markdown("---")

# Monthly trend
monthly_df = filtered_df.resample('M', on='dteday').sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly_df, x='dteday', y='cnt', marker='o', ax=ax)
ax.set_title("Monthly Bike Rentals")
ax.set_ylabel("Total Rides")
ax.set_xlabel("")
st.pyplot(fig)

# Weekday distribution
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=filtered_df, x='weekday', y='cnt', estimator=sum, ci=None, ax=ax)
ax.set_title("Bike Rentals by Weekday")
ax.set_ylabel("Total Rides")
ax.set_xlabel("Weekday")
st.pyplot(fig)

