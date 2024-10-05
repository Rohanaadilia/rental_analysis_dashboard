import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Memuat dataset dari file CSV
day_data = pd.read_csv('day.csv')
day_data['dteday'] = pd.to_datetime(day_data['dteday'])  # Mengonversi dteday menjadi datetime

# Menghapus kolom yang tidak relevan
day_data.drop(columns=['instant'], inplace=True)

# Menampilkan judul dashboard
st.title("Analisis Penyewaan Sepeda")

# --- Analisis Pertanyaan 1: Hari Kerja vs Akhir Pekan ---
st.header("Pertanyaan 1: Bagaimana perbedaan jumlah penyewaan sepeda antara hari kerja dan akhir pekan?")
workingday_counts = day_data.groupby('workingday')['cnt'].mean()

# Membuat grafik
plt.figure(figsize=(8, 5))
sns.barplot(x=['Weekend/Holiday', 'Working Day'], y=workingday_counts)
plt.title('Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xlabel('Tipe Hari')

# Menampilkan grafik di Streamlit
st.pyplot(plt)

# Menambahkan penjelasan untuk grafik
st.write("""
Rata-rata penyewaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan. 
Hal ini mengindikasikan bahwa penggunaan sepeda lebih sering digunakan untuk keperluan komuter daripada rekreasi. 
Rekomendasi: Pihak penyedia sepeda bisa meningkatkan layanan atau promosi yang lebih menarik di akhir pekan untuk menarik pengguna yang lebih banyak.
""")

# --- Analisis Pertanyaan 2: Pengaruh Cuaca ---
st.header("Pertanyaan 2: Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?")
weather_counts = day_data.groupby('weathersit')['cnt'].mean()

# Membuat grafik
weather_labels = {1: 'Clear/Partly Cloudy', 2: 'Cloudy/Mist', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'}

plt.figure(figsize=(8, 5))
sns.barplot(x=[weather_labels[i] for i in weather_counts.index], y=weather_counts)
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xlabel('Kondisi Cuaca')

# Menampilkan grafik di Streamlit
st.pyplot(plt)

# Menambahkan penjelasan untuk grafik
st.write("""
Cuaca memiliki dampak besar pada penyewaan sepeda. 
Pada hari-hari dengan cuaca cerah atau berawan, pengguna lebih cenderung menyewa sepeda, sedangkan cuaca buruk mengurangi penyewaan secara signifikan. 
Rekomendasi: Layanan penyewaan sepeda bisa mempertimbangkan untuk memberikan diskon atau promosi khusus pada hari-hari dengan cuaca buruk untuk mengurangi dampak negatif dari cuaca.
""")

# --- Analisis Lanjutan: Kategori Penyewaan ---
st.header("Analisis Lanjutan: Kategori Penyewaan Sepeda")
day_data['cnt_bin'] = pd.cut(day_data['cnt'], bins=[0, 3000, 6000, 9000], labels=['Rendah', 'Sedang', 'Tinggi'])

# Membuat grafik
plt.figure(figsize=(8, 5))
sns.countplot(data=day_data, x='cnt_bin', palette='viridis')
plt.title('Distribusi Kategori Penyewaan Sepeda (Rendah, Sedang, Tinggi)')
plt.xlabel('Kategori Penyewaan')
plt.ylabel('Jumlah Hari')

# Menampilkan grafik di Streamlit
st.pyplot(plt)

# Menambahkan penjelasan untuk grafik
st.write("""
Dari hasil clustering, kita bisa melihat bahwa sebagian besar hari memiliki penyewaan dalam kategori medium (sedang), yaitu antara 3000-6000 penyewaan per hari. 
Penyewaan rendah terjadi pada sejumlah kecil hari, yang mungkin disebabkan oleh kondisi cuaca buruk atau hari libur. 
Penyewaan tinggi menunjukkan adanya lonjakan penyewaan, kemungkinan karena event khusus atau kondisi cuaca yang sangat mendukung.
""")
