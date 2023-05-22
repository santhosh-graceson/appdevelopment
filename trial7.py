import json
import websocket
import streamlit as st
import pandas as pd
import altair as alt
import time as t
import numpy as np
from datetime import datetime
from PIL import Image
RANGE=10000
st.set_page_config(layout ="wide")
st.image("https://i.ibb.co/Fm8Gw54/Ai-Den-Medical-Rev-3-Mini.png",width=100)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css(r"https://github.com/santhosh-graceson/appdevelopment/blob/main/style.css")
part2,part3=st.columns([15,3])
col1,col2,col3,col4,col5=part2.columns([3,1,2,10,2])
col6,col7,col8,col9,col10=part3.columns([1,1,1,1,1])
with col2:
    image1 = Image.open(r"C:\Users\mpoor\Downloads\10522.png")   
    st.image(image1,width=40)
with col10:
    image2 = Image.open(r"C:\Users\mpoor\Downloads\wifi-icon-white.png")
    st.image(image2,width=60)
with col6:
    image3 = Image.open(r"C:\Users\mpoor\Downloads\wifi-icon-white.png")
    plug_icon= st.image(image3,width=60)
with col7:    
    image4 = Image.open(r"C:\Users\mpoor\Downloads\wifi-icon-white.png")
    plug_icon= st.image(image4,width=60)
with col8:
    image5 = Image.open(r"C:\Users\mpoor\Downloads\wifi-icon-white.png")
    plug_icon= st.image(image5,width=60)
with col9:
    image6 = Image.open(r"C:\Users\mpoor\Downloads\wifi-icon-white.png")
    plug_icon= st.image(image6,width=60)
