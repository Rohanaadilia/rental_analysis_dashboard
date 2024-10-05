# Dashboard Penyewaan Sepeda

Proyek ini adalah sebuah **Streamlit Dashboard** yang menampilkan analisis data penyewaan sepeda. Dashboard ini menyajikan beberapa visualisasi terkait jumlah penyewaan sepeda harian berdasarkan cuaca, hari kerja, serta kategori jumlah penyewaan. Dengan ini, pengguna dapat melihat tren dan pola dalam penyewaan sepeda serta mendapatkan insight terkait faktor-faktor yang mempengaruhi penyewaan sepeda.

## Fitur Utama

- **Distribusi Penyewaan Sepeda**: Menampilkan histogram jumlah penyewaan sepeda harian.
- **Perbandingan Penyewaan Hari Kerja vs Akhir Pekan**: Menampilkan bar chart rata-rata penyewaan pada hari kerja dan akhir pekan.
- **Penyewaan Berdasarkan Cuaca**: Menampilkan rata-rata penyewaan berdasarkan kondisi cuaca (cerah, mendung, hujan ringan, dsb.).
- **Kategori Penyewaan**: Menampilkan distribusi penyewaan sepeda dalam tiga kategori: Low, Medium, dan High.

## Instalasi

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

### 1. Clone Repository

Clone repository atau unduh file proyek:

```bash
git clone https://github.com/Rohanaadilia/rental_analysis_dashboard.git
```

### 2. Buat Virtual Environment (Opsional)

Sebaiknya membuat virtual environment agar pengelolaan dependensi lebih rapi:

```bash
python -m venv env
source env/bin/activate  # Untuk pengguna MacOS/Linux
env\Scripts\activate  # Untuk pengguna Windows
```

**Catatan**: Jangan tambahkan folder `env` ke dalam repository Git.

### 3. Install Dependensi

Instal library yang diperlukan menggunakan `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Jalankan Streamlit

Setelah semua dependensi diinstal, jalankan dashboard dengan perintah:

```bash
streamlit run rental_analysis_dashboard.py
```

Dashboard akan terbuka di browser pada `localhost:8501`.

## Struktur Proyek

Berikut adalah struktur direktori proyek ini:

```
Submission/
│
├── dashboard/
│   ├── day.csv                # Dataset yang digunakan dalam analisis
│   ├── picture.jpg            # Gambar yang ditampilkan di dashboard
│   └── rental_analysis_dashboard.py # Kode utama untuk Streamlit Dashboard
├── data/
│   └── day.csv                # Backup atau salinan dataset (opsional)
├── Proyek Analisis Data.ipynb # Notebook untuk eksplorasi dataset
├── README.md                  # Dokumentasi proyek ini
├── rental_analysis_dashboard.py # Alternatif script utama (di luar folder dashboard)
├── requirements.txt           # File untuk instalasi dependensi
└── url.txt                    # Informasi URL terkait
```

## Dataset

Dataset yang digunakan untuk analisis adalah **Bike Sharing Dataset**. Dataset ini memuat informasi harian terkait penyewaan sepeda dengan berbagai atribut seperti kondisi cuaca, jumlah hari kerja, dan lainnya.

## Penggunaan

1. Lihat distribusi penyewaan sepeda harian dengan histogram yang menunjukkan seberapa sering sepeda disewa setiap hari.
2. Bandingkan rata-rata penyewaan sepeda pada hari kerja dan akhir pekan.
3. Analisis bagaimana kondisi cuaca memengaruhi jumlah penyewaan sepeda.
4. Lihat distribusi penyewaan sepeda berdasarkan kategori (Low, Medium, High).
