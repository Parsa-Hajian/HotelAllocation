import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#import result data
report_df = pd.read_csv('report_df.csv')

# Correct strategy names
report_df = report_df.reset_index()
report_df.rename(columns={"index": "Strategy"}, inplace=True)
report_df["Strategy"] = ["Random", "Customer Preference", "Price-Based", "Availability-Based"]

# Title
st.title("Visualizations for Hotel Allocation Strategies")

# Dataset Preview
st.subheader("Dataset Preview")
st.write(report_df)

# 1. Line Plot for Total Revenue
st.subheader("1. Line Plot: Total Revenue")
fig1, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(report_df["Strategy"], report_df["Total Revenue"], marker="o", color="blue", label="Total Revenue")
ax1.set_ylim(639000, 644000)
ax1.set_title("Total Revenue by Strategy", fontsize=16)
ax1.set_ylabel("Total Revenue", fontsize=12)
ax1.set_xlabel("Strategy", fontsize=12)
ax1.set_xticks(range(len(report_df["Strategy"])))
ax1.set_xticklabels(report_df["Strategy"], rotation=45)
ax1.legend()
st.pyplot(fig1)

# 2. Pie Chart for Average Satisfaction
st.subheader("2. Pie Chart: Average Satisfaction")
fig2, ax2 = plt.subplots(figsize=(8, 8))

ax2.pie(
    report_df["Average Satisfaction"],
    labels=report_df["Strategy"],
    autopct="%1.1f%%",
    colors=["gold", "lightblue", "lightcoral", "lightgreen"],
    startangle=140,
)
ax2.set_title("Average Satisfaction by Strategy", fontsize=16)
st.pyplot(fig2)

# 3. Bar Plot for Rooms Occupied
st.subheader("3. Bar Plot: Rooms Occupied")
fig3, ax3 = plt.subplots(figsize=(10, 6))

ax3.bar(report_df["Strategy"], report_df["Rooms Occupied"], color="lightseagreen")
ax3.set_ylim(3970, 4020)
ax3.set_title("Rooms Occupied by Strategy", fontsize=16)
ax3.set_ylabel("Rooms Occupied", fontsize=12)
ax3.set_xlabel("Strategy", fontsize=12)
ax3.set_xticks(range(len(report_df["Strategy"])))
ax3.set_xticklabels(report_df["Strategy"], rotation=45)
st.pyplot(fig3)
