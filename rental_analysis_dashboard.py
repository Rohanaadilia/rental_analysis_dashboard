import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
day_data = pd.read_csv('day.csv')
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Function to create bar chart for working days vs weekends
def plot_working_days():
    workingday_counts = day_data.groupby('workingday')['cnt'].mean()
    
    # Create bar chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x=['Weekend/Holiday', 'Working Day'], y=workingday_counts)
    plt.title('Average Bike Rentals: Working Day vs Weekend/Holiday')
    plt.ylabel('Average Count of Rentals')
    plt.xlabel('Day Type')
    st.pyplot()

    # Add explanation
    st.write("""
    ### Insights:
    Rata-rata penyewaan sepeda lebih tinggi pada hari kerja (4500) dibandingkan akhir pekan (4300).
    Ini menunjukkan bahwa sepeda lebih banyak digunakan untuk keperluan komuter daripada rekreasi.
    Untuk menarik lebih banyak pengguna di akhir pekan, penyedia layanan dapat mempertimbangkan 
    untuk menawarkan promosi khusus atau meningkatkan layanan.
    """)

# Function to create bar chart for weather conditions
def plot_weather_conditions():
    weather_counts = day_data.groupby('weathersit')['cnt'].mean()
    
    weather_labels = {1: 'Clear/Partly Cloudy', 2: 'Cloudy/Mist', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'}
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=[weather_labels[i] for i in weather_counts.index], y=weather_counts)
    plt.title('Average Bike Rentals by Weather Condition')
    plt.ylabel('Average Count of Rentals')
    plt.xlabel('Weather Condition')
    st.pyplot()

    # Add explanation
    st.write("""
    ### Insights:
    Cuaca cerah dan berawan meningkatkan penggunaan sepeda, dengan lebih dari 5000 penyewaan.
    Sementara itu, kondisi hujan atau salju ringan mengurangi penyewaan secara signifikan (~2000).
    Hal ini menunjukkan ketergantungan tinggi pada kondisi cuaca yang baik. 
    """)

# Streamlit app layout
st.title("Bike Sharing Data Analysis")
st.header("Analysis of Bike Rentals")

plot_working_days()
plot_weather_conditions()
