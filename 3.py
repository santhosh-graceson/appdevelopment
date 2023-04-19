import json
import websocket
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import altair as alt

st.title("Real Time Data Streaming")
websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("wss://o7xkp9lilf.execute-api.ap-northeast-1.amazonaws.com/production")
def send_message(message):
    return ws.send(json.dumps(message))

df_Tidal_Volume = pd.DataFrame(columns=["time","Tidal_Volume"])
df_PEEP_Level = pd.DataFrame(columns=["time", "PEEP_Level"])

# Create empty line charts
chart_Tidal_Volume = st.empty()
chart_PEEP_Level = st.empty()

# Initialize the counter and time
counter = 0
start_time = datetime.now()
while True:
    try:
        message = ws.recv()        

        # Extract the values from the received data
        data = json.loads(message)

        # Get the current time
        time = datetime.now()
        last_update_time = start_time
        # Allocate the data to the corresponding parameter
        if counter < 10:
            df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": float(data)}, ignore_index=True)
        else:
            df_PEEP_Level = df_PEEP_Level.append({"time": time, "PEEP_Level": float(data)}, ignore_index=True)

        # Increment the counter
        counter = (counter + 1) % 20
        
        # Keep only the last 400 data points
        if len(df_Tidal_Volume) > 400:
            df_Tidal_Volume = df_Tidal_Volume.tail(400)
        if len(df_PEEP_Level) > 400:
            df_PEEP_Level = df_PEEP_Level.tail(400)

        # Update the line charts every 50 milliseconds for each parameter
        time_since_last_update = datetime.now() - last_update_time
        if time_since_last_update >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(100)).mark_line().encode(x='time', y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[-360, 360]))))
            chart_PEEP_Level.altair_chart(alt.Chart(df_PEEP_Level.tail(100)).mark_line().encode(x='time', y=alt.Y('PEEP_Level', scale=alt.Scale(domain=[-6, 6]))))
            last_update_time = datetime.now()

    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break
