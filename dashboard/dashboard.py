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

# Create helper functions
def create_seasonly_users_df(df):
    seasonly_users_df = df.groupby("season").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    seasonly_users_df = seasonly_users_df.reset_index()
    seasonly_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    seasonly_users_df = pd.melt(seasonly_users_df,
                                id_vars=['season'],
                                value_vars=['casual_rides', 'registered_rides'],
                                var_name='type_of_rides',
                                value_name='count_rides')
    
    seasonly_users_df['season'] = pd.Categorical(seasonly_users_df['season'],
                                                 categories=['Spring', 'Summer', 'Fall', 'Winter'])
    
    seasonly_users_df = seasonly_users_df.sort_values('season')
    
    return seasonly_users_df

def create_weekday_users_df(df):
    weekday_users_df = df.groupby("weekday").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    weekday_users_df = weekday_users_df.reset_index()
    weekday_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    weekday_users_df = pd.melt(weekday_users_df,
                               id_vars=['weekday'],
                               value_vars=['casual_rides', 'registered_rides'],
                               var_name='type_of_rides',
                               value_name='count_rides')
    
    weekday_users_df['weekday'] = pd.Categorical(weekday_users_df['weekday'],
                                                 categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    weekday_users_df = weekday_users_df.sort_values('weekday')
    
    return weekday_users_df

# Sidebar filter
with st.sidebar:
    st.sidebar.header("Filter:")
    min_date = df_hour["dteday"].min()
    max_date = df_hour["dteday"].max()
    start_date, end_date = st.date_input("Date Filter", min_value=min_date, max_value=max_date, value=[min_date, max_date])

# Filter data
main_df = df_hour[(df_hour["dteday"] >= str(start_date)) & (df_hour["dteday"] <= str(end_date))]

# Assign main_df ke helper functions
seasonly_users_df = create_seasonly_users_df(main_df)
weekday_users_df = create_weekday_users_df(main_df)

# Main Page
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

# Bar charts
fig1, ax1 = plt.subplots()
sns.barplot(data=seasonly_users_df, x='season', y='count_rides', hue='type_of_rides', ax=ax1)
ax1.set_title("Count of bikeshare rides by season")
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.barplot(data=weekday_users_df, x='weekday', y='count_rides', hue='type_of_rides', ax=ax2)
ax2.set_title("Count of bikeshare rides by weekday")
st.pyplot(fig2)

st.caption("Copyright (c)")


