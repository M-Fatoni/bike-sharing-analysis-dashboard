# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 21:48:37 2025

@author: Tonsbray
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
df_hour = pd.read_csv("dashboard/hour.csv")
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

st.set_page_config(page_title="Bike-sharing Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

# ----- SIDEBAR -----
with st.sidebar:
    st.sidebar.header("Filter:")
    
    min_date = df_hour["dteday"].min()
    max_date = df_hour["dteday"].max()
    
    start_date, end_date = st.date_input(
        label="Pilih Rentang Waktu", min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data sesuai rentang tanggal
main_df = df_hour[(df_hour["dteday"] >= str(start_date)) & (df_hour["dteday"] <= str(end_date))]

# ----- MAINPAGE -----
st.title(":bar_chart: Bike-Sharing Dashboard")
st.markdown("##")

col1, col2, col3 = st.columns(3)

with col1:
    total_all_rides = main_df['cnt'].sum()
    st.metric("Total Rides", value=total_all_rides)
with col2:
    total_casual_rides = main_df['casual'].sum()
    st.metric("Total Casual Rides", value=total_casual_rides)
with col3:
    total_registered_rides = main_df['registered'].sum()
    st.metric("Total Registered Rides", value=total_registered_rides)

st.markdown("---")

# ----- BARPLOT: Perbedaan Penyewaan Sepeda pada Hari Kerja dan Hari Libur -----
df_grouped = main_df.groupby("workingday")[["registered", "casual"]].sum().reset_index()
df_grouped["workingday"] = df_grouped["workingday"].map({1: "Hari Kerja", 0: "Hari Libur"})
df_melted = df_grouped.melt(id_vars="workingday", var_name="User Type", value_name="Total Rentals")

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.barplot(data=df_melted, x="workingday", y="Total Rentals", hue="User Type", palette=["#6ee5c7", "#e56e8c"], ax=ax1)
ax1.set_xlabel("Hari")
ax1.set_ylabel("Jumlah Penyewaan")
ax1.set_title("Perbedaan Penyewaan Sepeda pada Hari Kerja dan Hari Libur")
st.pyplot(fig1)

st.markdown("---")

# ----- LINEPLOT: Tren Penyewaan Sepeda Berdasarkan Jam -----
df_hourly_trend = main_df.groupby("hr")[["cnt"]].sum().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_hourly_trend, x="hr", y="cnt", marker="o", color="#4C72B0", ax=ax2)
ax2.set_xticks(range(0, 24))  # Pastikan semua jam (0-23) muncul
ax2.set_xlabel("Jam")
ax2.set_ylabel("Jumlah Penyewaan")
ax2.set_title("Tren Penyewaan Sepeda Berdasarkan Jam")
st.pyplot(fig2)

st.caption('Copyright (c), created by Tonsbray')

# ----- HIDE STREAMLIT STYLE -----
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