with col3:
    f="Patient ID"
    e="25"
    st.markdown("<p style='font-size:16px;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(e), unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(f), unsafe_allow_html=True)
with col1:
    x = datetime.now()
    a=x.strftime("%d-%b-%y") 
    st.markdown("<p style='font-size:16px;text-align: center;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(a), unsafe_allow_html=True)
    b=x.strftime("%I:%M")
    st.markdown("<p style='font-size:16px;text-align: center;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(b), unsafe_allow_html=True)
with col4:
    st.markdown("<h1 style='font-size:20px;text-align: center; color: #000000;'>Patient is Ventilated</h1>", unsafe_allow_html=True)
with col5:
     c ="Bi-Level"
     st.markdown("<p style='font-size:16px;text-align: center;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(c), unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     div.css-peenxw.e1tzin5v0{
#         gap: 0.2rem;
#     }
#     </style>
#     """,unsafe_allow_html=True)
st.markdown("""
    <style>
    div.css-ocqkz7.e1tzin5v3{
        gap: 0.1rem;
    }
    </style>
    """,unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     div.css-kfxrcf.e1tzin5v0{
#     gap : 0rem;
#     }
#     </style>
#     """,unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     div.css-ocqkz7.e1tzin5v3{
#         gap: 0.1rem;
#     }
#     </style>
#     """,unsafe_allow_html=True) 
First_Parameter = st.markdown("<h1 style='font-size:20px;text-align: left; color: #ff904f;width: 940px;'>INSPIRATION FLOW</h1>", unsafe_allow_html=True)
chart_, values_container = st.columns([3, 1])
chart_container,null1 = chart_.columns([99,1])
chart2_container,null1=chart_.columns([99,1])

insp_flow_container,awp_container = values_container.columns(2)
awp_container1,awp_container2=values_container.columns(2)


awp_container3, awp_container4= values_container.columns(2)
awp_container5, awp_container6 = values_container.columns(2)
chart = chart_container.empty()
websocket.enableTrace(True)
ws = websocket.WebSocket()
ws1 = websocket.WebSocket()
ws.connect("wss://i7kggwivc5.execute-api.us-west-2.amazonaws.com/production")
ws1.connect("wss://fr21il5ko7.execute-api.us-west-2.amazonaws.com/production")
df_Inspiration_Flow = pd.DataFrame(columns=["Units","Inspiration_Flow"])
a=[]
n=0
last_insp_flow = insp_flow_container.empty()
last_insp_flow.markdown("<h2 style='font-size:19px;color: #80ff80;font-synthesis: bold;text-align:center;fill:#000000'>Ppeak</h2>", unsafe_allow_html=True)
last_insp_flow_value = insp_flow_container.empty() 
last_insp_flow_value.markdown("<p style='font-size:36px;color: #80ff80;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp = awp_container.empty()
last_awp.markdown("<h2 style='font-size:19px;color: #FFFFFF;font-synthesis: bold;text-align:center;'>O2</h2>", unsafe_allow_html=True)
last_awp_value = awp_container.empty()
last_awp_value.markdown("<p style='font-size:36px;color: #FFFFFF;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp1 = awp_container1.empty()
last_awp1.markdown("<h2 style='font-size:19px;color: #ff904f;font-synthesis: bold;text-align:center;'>Flow</h2>", unsafe_allow_html=True)
last_awp1_value = awp_container1.empty()
last_awp1_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp2 = awp_container2.empty()
last_awp2.markdown("<h2 style='font-size:19px;color: #ff904f;font-synthesis: bold;text-align:center;'>RR</h2>", unsafe_allow_html=True)
last_awp2_value = awp_container2.empty()
last_awp2_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp3 = awp_container3.empty()
last_awp3.markdown("<h2 style='font-size:19px;color: #ff904f;font-synthesis: bold;text-align:center;'>I:E</h2>", unsafe_allow_html=True)
last_awp3_value = awp_container3.empty()
last_awp3_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp4 = awp_container4.empty()
last_awp4.markdown("<h2 style='font-size:19px;color: #80ff80;font-synthesis: bold;text-align:center;'>PEEP</h2>", unsafe_allow_html=True)
last_awp4_value = awp_container4.empty()
last_awp4_value.markdown("<p style='font-size:36px;color: #80ff80;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp5 = awp_container5.empty()
last_awp5.markdown("<h2 style='font-size:19px;color: #87CEEB;font-synthesis: bold;text-align:center;'>VTi</h2>", unsafe_allow_html=True)
last_awp5_value = awp_container5.empty()
last_awp5_value.markdown("<p style='font-size:36px;color: #87CEEB;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)
last_awp6 = awp_container6.empty()
last_awp6.markdown("<h2 style='font-size:19px;color: #87CEEB;font-synthesis: bold;text-align:center;'>VTe</h2>", unsafe_allow_html=True)
last_awp6_value = awp_container6.empty()
last_awp6_value.markdown("<p style='font-size:36px;color: #87CEEB;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)
counter=0
while True:
    try:  
        message = ws.recv()
        message1 = ws1.recv() 
        data = json.loads(message)
        data1 = json.loads(message1)
        if n<=160:
            if counter<9:
                a.append(data)
                counter=counter+1
            elif counter==9:
                counter = 0
                a.append(data)
                # Update latest value display
                last_insp_flow_value.markdown("<p style='font-size:36px;color: #80ff80;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[4]), unsafe_allow_html=True)
                last_awp_value.markdown("<p style='font-size:36px;color: #FFFFFF;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[0]), unsafe_allow_html=True)
                last_awp1_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[1]), unsafe_allow_html=True)
                last_awp2_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[5]), unsafe_allow_html=True)
                last_awp3_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[7]), unsafe_allow_html=True)
                last_awp4_value.markdown("<p style='font-size:36px;color: #80ff80;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[8]), unsafe_allow_html=True)
                last_awp5_value.markdown("<p style='font-size:36px;color: #87CEEB;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[2]), unsafe_allow_html=True)
                last_awp6_value.markdown("<p style='font-size:36px;color: #87CEEB;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[3]), unsafe_allow_html=True)
                # Update chart
                for i in range(10):
                    init_time=t.time()    
                    df_Inspiration_Flow = df_Inspiration_Flow.append({"Units":n+i, "Inspiration_Flow": a[i]}, ignore_index=True)
                    chart.altair_chart((alt.Chart(df_Inspiration_Flow.tail(160)).mark_area(color='#ff904f').encode(x='Units',y=alt.Y('Inspiration_Flow', scale=alt.Scale(domain=[0,35])))).properties(width=940,height=250).configure_axis(grid=False).configure_axisY(grid=True))
                    final_time=t.time()
                    time_taken=(final_time-init_time)
                    rem_time=np.absolute(0.05-time_taken)
                    t.sleep(rem_time)   
                print("Insp_Flow =",a)
                a.clear()
                n=n+10
        elif n>160:
            n=1 
        else:
            print("Data not received")
    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break
