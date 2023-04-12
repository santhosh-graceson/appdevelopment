import json
import websocket
import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

st.title("Real Time Data Streaming")
websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("wss://o7xkp9lilf.execute-api.ap-northeast-1.amazonaws.com/production")

def send_message(message):
    ws.send(json.dumps(message))

# Create an empty DataFrame to store the received data
df = pd.DataFrame(columns=["time", "temperature"])

# Create an empty line chart
chart = st.line_chart(use_container_width=True)

while True:
    try:
        message = ws.recv()
        
        # Extract the value from the received data
        temperature = message		 		
        # Get the current time
        time = datetime.now().strftime("%H:%M:%S")

        # Append the data to the DataFrame
        df = df.append({"time": time, "temperature": temperature}, ignore_index=True)
        df['temperature'] = pd.to_numeric(df['temperature'])

        if len(df) > 20:
            df = df.tail(20)
        
        chart.empty()

        chart = st.line_chart(df.set_index("time"))

    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break
