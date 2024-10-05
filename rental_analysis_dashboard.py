import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_data = pd.read_csv('day.csv')
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Header
st.title('Bike Rental Analysis Dashboard')

# Section: Data Wrangling
st.subheader('Data Wrangling')
st.write("The dataset contains daily bike rental information with features like date, season, weather conditions, and more.")

# Plotting distribution of bike rentals
st.subheader('Distribution of Bike Rentals')
plt.figure(figsize=(10, 6))
sns.histplot(day_data['cnt'], bins=30, kde=True)
plt.title('Distribusi Jumlah Penyewaan Sepeda')
plt.xlabel('Jumlah Penyewaan')
plt.ylabel('Frekuensi')
st.pyplot()

st.write("The histogram shows the distribution of bike rentals, indicating that the data is skewed to the right, with most rentals being below the average.")

# Average Rentals on Working Days vs. Weekends
st.subheader('Average Rentals: Working Day vs Weekend/Holiday')
workingday_counts = day_data.groupby('workingday')['cnt'].mean()

plt.figure(figsize=(8, 5))
sns.barplot(x=['Weekend/Holiday', 'Working Day'], y=workingday_counts)
plt.title('Average Bike Rentals: Working Day vs Weekend/Holiday')
plt.ylabel('Average Count of Rentals')
plt.xlabel('Day Type')
st.pyplot()

st.write("The bar chart illustrates that average bike rentals are higher on working days (4500) compared to weekends (4300), suggesting more usage for commuting purposes.")

# Average Rentals by Weather Condition
st.subheader('Average Rentals by Weather Condition')
weather_counts = day_data.groupby('weathersit')['cnt'].mean()
weather_labels = {1: 'Clear/Partly Cloudy', 2: 'Cloudy/Mist', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'}

plt.figure(figsize=(8, 5))
sns.barplot(x=[weather_labels[i] for i in weather_counts.index], y=weather_counts)
plt.title('Average Bike Rentals by Weather Condition')
plt.ylabel('Average Count of Rentals')
plt.xlabel('Weather Condition')
st.pyplot()

st.write("This chart indicates that clear and partly cloudy weather (5000+ rentals) leads to higher bike usage, while rainy conditions significantly reduce rentals.")

# Bike Rentals Category Distribution
st.subheader('Bike Rentals Category Distribution')
day_data['cnt_bin'] = pd.cut(day_data['cnt'], bins=[0, 3000, 6000, 9000], labels=['Low', 'Medium', 'High'])

plt.figure(figsize=(8, 5))
sns.countplot(data=day_data, x='cnt_bin', palette='viridis')
plt.title('Distribusi Kategori Penyewaan Sepeda (Low, Medium, High)')
plt.xlabel('Kategori Penyewaan')
plt.ylabel('Jumlah Hari')
st.pyplot()

st.write("The count plot shows that most days fall into the 'Medium' rental category (3000-6000 rentals), while 'Low' rentals occur less frequently.")

# Conclusion Section
st.subheader('Conclusions')
st.write("""
1. **Working Days vs Weekends**: Average bike rentals are higher on working days, indicating a trend towards commuter usage. 
   *Recommendation*: Enhance promotions for weekends to attract more users.
   
2. **Weather Impact**: Weather significantly affects rental rates, with good weather increasing usage. 
   *Recommendation*: Consider offering discounts on rainy days to mitigate rental declines.
""")
