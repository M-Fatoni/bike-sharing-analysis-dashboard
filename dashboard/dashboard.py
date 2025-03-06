# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 21:48:37 2025

@author: Tonsbray
"""

import streamlit as st # library membuat aplikasi web berbasis data
import pandas as pd # library mengolah dataframe

# Library visualisasi data
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df_hour = pd.read_csv("hour.csv")

# Sidebar navigation
st.sidebar.title("📊 Bike Sharing Dashboard")
option = st.sidebar.radio("Pilih Opsi:", [
    "Tujuan", "Peminjaman Berdasarkan Musim", "Pola Penyewaan Berdasarkan Waktu",
    "Perbedaan Penyewaan Hari Kerja vs Libur", "Dampak Kondisi Cuaca terhadap Penyewaan",
    "Kesimpulan dan Strategi Bisnis"])

# Halaman Tujuan
if option == "Tujuan":
    st.title("🚲 Analisis Penyewaan Sepeda")
    st.write("Dashboard ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan berbagai faktor seperti musim, waktu, hari kerja, dan kondisi cuaca. Dengan wawasan ini, bisnis dapat mengoptimalkan strategi operasional, termasuk penyesuaian harga, promosi musiman, dan alokasi sepeda secara lebih efisien.")

# Visualisasi: Peminjaman Sepeda Berdasarkan Musim
elif option == "Peminjaman Berdasarkan Musim":
    st.subheader("🍂 Peminjaman Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(6, 4))
    df_hour.groupby("season")["cnt"].mean().plot(kind="bar", color=["#66cc33", "#ffcc00", "#ff3300", "#02a5ff"], ax=ax)
    ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"], rotation=0)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Peminjaman")
    ax.set_title("Rata-rata Peminjaman Sepeda per Musim")
    st.pyplot(fig)
    st.markdown("""
                Peminjaman sepeda tertinggi terjadi pada musim gugur (Fall) dan terendah pada musim semi (Spring). 
                Hal ini menunjukkan bahwa musim gugur adalah waktu yang paling diminati untuk bersepeda, 
                sementara musim semi memiliki jumlah peminjaman paling sedikit, kemungkinan karena cuaca yang lebih basah atau kurang mendukung.
                """)

# Visualisasi: Pola Penyewaan Berdasarkan Waktu
elif option == "Pola Penyewaan Berdasarkan Waktu":
    st.subheader("⏰ Pola Penyewaan Sepeda Berdasarkan Jam")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='hr', y='cnt', data=df_hour, hue='workingday', ci=None, marker='o', ax=ax)
    ax.set_xticks(range(0, 24))
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewa")
    ax.set_title("Pola Penyewaan Sepeda Berdasarkan Jam")
    st.pyplot(fig)
    st.markdown("""
                Pada hari kerja, sepeda lebih banyak digunakan untuk perjalanan ke kantor atau sekolah, 
                sedangkan pada hari libur, pengguna cenderung bersepeda untuk aktivitas santai 
                di siang hingga sore hari.
                """)

# Visualisasi: Perbedaan Penyewaan Hari Kerja vs Libur
elif option == "Perbedaan Penyewaan Hari Kerja vs Libur":
    st.subheader("📅 Perbedaan Penyewaan Sepeda pada Hari Kerja dan Hari Libur")
    df_grouped = df_hour.groupby("workingday")[["registered", "casual"]].sum().reset_index()
    df_grouped["workingday"] = df_grouped["workingday"].map({1: "Hari Kerja", 0: "Hari Libur"})
    df_melted = df_grouped.melt(id_vars="workingday", var_name="User Type", value_name="Total Rentals")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df_melted, x="workingday", y="Total Rentals", hue="User Type", palette=["#6ee5c7", "#e56e8c"], ax=ax)
    ax.set_xlabel("Hari")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Perbedaan Penyewaan Sepeda pada Hari Kerja dan Hari Libur")
    st.pyplot(fig)
    st.markdown("""
                - Penyewaan sepeda lebih tinggi pada hari kerja karena mayoritas pengguna registered 
                menggunakan sepeda untuk keperluan transportasi harian.
                - Pada hari libur, jumlah pengguna casual meningkat, menunjukkan bahwa banyak orang 
                menggunakan sepeda untuk rekreasi atau aktivitas non-rutin.
                """)

# Visualisasi: Dampak Kondisi Cuaca terhadap Penyewaan
elif option == "Dampak Kondisi Cuaca terhadap Penyewaan":
    st.subheader("🌦️ Dampak Kondisi Cuaca terhadap Penyewaan Sepeda")
    weather_rentals = df_hour.groupby('weathersit')['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='weathersit', y='cnt', data=weather_rentals, palette=['#dfe2fe', '#b1cbfa', '#8e98f5', '#7971ea'], ax=ax)
    ax.set_xticklabels(["Clear", "Mist", "Light Rain", "Heavy Rain"], rotation=0)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Total Penyewaan Sepeda")
    ax.set_title("Dampak Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda")
    st.pyplot(fig)
    st.markdown("""
                Orang lebih nyaman bersepeda ketika cuaca mendukung.
                """)

# Halaman Kesimpulan dan Strategi Bisnis
elif option == "Kesimpulan dan Strategi Bisnis":
    st.title("📌 Kesimpulan dan Strategi Bisnis")
    st.write("**1. Musim Gugur memiliki peminjaman tertinggi, sementara Musim Semi memiliki yang terendah.**")
    st.write("**2. Puncak penyewaan terjadi pada jam 08:00 dan 17:00, mencerminkan keadaan jam kerja dan pulang kerja.**")
    st.write("**3. Hari kerja memiliki jumlah penyewaan lebih tinggi dibandingkan hari libur.**")
    st.write("**4. Cuaca buruk mengurangi jumlah penyewaan sepeda secara signifikan.**")
    st.subheader("💡 Rekomendasi Strategi Bisnis")
    st.write("📌 Meningkatkan promosi penyewaan sepeda saat musim semi untuk meningkatkan minat pelanggan.")
    st.write("📌 Menyediakan lebih banyak sepeda di pagi dan sore hari untuk memenuhi permintaan saat jam sibuk.")
    st.write("📌 Menawarkan diskon atau insentif bagi pengguna saat cuaca mendung atau hujan ringan.")

