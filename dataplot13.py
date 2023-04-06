import json
import websocket
import streamlit as st
import pandas as pd
from datetime import datetime

websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("wss://o7xkp9lilf.execute-api.ap-northeast-1.amazonaws.com/production")

def send_message(message):
    ws.send(json.dumps(message))

# Create an empty DataFrame to store the received data
df = pd.DataFrame(columns=["time", "value"])

# Create an empty line chart
chart = st.line_chart(use_container_width=True)

while True:
    try:
        message = ws.recv()
        
        # Extract the value from the received data
        value = message
        
        # Get the current time
        time = datetime.now().strftime("%H:%M:%S.%f")

        # Append the data to the DataFrame
        df = df.append({"time": time, "value": value}, ignore_index=True)

        # Update the line chart
        chart.add_rows(df.set_index("time"))

    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break
