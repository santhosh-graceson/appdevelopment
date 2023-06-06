import streamlit as st
import pandas as pd
from datetime import datetime   
import time as t  
import math                               
st.title("Dataframe")
df_Tidal_Volume = pd.DataFrame(columns=["time","Tidal_Volume"])
time = datetime.now()

while True:
    try:
        data = [5*math.sin(math.radians(0)),5*math.sin(math.radians(9)),5*math.sin(math.radians(13.5)),5*math.sin(math.radians(18)),5*math.sin(math.radians(22.5)),5*math.sin(math.radians(27)),5*math.sin(math.radians(31.5)),5*math.sin(math.radians(36)),5*math.sin(math.radians(40.5)),5*math.sin(math.radians(45))]
   
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[0]}, ignore_index=True)
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[1]}, ignore_index=True)
        
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[2]}, ignore_index=True)
        
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[3]}, ignore_index=True)
        
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[4]}, ignore_index=True)
        
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[5]}, ignore_index=True)
        
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[6]}, ignore_index=True)
        
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[7]}, ignore_index=True)
        
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[8]}, ignore_index=True)
        
        t.sleep(1)
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[9]}, ignore_index=True)
        
        t.sleep(1)
        
        st.write(df_Tidal_Volume)
    except:
        st.write("No data to plot")
        break   