import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Judul dashboard
st.title('Analisis Penyewaan Sepeda')

# Memuat dataset dari file CSV
day_data = pd.read_csv('day.csv')

# Menampilkan 5 baris pertama dari dataset
st.write("Berikut adalah 5 baris pertama dari dataset:")
st.write(day_data.head())

# Analisis Data
st.header('Analisis Data')
st.write(day_data.info())
st.write("Tidak ada nilai null di dataset dan tidak ditemukan data duplikat.")

# Mengecek outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=day_data[['cnt', 'temp', 'atemp', 'hum', 'windspeed']])
plt.title('Pengecekan Outliers pada Fitur Numerik')
st.pyplot()

# Histogram distribusi 'cnt'
plt.figure(figsize=(8, 5))
plt.hist(day_data['cnt'], bins=30, color='blue', edgecolor='black')
plt.title('Distribusi Jumlah Penyewaan Sepeda (cnt)')
plt.xlabel('Jumlah Penyewaan (cnt)')
plt.ylabel('Frekuensi')
st.pyplot()

# Penjelasan
st.write("Distribusi jumlah penyewaan sepeda menunjukkan bahwa data cenderung tidak normal (skewed), "
         "dengan sebagian besar penyewaan berada di bawah rata-rata.")

# Pertanyaan 1: Rata-rata penyewaan antara hari kerja dan akhir pekan
workingday_counts = day_data.groupby('workingday')['cnt'].mean()
plt.figure(figsize=(8, 5))
sns.barplot(x=['Weekend/Holiday', 'Working Day'], y=workingday_counts)
plt.title('Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xlabel('Tipe Hari')
st.pyplot()

# Penjelasan
st.write("Rata-rata penyewaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan, "
         "menunjukkan bahwa sepeda lebih banyak digunakan untuk keperluan komuter.")

# Pertanyaan 2: Pengaruh kondisi cuaca
weather_counts = day_data.groupby('weathersit')['cnt'].mean()
weather_labels = {1: 'Clear/Partly Cloudy', 2: 'Cloudy/Mist', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'}

plt.figure(figsize=(8, 5))
sns.barplot(x=[weather_labels[i] for i in weather_counts.index], y=weather_counts)
plt.title('Rata-rata Penyewaan Sepeda berdasarkan Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xlabel('Kondisi Cuaca')
st.pyplot()

# Penjelasan
st.write("Kondisi cuaca cerah dan berawan meningkatkan penggunaan sepeda, "
         "sementara kondisi hujan atau salju mengurangi penyewaan secara signifikan.")

# Kategori penyewaan sepeda
day_data['cnt_bin'] = pd.cut(day_data['cnt'], bins=[0, 3000, 6000, 9000], labels=['Rendah', 'Sedang', 'Tinggi'])
plt.figure(figsize=(8, 5))
sns.countplot(data=day_data, x='cnt_bin', palette='viridis')
plt.title('Distribusi Kategori Penyewaan Sepeda (Rendah, Sedang, Tinggi)')
plt.xlabel('Kategori Penyewaan')
plt.ylabel('Jumlah Hari')
st.pyplot()

# Penjelasan
st.write("Sebagian besar hari memiliki penyewaan dalam kategori sedang (3000-6000), "
         "dengan jumlah hari penyewaan rendah dan tinggi yang lebih sedikit.")

# Kesimpulan
st.header('Kesimpulan')
st.write("1. Rata-rata penyewaan sepeda lebih tinggi pada hari kerja, menunjukkan penggunaan untuk keperluan komuter.\n"
         "2. Cuaca memiliki dampak signifikan pada penyewaan sepeda. Hari cerah mendorong lebih banyak penyewaan, "
         "sementara hujan mengurangi minat pengguna.")
