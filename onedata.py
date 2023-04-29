import json
import websocket
import streamlit as st
import pandas as pd
import altair as alt
import time as t
import numpy as np
st.title("Plotting of Dummy Ventilator Data")
websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("wss://i7kggwivc5.execute-api.us-west-2.amazonaws.com/production")
df_Inspiration_Flow = pd.DataFrame(columns=["Units","Inspiration_Flow"])
chart_Inspiration_Flow = st.empty()
a=[]
n=0
counter = 0
while True:
    try:  
        @st.cache
        def message(message):
            return message 
        message = ws.recv()   
        data = json.loads(message)
        if n<=160:
            if counter<9:
                a.append(data)
                counter=counter+1
            elif counter==9:
                counter = 0
                a.append(data)
                print("Inspiration_Flow = ",a)
                for i in range(10):
                    init_time=t.time()    
                    df_Inspiration_Flow = df_Inspiration_Flow.append({"Units":n+i, "Inspiration_Flow": a[i]}, ignore_index=True)
                    chart_Inspiration_Flow.altair_chart((alt.Chart(df_Inspiration_Flow.tail(160)).mark_line().encode(x='Units',y=alt.Y('Inspiration_Flow', scale=alt.Scale(domain=[0,40])))).properties(width=900))
                    
                    final_time=t.time()
                    time_taken=(final_time-init_time)
                    rem_time=np.absolute(0.05-time_taken)
                    t.sleep(rem_time)   
                a.clear()
                n=n+10
        elif n>160:
            n=1 
        else:
            print("Data not received")
    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break