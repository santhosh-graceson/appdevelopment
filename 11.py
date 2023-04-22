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
@st.cache_data
def send_message(message):
    return ws.send(json.dumps(message))
df_Tidal_Volume = pd.DataFrame(columns=["time","Tidal_Volume"])
chart_Tidal_Volume = st.empty()
Tidal_Volume = []
start_time = datetime.now()
while True:
    try:
        message = ws.recv()        
        data = json.loads(message)
        time = datetime.now()
        df_Tidal_Volume = df_Tidal_Volume.append({"time": time, "Tidal_Volume": int(data)}, ignore_index=True)
        last_update_time = start_time
        time_since_last_update = time - last_update_time
        if time_since_last_update >= timedelta(milliseconds=50):
            chart_Tidal_Volume.altair_chart(alt.Chart(df_Tidal_Volume.tail(80)).mark_line().encode(x='time',y=alt.Y('Tidal_Volume', scale=alt.Scale(domain=[0,3]))))
        start_time = time
    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break

