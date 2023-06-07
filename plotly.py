import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time as t
import math

st.title("Plotly plotting")
df_Tidal_Volume = pd.DataFrame(columns=["time", "Tidal_Volume"])
time = datetime.now()

# Create an empty figure
fig = px.line()

while True:
    try:
        data = [1,2,3,4,5,6,7,8,9,10]

        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[0]}, ignore_index=True)
        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[1]}, ignore_index=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[2]}, ignore_index=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[3]}, ignore_index=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[4]}, ignore_index=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[5]}, ignore_index=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[6]}, ignore_index=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[7]}, ignore_index=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[8]}, ignore_index=True)

        t.sleep(0.05)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[9]}, ignore_index=True)

        t.sleep(0.05)

        # Update the figure with the new data
        fig = px.line(df_Tidal_Volume, x="time", y="Tidal_Volume")

        # Display the figure using Streamlit
        st.plotly_chart(fig)
    except:
        st.write("No data to plot")
        break
