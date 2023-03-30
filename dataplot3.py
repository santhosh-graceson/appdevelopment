import requests
import streamlit as st
import time
import json
import pandas as pd
from datetime import datetime, timedelta

api_url = 'https://t3mosjye77.execute-api.ap-northeast-1.amazonaws.com/new/body'

# Create a dictionary to store the charts
charts = {}

# Iterate through the parameters
for param in ["Tidal_Volume", "Respiratory_Rate", "PEEP_Pressure", "O2_level"]:
    # Create an empty chart for the parameter
    charts[param] = st.line_chart(use_container_width=True)

while True:
    response = requests.get(api_url)
    if response.status_code == 200:
        response_body = response.json()["body-json"]
        data = json.loads(response_body)

        # Create a dictionary to store the data for each parameter
        param_data = {}
        for param in ["Tidal_Volume", "Respiratory_Rate", "PEEP_Pressure", "O2_level"]:
            if param in data:
                param_data[param] = data[param]

        # Create a DataFrame for each parameter
        for param, param_value in param_data.items():
            df = pd.DataFrame.from_dict({param: param_value}, orient="index").T
            df["timestamp"] = datetime.utcnow().strftime('%H:%M:%S.%f')
            df.set_index("timestamp", inplace=True)

            # Keep only the rows with timestamp within the last 20 seconds
            time_threshold = datetime.utcnow() - timedelta(seconds=20)
            df = df[df.index >= time_threshold.strftime('%H:%M:%S.%f')]

            # Update the chart for the parameter with the latest data
            charts[param].add_rows(df)

        time.sleep(0.02)
    else:
        st.write(f"Error: {response.status_code}")


