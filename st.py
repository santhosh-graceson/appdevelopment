import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import altair as alt
import time as t      
import math            
st.set_page_config(layout ="wide")                   
st.title("Sine wave Plotting")
st.write("The following graph is plotting sine wave from 0 to Pi in every 2 seconds, with 2 two seconds break")
df_Tidal_Volume = pd.DataFrame(columns=["time","Tidal_Volume"])
chart_Tidal_Volume = st.empty()
start_time = datetime.now()
a,null =st.columns([99,1])

while True:
    try:
        data = [5*math.sin(math.radians(0)),5*math.sin(math.radians(9)),5*math.sin(math.radians(13.5)),5*math.sin(math.radians(18)),5*math.sin(math.radians(22.5)),5*math.sin(math.radians(27)),5*math.sin(math.radians(31.5)),5*math.sin(math.radians(36)),5*math.sin(math.radians(40.5)),5*math.sin(math.radians(45))] 
        data1 = [5*math.sin(math.radians(49.5)),5*math.sin(math.radians(54)),5*math.sin(math.radians(58.5)),5*math.sin(math.radians(63)),5*math.sin(math.radians(67.5)),5*math.sin(math.radians(72)),5*math.sin(math.radians(76.5)),5*math.sin(math.radians(81)),5*math.sin(math.radians(85.5)),5*math.sin(math.radians(90))] 
        data2=[5*math.sin(math.radians(94.5)),5*math.sin(math.radians(99)),5*math.sin(math.radians(103.5)),5*math.sin(math.radians(108)),5*math.sin(math.radians(112.5)),5*math.sin(math.radians(117)),5*math.sin(math.radians(121.5)),5*math.sin(math.radians(126)),5*math.sin(math.radians(130.5)),5*math.sin(math.radians(135))]
        data3=[5*math.sin(math.radians(139.5)),5*math.sin(math.radians(144)),5*math.sin(math.radians(148.5)),5*math.sin(math.radians(153)),5*math.sin(math.radians(157.5)),5*math.sin(math.radians(162)),5*math.sin(math.radians(166.5)),5*math.sin(math.radians(171)),5*math.sin(math.radians(175.5)),5*math.sin(math.radians(180))]
        data4=[0,0,0,0,0,0,0,0,0,0]
        data5=[0,0,0,0,0,0,0,0,0,0]
        data6=[0,0,0,0,0,0,0,0,0,0]
        data7=[0,0,0,0,0,0,0,0,0,0]
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[0]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            a= chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[1]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[2]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[3]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[4]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[5]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not plotted")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[6]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[7]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[8]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data[9]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received") 
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[0]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[1]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[2]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[3]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[4]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[5]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[6]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[7]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[8]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data1[9]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[0]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[1]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[2]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[3]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[4]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[5]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[6]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[7]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[8]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data2[9]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[0]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[1]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[2]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[3]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[4]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[5]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[6]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[7]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[8]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data3[9]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[0]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[1]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[2]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[3]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[4]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[5]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not plotted")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[6]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[7]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[8]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data4[9]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received") 
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[0]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[1]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[2]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[3]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[4]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[5]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[6]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[7]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[8]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        t.sleep(0.03)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data5[9]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[0]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[1]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[2]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[3]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[4]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[5]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[6]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[7]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[8]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data6[9]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[0]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[1]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[2]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[3]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[4]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[5]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[6]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[7]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[8]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": data7[9]}, ignore_index=True)
        latest_time = time - start_time
        if latest_time >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(200)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,6]))))
            print("Plot Success")
        else:
            print("Data not received")
        
        # t.sleep(1)
        start_time = time
    except:
        st.write("No data to plot")
        break   