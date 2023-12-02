# -*- coding: utf-8 -*-
"""Proyek Data Analis Dicoding

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19R0ygfgUMw2GUQtjglYS_p8z7lvK8LQl

# Proyek Analisis Data: Nama dataset

*   Nama : Ammar
*   Email : ammarmar592@gmail.com
*   Id Dicoding : ammar_mar_ra9h

# Pertanyaan Bisnis

*   Bagaimana hubungan antara musim dan jumlah sewa sepeda harian ?
*   Apakah ada pola berdasarkan waktu (bulan, jam)dalam jumlah sewa sepeda harian?
*   Bagaimana pengaruh cuaca (weathersit) terhadap jumlah sewa sepeda harian?
*   Apakah ada perbedaan antara hari kerja (workingday) dan hari libur (holiday) dalam jumlah sewa sepeda harian?

# Menyiapkan Semua Library yang dibutuhkan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import streamlit as st

warnings.filterwarnings("ignore")


"""# Exploratory Data Analysis (EDA)

Menggabungkan kedua tabel
"""


bike_sharing = pd.read_csv("bike_sharing_data.csv")
st.dataframe(bike_sharing)


"""# Visualization dan Explanatory Analysis

1. Bagaimana hubungan antara musim dan jumlah sewa sepeda harian ?
"""
bymusim = bike_sharing.groupby(by="season_daily").cnt_daily.nunique().reset_index()
bymusim.rename(columns={"cnt_daily": "count_daily"}, inplace=True)
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
fig, ax = plt.subplots(figsize=(7, 7))

sns.barplot(
    y="count_daily",
    x="season_daily",
    data=bymusim.sort_values(by="count_daily", ascending=False),
    palette=colors,
)

plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Musim")
plt.xlabel("Musim")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.show()
st.pyplot(fig)

"""Pada Diagram diatas dapat kita simpulkan bahwa rental sepeda paling banyak ketika musim fall(musim gugur) dan jumlah rental sepeda paling sedikit yaitu pada musim winter(musim dingin)

2. Bagaimana Pengaruh cuaca dengan jumlah rental sepeda harian ?
"""
byweathersit = (
    bike_sharing.groupby(by="weathersit_daily").cnt_daily.nunique().reset_index()
)
byweathersit.rename(columns={"cnt_daily": "count_daily"}, inplace=True)
fig, ax = plt.subplots(figsize=(7, 7))
sns.barplot(
    y="count_daily",
    x="weathersit_daily",
    data=byweathersit.sort_values(by="count_daily", ascending=False),
    palette=colors,
)
plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Cuaca")
plt.xlabel("Cuaca")
plt.ylabel("Jumlah Sewa Sepeda Harian")
st.pyplot(fig)

"""Pada Diagram diatas dapat kita simpulkan bahwasanya jumlah rental sepeda paling banyak yaitu ketika cuaca Clear(cerah) dan jumlah rental sepeda yang paling sedikit ketika cuaca Light Rainsow(Hujan ringan)

3. Bagaimana Hubungan Antara Hari Kerja terhadap Rental Sepeda ?
"""

byworkingday = (
    bike_sharing.groupby(by="workingday_daily").cnt_daily.nunique().reset_index()
)
byworkingday.rename(columns={"cnt_daily": "count_daily"}, inplace=True)
fig, ax = plt.subplots(figsize=(7, 7))
colors = ["#72BCD4", "#D3D3D3"]

sns.barplot(
    y="count_daily",
    x="workingday_daily",
    data=byworkingday.sort_values(by="count_daily", ascending=False),
    palette=colors,
)

plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Hari Kerja")
plt.xlabel("Hari Kerja")
plt.ylabel("Jumlah Sewa Sepeda Harian")
st.pyplot(fig)

"""Pada Diagram diatas dapat kita simpulkan bahwa jumlah rental sepeda ketika hari kerja lebih banyak daripada jumlah rental sepeda pada hari libur.

4. Bagaimana perbandingan jumlah rental sepeda tahun 2011 dan 2012?
"""
byyear = bike_sharing.groupby(by="yr_daily").cnt_daily.nunique().reset_index()
byyear.rename(columns={"cnt_daily": "count_daily"}, inplace=True)
fig, ax = plt.subplots(figsize=(5, 7))

colors = ["#D3D3D3", "#72BCD4"]
sns.barplot(
    y="count_daily",
    x="yr_daily",
    data=byyear.sort_values(by="count_daily", ascending=False),
    palette=colors,
)

plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Tahun")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Sewa Sepeda Harian")
st.pyplot(fig)

"""Dari Gambar diatas dapat kita simpulkan bahwa jumlah rental sepeda paling banyak pada tahun 2012

"""

bike_sharing.to_csv("bike_sharing_data.csv", index=False)
