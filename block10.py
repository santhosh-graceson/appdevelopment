import json
import websocket
import streamlit as st
import pandas as pd
import altair as alt
import time as t
import numpy as np
st.set_page_config(layout ="wide")
st.image("https://i.ibb.co/Fm8Gw54/Ai-Den-Medical-Rev-3-Mini.png",width=100)
st.markdown("<h1 style='font-size:30px;text-align: center; color: darkblue;'>DORION VENTILATOR</h1>", unsafe_allow_html=True)
# Define the chart
chart = st.empty()

websocket.enableTrace(True)
ws = websocket.WebSocket()
ws1 = websocket.WebSocket()
ws2 = websocket.WebSocket()
ws3 = websocket.WebSocket()
ws4 = websocket.WebSocket()
ws5 = websocket.WebSocket()
ws.connect("wss://i7kggwivc5.execute-api.us-west-2.amazonaws.com/production")
ws1.connect("wss://fr21il5ko7.execute-api.us-west-2.amazonaws.com/production")
ws2.connect("wss://ll2yuct7hh.execute-api.us-west-2.amazonaws.com/production")
ws3.connect("wss://jgkvivcmyi.execute-api.us-west-2.amazonaws.com/production")
ws4.connect("wss://pepkkt2rhj.execute-api.us-west-2.amazonaws.com/production")
ws5.connect("wss://vvtdnwz280.execute-api.us-west-2.amazonaws.com/production")
df_Inspiration_Flow = pd.DataFrame(columns=["Units","Inspiration_Flow"])
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
n=0

# Define the layout
values_container,values1_container= st.columns([1,1])
values2_container,values3_container= st.columns([1,1])
insp_flow_container,awp_container = values_container.columns(2)
awp_container1,awp_container2 = values1_container.columns(2)
awp_container3, awp_container4= values2_container.columns(2)
awp_container5, awp_container6 = values3_container.columns(2)


