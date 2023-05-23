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
st.image("https://i.ibb.co/q059f9Q/Ai-Den-Medical-Rev-3-Mini-white.png",width=100)
part2,part3=st.columns([15,3])
col1,col2,col3,col4,col5=part2.columns([3,1,2,10,2])
col6,col7,col8,col9=part3.columns([1,1,1,1])
with col2:
    st.markdown("<p style='font-size:0.8px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col2:  
    st.image("https://i.ibb.co/Y084PGJ/10522.png",width =40,use_column_width="auto")
with col2:
    st.markdown("<p style='font-size:0.01px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col6:
    st.markdown("<p style='font-size:1px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col6:
    # image3 = Image.open(r"C:\Users\mpoor\Downloads\wifi-icon-white.png")
    plug_icon= st.image("https://i.ibb.co/nRmgTmw/wifi-icon-white.png",width=60)
with col7:
    st.markdown("<p style='font-size:1px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col7:    
    plug_icon= st.image("https://i.ibb.co/nRmgTmw/wifi-icon-white.png",width=60)
with col8:
    st.markdown("<p style='font-size:1px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col8:
    plug_icon= st.image("https://i.ibb.co/nRmgTmw/wifi-icon-white.png",width=60)
with col9:
    st.markdown("<p style='font-size:1px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col9:
    plug_icon= st.image("https://i.ibb.co/nRmgTmw/wifi-icon-white.png",width=60)
with col3:
    st.markdown("<p style='font-size:0.001px;color: #070D1C;'>1</p>", unsafe_allow_html=True)
with col3:
    f="Patient ID"
    e="25"
    st.markdown("<p style='font-size:16px;text-align: center;gap: 0rem;padding:  0;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(e), unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;text-align: center;gap: 0rem;padding:  0;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(f), unsafe_allow_html=True)
with col1:
    st.markdown("<p style='font-size:0.001px;color: #070D1C;'>1</p>", unsafe_allow_html=True)
with col1:
    x = datetime.now()
    a=x.strftime("%d-%b-%y") 
    st.markdown("<p style='font-size:16px;gap: 0rem;padding:  0;text-align: center;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(a), unsafe_allow_html=True)
    b=x.strftime("%I:%M")
    st.markdown("<p style='font-size:16px;gap: 0rem;padding:  0;  text-align: center;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(b), unsafe_allow_html=True)
with col4:
    st.markdown("<h1 style='font-size:32px;text-align: center; color: #000000;'>Patient is Ventilated</h1>", unsafe_allow_html=True)
with col5:
     st.markdown("<h1 style='font-size:20px;text-align: center; color: #FFFFFF;'>Bi-Level</h1>", unsafe_allow_html=True)

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
last_insp_flow.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #80ff80;font-synthesis: bold;text-align:center;fill:#000000'>Ppeak</h2>", unsafe_allow_html=True)
last_insp_flow_value = insp_flow_container.empty() 
last_insp_flow_value.markdown("<p style='font-size:36px;color: #80ff80;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp = awp_container.empty()
last_awp.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #FFFFFF;font-synthesis: bold;text-align:center;'>O2</h2>", unsafe_allow_html=True)
last_awp_value = awp_container.empty()
last_awp_value.markdown("<p style='font-size:36px;color: #FFFFFF;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp1 = awp_container1.empty()
last_awp1.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>Flow</h2>", unsafe_allow_html=True)
last_awp1_value = awp_container1.empty()
last_awp1_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp2 = awp_container2.empty()
last_awp2.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>RR</h2>", unsafe_allow_html=True)
last_awp2_value = awp_container2.empty()
last_awp2_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp3 = awp_container3.empty()
last_awp3.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>I:E</h2>", unsafe_allow_html=True)
last_awp3_value = awp_container3.empty()
last_awp3_value.markdown("<p style='font-size:36px;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp4 = awp_container4.empty()
last_awp4.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #80ff80;font-synthesis: bold;text-align:center;'>PEEP</h2>", unsafe_allow_html=True)
last_awp4_value = awp_container4.empty()
last_awp4_value.markdown("<p style='font-size:36px;color: #80ff80;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp5 = awp_container5.empty()
last_awp5.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #87CEEB;font-synthesis: bold;text-align:center;'>VTi</h2>", unsafe_allow_html=True)
last_awp5_value = awp_container5.empty()
last_awp5_value.markdown("<p style='font-size:36px;color: #87CEEB;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)
last_awp6 = awp_container6.empty()
last_awp6.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #87CEEB;font-synthesis: bold;text-align:center;'>VTe</h2>", unsafe_allow_html=True)
last_awp6_value = awp_container6.empty()
last_awp6_value.markdown("<p style='font-size:36px;color: #87CEEB;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)
counter=0
st.markdown("""
    <style> 
    div.css-ocqkz7.e1tzin5v3{
        gap: 0.1rem;
    }
    </style>
    """,unsafe_allow_html=True)
st.markdown("""
    <style>
    div.css-peenxw.e1tzin5v0{
        gap: 0.1rem;
    }
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   h2#ppeak{
    background-color:#070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   h2#flow{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   h2#rr{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   h2#i-e{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   h2#peep{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   h2#vti{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   h2#vte{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   p{
background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   h2#o2{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-1rrbo1k.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-m9mqwd.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-1wk3dql.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-115gedg.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-1kb5vwi.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-1cwt8z2.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-1l269bu.e1tzin5v1{
    background-color: #070D1C;
    text-align: center;
    justify-content: center;
    vertical-align: middle
}
    </style>
    """,unsafe_allow_html=True)


st.markdown("""
    <style>
   div.css-103uxol.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)


st.markdown("""
    <style>
   div.css-949r0i.e1tzin5v1{
    background-color: #9EB8F5;
    border: 1px solid black;
    border-radius: 8px;
}
    </style>
    """,unsafe_allow_html=True)


st.markdown("""
    <style>
   div.css-1l269bu.e1tzin5v1{
    background-color: #070D1C;
    text-align: center;
    justify-content: center;
    vertical-align: middle
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-1m8p54g.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   div.css-1l269bu.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
   canvas.marks{
    border-bottom-color: #535B6B;
    border-right-color: #535B6B;
    border-left-color: #535B6B;
    border-right-style: solid;
    border-bottom-style: solid;
    border-left-style: solid;
}
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
    h1#inspiration-flow{
    border-top-color:#535B6B;
    border-right-color: #535B6B;
    border-left-color: #535B6B;
    border-right-style: solid;
    border-top-style: solid;
    border-left-style: solid;
}
    </style>
    """,unsafe_allow_html=True)

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