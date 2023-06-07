import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from datetime import datetime
import time as t

st.title("Plotting of Data")
df_Tidal_Volume = pd.DataFrame(columns=["time", "Tidal_Volume"])

# Create an empty placeholder for the plot
st.write("Plotting using plotly chart")
plot_placeholder = st.empty()
st.write("Plotting using altair chart")
chart_Tidal_Volume = st.empty()

while True:
    try:
        time = datetime.now()
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Append new data to the DataFrame
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[0]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[1]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[2]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[3]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[4]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[5]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[6]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[7]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[8]}, ignore_index=True)
        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[9]}, ignore_index=True)
        t.sleep(0.05)

        # Update the plot with the new data
        fig = px.line(df_Tidal_Volume.tail(200), x="time", y="Tidal_Volume")

        # Update the placeholder with the new plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume')),use_container_width=True)
    except Exception as e:
        st.write("An error occurred:", e)
        break