with values1_container:
    st.markdown(
    """
    <style>
        /* Change background color of column parameters */
        .element-container:nth-child(even) {
            background-color: #ADD8E6;
        }
        /* Add padding to column parameters */
        .element-container .stTextInput{
            padding: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)


last_insp_flow = insp_flow_container.empty()
last_insp_flow.markdown("<h2 style='font-size:19px;color: #8B0000;font-synthesis: bold;text-align:center;'>Ppeak</h2>", unsafe_allow_html=True)
last_insp_flow_value = insp_flow_container.empty()
last_insp_flow_value.markdown("<p style='font-size:18px;color: #8B0000;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp = awp_container.empty()
last_awp.markdown("<h2 style='font-size:19px;color: #00008B;font-synthesis: bold;text-align:center;'>O2</h2>", unsafe_allow_html=True)
last_awp_value = awp_container.empty()
last_awp_value.markdown("<p style='font-size:18px;color: #00008B;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp1 = awp_container1.empty()
last_awp1.markdown("<h2 style='font-size:19px;color: #056608;font-synthesis: bold;text-align:center;'>Flow</h2>", unsafe_allow_html=True)
last_awp1_value = awp_container1.empty()
last_awp1_value.markdown("<p style='font-size:18px;color: #056608;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp2 = awp_container2.empty()
last_awp2.markdown("<h2 style='font-size:19px;color: #000000;font-synthesis: bold;text-align:center;'>RR</h2>", unsafe_allow_html=True)
last_awp2_value = awp_container2.empty()
last_awp2_value.markdown("<p style='font-size:18px;color: #000000;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp3 = awp_container3.empty()
last_awp3.markdown("<h2 style='font-size:19px;color: #36013F;font-synthesis: bold;text-align:center;'>I:E</h2>", unsafe_allow_html=True)
last_awp3_value = awp_container3.empty()
last_awp3_value.markdown("<p style='font-size:18px;color: #36013F;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp4 = awp_container4.empty()
last_awp4.markdown("<h2 style='font-size:19px;color: #8B4000;font-synthesis: bold;text-align:center;'>PEEP</h2>", unsafe_allow_html=True)
last_awp4_value = awp_container4.empty()
last_awp4_value.markdown("<p style='font-size:18px;color: #8B4000;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp5 = awp_container5.empty()
last_awp5.markdown("<h2 style='font-size:19px;color: #000000;font-synthesis: bold;text-align:center;'>VTi</h2>", unsafe_allow_html=True)
last_awp5_value = awp_container5.empty()
last_awp5_value.markdown("<p style='font-size:18px;color: #000000;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp6 = awp_container6.empty()
last_awp6.markdown("<h2 style='font-size:19px;color: #492000;font-synthesis: bold;text-align:center;'>VTe</h2>", unsafe_allow_html=True)
last_awp6_value = awp_container6.empty()
last_awp6_value.markdown("<p style='font-size:18px;color: #492000;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)
counter = 0

while True:
    try:  
        # @st.cache
        # def message(message):
        #     return message 
        # @st.cache
        # def message1(message1):
        #     return message1
        # @st.cache
        # def message2(message2):
        #     return message2
        # @st.cache
        # def message3(message3):
        #     return message3
        # @st.cache
        # def message4(message4):
        #     return message4
        # @st.cache
        # def message5(message5):
        #     return message5
        message = ws.recv()
        message1 = ws1.recv() 
        message2 = ws2.recv()  
        message3 = ws3.recv()  
        message4 = ws4.recv()  
        message5 = ws5.recv()  
        data = json.loads(message)
        data1 = json.loads(message1)
        data2 = json.loads(message2)
        data3 = json.loads(message3)
        data4 = json.loads(message4)
        data5 = json.loads(message5)
        if n<=160:
            if counter<9:
                a.append(data)
                b.append(data1)
                c.append(data2)
                d.append(data3)
                e.append(data4)
                f.append(data5)
                counter=counter+1
            elif counter==9:
                counter = 0
                a.append(data)
                b.append(data1)
                c.append(data2)
                d.append(data3)
                e.append(data4)
                f.append(data5)



                # Update latest value display
                last_insp_flow_value.markdown("<p style='font-size:18px;color: #8B0000;font-synthesis: bold;text-align:center;'>{}</p>".format(f[0]), unsafe_allow_html=True)
                last_awp_value.markdown("<p style='font-size:18px;color: #00008B;font-synthesis: bold;text-align:center;'>{}</p>".format(b[0]), unsafe_allow_html=True)
                last_awp1_value.markdown("<p style='font-size:18px;color: #056608;font-synthesis: bold;text-align:center;'>{}</p>".format(c[0]), unsafe_allow_html=True)
                last_awp2_value.markdown("<p style='font-size:18px;color: #000000;font-synthesis: bold;text-align:center;'>{}</p>".format(0), unsafe_allow_html=True)
                last_awp3_value.markdown("<p style='font-size:18px;color: #36013F;font-synthesis: bold;text-align:center;'>{}</p>".format(0), unsafe_allow_html=True)
                last_awp4_value.markdown("<p style='font-size:18px;color: #8B4000;font-synthesis: bold;text-align:center;'>{}</p>".format(0), unsafe_allow_html=True)
                last_awp5_value.markdown("<p style='font-size:18px;color: #000000;font-synthesis: bold;text-align:center;'>{}</p>".format(d[0]), unsafe_allow_html=True)
                last_awp6_value.markdown("<p style='font-size:18px;color: #492000;font-synthesis: bold;text-align:center;'>{}</p>".format(e[0]), unsafe_allow_html=True)
                
                # Update chart
                for i in range(10):
                    init_time=t.time()    
                    df_Inspiration_Flow = df_Inspiration_Flow.append({"Units":n+i, "Inspiration_Flow": a[i]}, ignore_index=True)
                    chart.altair_chart((alt.Chart(df_Inspiration_Flow.tail(160)).mark_line().encode(x='Units',y=alt.Y('Inspiration_Flow', scale=alt.Scale(domain=[0,35])))).properties(width=1285,height=250))
                    final_time=t.time()
                    time_taken=(final_time-init_time)
                    rem_time=np.absolute(0.05-time_taken)
                    t.sleep(rem_time)   
                print("Insp_Flow =",a)
                a.clear()
                b.clear()
                c.clear()
                d.clear()
                e.clear()
                f.clear()
                n=n+10
        elif n>160:
            n=1 
        else:
            print("Data not received")
    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break