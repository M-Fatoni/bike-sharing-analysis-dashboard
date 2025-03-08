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

df_hour['year'] = df_hour['dteday'].dt.year  # Tambahkan kolom tahun untuk analisis tren

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

# ----- LINEPLOT Tren Penyewaan Sepeda dari Tahun ke Tahun -----
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=df_hour.groupby('year')['cnt'].sum().reset_index(), x='year', y='cnt', marker='o', ax=ax)
ax.set_title("Tren Penyewaan Sepeda dari Tahun ke Tahun")
ax.set_xlabel("Tahun")
ax.set_ylabel("Total Rides")
st.pyplot(fig)

# ----- LINEPLOT Tren Penyewaan Sepeda berdasarkan Jam -----
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=main_df.groupby('hr')['cnt'].mean().reset_index(), x='hr', y='cnt', marker='o', ax=ax)
ax.set_title("Tren Penyewaan Sepeda berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Total Penyewaan")
ax.set_xticks(range(24))  # Menampilkan semua jam dari 0-23
st.pyplot(fig)

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
