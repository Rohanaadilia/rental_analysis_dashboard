import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set tema
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", layout="wide")

# Judul Dashboard yang diratakan di tengah dengan gaya menarik
st.markdown("""
    <h1 style='text-align: center; 
                color: #FF6347; 
                font-family: "Arial", sans-serif; 
                font-size: 48px; 
                text-shadow: 3px 3px 2px rgba(0, 0, 0, 0.4);
                background: linear-gradient(to right, #FF6347, #FFD700); 
                -webkit-background-clip: text; 
                -webkit-text-fill-color: transparent;'>Dashboard Penyewaan Sepeda</h1>
""", unsafe_allow_html=True)

# Menampilkan gambar
st.image('dashboard/picture.jpg', use_column_width=True)

# Memuat data
day_data = pd.read_csv('dashboard/day.csv')


# Menampilkan data di container terpisah
st.subheader("Data Penyewaan Sepeda:")
st.dataframe(day_data.head())  # Menggunakan st.dataframe untuk tampilan interaktif

# Membuat histogram untuk kolom 'cnt'
st.subheader("Distribusi Jumlah Penyewaan Sepeda:")
plt.figure(figsize=(10, 6))
sns.histplot(day_data['cnt'], bins=30, kde=True)
plt.title('Distribusi Jumlah Penyewaan Sepeda', fontsize=18)
plt.xlabel('Jumlah Penyewaan', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
st.pyplot(plt)  # Menggunakan st.pyplot untuk menampilkan plot

# Mengelompokkan data berdasarkan hari kerja untuk mendapatkan rata-rata
workingday_counts = day_data.groupby('workingday')['cnt'].mean()

# Membuat bar chart untuk Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan
st.subheader("Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
plt.figure(figsize=(8, 5))
sns.barplot(x=['Weekend/Holiday', 'Working Day'], y=workingday_counts, palette='coolwarm')
plt.title('Average Bike Rentals: Working Day vs Weekend/Holiday', fontsize=18)
plt.ylabel('Average Count of Rentals', fontsize=14)
plt.xlabel('Day Type', fontsize=14)
st.pyplot(plt)  # Menampilkan bar chart di Streamlit

# Mengelompokkan data berdasarkan situasi cuaca untuk mendapatkan rata-rata
weather_counts = day_data.groupby('weathersit')['cnt'].mean()

# Membuat bar chart untuk Penyewaan Sepeda Berdasarkan Cuaca
st.subheader("Penyewaan Sepeda Berdasarkan Cuaca")
weather_labels = {1: 'Clear/Partly Cloudy', 2: 'Cloudy/Mist', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'}

plt.figure(figsize=(8, 5))
sns.barplot(x=[weather_labels[i] for i in weather_counts.index], y=weather_counts, palette='pastel')
plt.title('Average Bike Rentals by Weather Condition', fontsize=18)
plt.ylabel('Average Count of Rentals', fontsize=14)
plt.xlabel('Weather Condition', fontsize=14)
st.pyplot(plt)  # Menampilkan bar chart di Streamlit

# Membuat kategori penyewaan sepeda berdasarkan jumlahnya (low, medium, high)
day_data['cnt_bin'] = pd.cut(day_data['cnt'], bins=[0, 3000, 6000, 9000], labels=['Low', 'Medium', 'High'])

# Visualisasi distribusi kategori penyewaan sepeda
st.subheader("Distribusi Kategori Penyewaan Sepeda (Low, Medium, High)")
plt.figure(figsize=(8, 5))
sns.countplot(data=day_data, x='cnt_bin', palette='viridis')
plt.title('Distribusi Kategori Penyewaan Sepeda (Low, Medium, High)', fontsize=18)
plt.xlabel('Kategori Penyewaan', fontsize=14)
plt.ylabel('Jumlah Hari', fontsize=14)
st.pyplot(plt)  # Menampilkan plot di Streamlit

# Menampilkan insight singkat di bawah visualisasi
st.write("### Insight:")
st.write("- Penyewaan lebih tinggi pada hari kerja dibandingkan akhir pekan.")
st.write("- Cuaca cerah meningkatkan penyewaan sepeda.")
# Cek distribusi kategori penyewaan sepeda
st.write("Distribusi Kategori Penyewaan Sepeda:")
st.write(day_data['cnt_bin'].value_counts())
