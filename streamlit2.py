import streamlit as st
import websocket
import json
import pandas as pd
import plotly.express as px
import altair as alt
from datetime import datetime
import time as t

st.title("Plotting of Data")
#Websocket connection establishment
websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("wss://i7kggwivc5.execute-api.us-west-2.amazonaws.com/production")
df_Inspiration_Flow = pd.DataFrame(columns=["Units","Inspiration_Flow"])
a=[]
n=0

# df_Tidal_Volume = pd.DataFrame(columns=["time", "Tidal_Volume"])

# Create an empty placeholder for the plot
st.write("Plotting using plotly chart")
plot_placeholder = st.empty()
st.write("Plotting using altair chart")
chart_Tidal_Volume = st.empty()
counter=0

while True:
    try:
        #Receiving value through websocket
        message = ws.recv()
        data = json.loads(message)

        if n<=200:
            if counter<9:
                a.append(data)
                counter=counter+1
            elif counter==9:
                counter = 0
                a.append(data)



                for i in range(10):
                    
                    # Append new data to the DataFrame
                    df_Inspiration_Flow = df_Inspiration_Flow.append({"Units":n+i, "Inspiration_Flow": a[i]}, ignore_index=True)

                    # Update the plot with the new data
                    fig = px.line(df_Inspiration_Flow.tail(200), x="Units", y="Inspiration_Flow")

                    # Update the placeholder with the new plot
                    plot_placeholder.plotly_chart(fig, use_container_width=True)
                    chart_Tidal_Volume.altair_chart(alt.Chart(df_Inspiration_Flow.tail(200)).mark_line().encode(x='Units',y=alt.Y('Inspiration_Flow')),use_container_width=True)

                a.clear()
                n=n+10
        elif n>200:
            n=1 
        else:
            print("Data not received")
    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break