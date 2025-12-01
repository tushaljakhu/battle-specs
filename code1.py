import streamlit as st
import base64
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import plotly.graph_objects as go
import re
import matplotlib.ticker as ticker
from streamlit_lottie import st_lottie
import json
import streamlit as st
import requests    





st.set_page_config(layout="wide", page_title="Battle Specs ⚔️", page_icon="📱")


st.markdown("""
<style>
form[action^="/"] button[type="submit"] {
    background-color: #ffffff;
    color: #000000 !important;
    font-weight: bold;
    border: 2px solid black;
    border-radius: 10px;
    padding: 0.5em 1.2em;
}
div.stForm {
    border: 2px solid white;
    border-radius: 12px;
    padding: 20px;
}
hr { border: 1px solid white; }
form[action^="/"] button[type="submit"]:hover {
    background-color: #f0f0f0;
    color: black;
}
label { color: white !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)


sr = pd.read_excel("Datasetgold.xlsx")


def encode_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

bg_base64 = encode_image_to_base64("pb3.jpg")
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{bg_base64}");
    background-size: cover;
}}
</style>
""", unsafe_allow_html=True)
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url1 ="https://lottie.host/5e36be7b-f950-468d-b597-326f66aa8c9f/NeZRCDyseu.json"
lottie_json1 = load_lottie_url(lottie_url1)

with st.sidebar:
    
    if lottie_json1:
        st_lottie(lottie_json1, height=100,width=200, loop=True)
         
    else:
        st.write("Lottie animation not found.")

    st.markdown("""
    <style>
     /* Sidebar fix: content starts from very top */
     [data-testid="stSidebar"] > div:first-child {
     padding-top: 0px !important;   /* remove push down */
     margin-top: 0px !important;
   }
    </style>            
     """, unsafe_allow_html=True)
    selected = option_menu(
        menu_title="Battle Specs Menu",
        options=["Comparison", "Visualization", "Price Comparison", "Tutorial"],
        icons=["phone", "bar-chart", "graph-up", "lightbulb"],
        menu_icon="cast",
        default_index=0
    )
    
    lottie_url ="https://lottie.host/5e36be7b-f950-468d-b597-326f66aa8c9f/NeZRCDyseu.json"
    lottie_json = load_lottie_url(lottie_url)

if selected == "Comparison":
    
    st.markdown("<h1 style='color: white;'>Mobile Comparison Project :</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: white;'>Battle Specs 📱⚔️📱 :</h2>", unsafe_allow_html=True)
    
    st.markdown("<hr style='height:3px;border:none;background-color:white;' />", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 0.2, 3])

    with col1:
        st.markdown("<h2 style='color:white;'>➡️Select your 1st phone📱 </h2>", unsafe_allow_html=True)
        gif_b64 = encode_image_to_base64("photo2.gif")
        st.markdown(f"<img src='data:image/gif;base64,{gif_b64}' style='height:160px; width:160px; display:block; margin:auto;'/>", unsafe_allow_html=True)

        company_a = st.selectbox("🏢 Select Company of First Phone 📱", sorted(sr["Company Name"].unique()))
        model_a = st.selectbox("📱 Select Model of First Phone", sorted(sr[sr["Company Name"] == company_a]["Model Name"].astype(str).unique()))
        st.session_state["phone1"] = model_a
        st.session_state.model_a = model_a


    with col2:
      st.markdown("""
        <style>
        .divider {
            height: 130vh;         
            width: 6px;
            background-color: white;
            border-radius: 4px;
            margin-left: auto;
            margin-right: auto;
            position: relative;
            top: -4vh;            
        }
        </style>
        <div class="divider"></div>
        """, unsafe_allow_html=True)
    

    with col3:
        st.markdown("<h2 style='color:white;'>➡️Select your 2nd phone 📱</h2>", unsafe_allow_html=True)
        st.markdown(f"<img src='data:image/gif;base64,{gif_b64}' style='height:160px; width:160px; display:block; margin:auto;'/>", unsafe_allow_html=True)

        company_b = st.selectbox("🏢 Select Company of Second Phone", sorted(sr["Company Name"].unique()))
        model_b = st.selectbox("📱 Select Model of Second Phone", sorted(sr[sr["Company Name"] == company_b]["Model Name"].astype(str).unique()))
        st.session_state["phone2"] = model_b
        st.session_state.model_b = model_b

    st.markdown("""
    <style>
    @keyframes fight {0% {transform: translateX(0);} 25% {transform: translateX(-3px);} 50% {transform: translateX(3px);} 75% {transform: translateX(-2px);} 100% {transform: translateX(0);} }
    div.stButton > button {
        width: 420px; height: 85px; font-size: 42px; font-weight: bold;
        background-color: #ffffff; color: #000000;
        border: 3px solid black; border-radius: 14px; margin: 20px auto;
        display: block; box-shadow: 2px 2px 12px rgba(0,0,0,0.4);
    }
    div.stButton > button:hover {
        animation: fight 0.6s infinite; background-color: skyblue; color: white;
        transform: scale(1.06);
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button("📱⚔️📱 Comparison"):
        with col1:
            st.markdown(f"<h3 style='color:white;'>📱 Model Name: {model_a}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:white;'>🏢 Company Name: {company_a}</h3>", unsafe_allow_html=True)
            phone_a_data = sr[(sr["Company Name"] == company_a) & (sr["Model Name"] == model_a)]
            if not phone_a_data.empty:
              specs_a = phone_a_data.iloc[0]
              st.markdown(f"""<h3 style='color:white;font-size:18px; line-height: 2;'>  <!-- line-height controls spacing -->
              ⚖️Weight: {specs_a['Mobile Weight']}<br> 
              💾RAM: {specs_a['RAM']}<br> 
              🤳Front Camera: {specs_a['Front Camera']}<br>  
              📸Back Camera: {specs_a['Back Camera']}<br>  
              ⚙️Processor: {specs_a['Processor']}<br>  
              🔋Battery: {specs_a['Battery Capacity']}<br> 
              📏Screen Size: {specs_a['Screen Size']}<br>
              📶 Connectivity: {specs_a['Connectivity']}</h3>  
              """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"<h3 style='color:white;'>📱 Model Name: {model_b}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:white;'>🏢 Company Name: {company_b}</h3>", unsafe_allow_html=True)
            phone_b_data = sr[(sr["Company Name"] == company_b) & (sr["Model Name"] == model_b)]
            if not phone_b_data.empty:
              specs_b = phone_b_data.iloc[0]
              st.markdown(f"""<h3 style='color:white; font-size:18px; line-height: 2;'>  <!-- line-height controls spacing -->
              ⚖️Weight: {specs_b['Mobile Weight']}<br> 
              💾RAM: {specs_b['RAM']}<br> 
              🤳Front Camera: {specs_b['Front Camera']}<br>  
              📸Back Camera: {specs_b['Back Camera']}<br>  
              ⚙️Processor: {specs_b['Processor']}<br>  
              🔋Battery: {specs_b['Battery Capacity']}<br> 
              📏Screen Size: {specs_b['Screen Size']}<br>
              📶 Connectivity: {specs_b['Connectivity']}</h3> 
              """, unsafe_allow_html=True)

elif selected == "Visualization":
    
    st.markdown("""
    <style>
    /* Change background color */
    .main {
        background-color: #0a0a0a;  /* dark background for better white contrast */
    }

    /* Change title and header text color to white */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    
    </style>
    """, unsafe_allow_html=True)


    st.title("📊 Visualization Page")
    st.header("📊 Graphical Comparison of Specifications :")
    sr=pd.read_excel("Datasetgold.xlsx")
    sr.head(5)
    st.markdown("""
    <style>
    /* Style the entire tab container */
    [data-testid="stTabs"] div[role="tablist"] {
    background-color: #f5f5f5;
    padding: 8px;
    border-radius: 10px;
    gap: 10px;
    display: flex;
    justify-content: flex-start;
    }

    /* Style for active tab */
    [data-testid="stTab"][aria-selected="true"] {
    background-color: #004080 !important;  /* Deep blue */
    color: #ffffff !important;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 8px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    /* Style for inactive tabs */
    [data-testid="stTab"][aria-selected="false"] {
    background-color: #e0e0e0 !important;  /* light gray */
    color: #333333 !important;
    padding: 8px 16px;
    border-radius: 8px;
    transition: 0.3s ease;
    }

    /* Hover effect */
    [data-testid="stTab"]:hover {
    background-color: #cfcfcf !important;
    color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    sr = pd.read_excel("Datasetgold.xlsx")

    if "model_a" not in st.session_state or "model_b" not in st.session_state:
      st.warning("Please select two phones on the Comparison page first.")
      st.stop()
    else:
      model_a = st.session_state.model_a
      model_b = st.session_state.model_b

    t1,t2,t3,t4,t5,t6=st.tabs(["⚙️ Processor", "🔋 Battery", "📷 Back Camera","💾 RAM","🤳 Front Camera","📅 Launch Year"])
    with t1:
      st.title("⚙️ Processor Comparison")
      processor_rank ={
       "Snapdragon 8 Gen 3": 10,
       "A17 Bionic": 10,
        "A17 Bionic": 10,
        "A17 Bionic": 10,
        "A17 Bionic": 10,
        "A17 Bionic": 10,
        "A17 Bionic": 10,
        "A17 Pro": 10,
        "A17 Pro": 10,
        "A17 Pro": 10,
        "A17 Pro": 10,
        "A17 Pro": 10,
        "A17 Pro": 10,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,        
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A16 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A15 Bionic": 9,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A11 Bionic": 7,
        "A11 Bionic": 7,                
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A14 Bionic": 8,
        "A14 Bionic": 8,
        "A13 Bionic": 8,
        "A13 Bionic": 8,
        "A12 Bionic": 7,
        "A12 Bionic": 7,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "A12Z Bionic": 8,
        "Exynos 2400": 9,
        "Exynos 2400": 9,
        "Exynos 2400": 9,
        "Exynos 2400": 9,
        "Exynos 2400": 9,
        "Exynos 2400": 9,
        "Snapdragon 8 Gen 2": 9, 
        "Snapdragon 8 Gen 2": 9, 
        "Snapdragon 8 Gen 2": 9, 
        "Snapdragon 8 Gen 2": 9, 
        "Snapdragon 8 Gen 2": 9, 
        "Snapdragon 8 Gen 2": 9, 
        " Exynos 2200": 8,  
        " Exynos 2200": 8,  
        " Exynos 2200": 8,  
        " Exynos 2200": 8,  
        " Exynos 2200": 8,  
        " Exynos 2200": 8,  
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 1": 9,
        "Snapdragon 8 Gen 1": 9,
        "Snapdragon 8 Gen 1": 9,
        "Snapdragon 8 Gen 1": 9,
        "Exynos 1380": 7,
        "Exynos 1380": 7,
        "MediaTek Dimensity 1080": 8,
        ",MediaTek Dimensity 1080": 8,
        "MediaTek Helio G99": 7,
        "MediaTek Helio G99": 7,
        "Exynos 850 ":6,
        "Exynos 850 ":6,
        "Exynos 850 ":6,
        "Exynos 850 ":6,
        "Exynos 1380": 7,
        "Exynos 1380": 7,
        "Exynos 1280": 7,
        "Exynos 1280": 7,
        "Exynos 850": 6,
        "Exynos 850": 6,
        "MediaTek Helio P35": 5,
        "MediaTek Helio P35": 5,
        "Exynos 1380": 7,
        "Exynos 1380": 7,
        "Exynos 1280": 7,
        "Exynos 1280": 7,
        "Exynos 850": 6,
        "Exynos 850": 6,
        "Exynos 990": 8,
        "Exynos 990": 8,
        "Exynos 990": 8,
        "Exynos 990": 8,
        "Exynos 9825": 7,
        "Exynos 9825": 7,
        "Exynos 9825": 7,
        "Exynos 9825": 7,
        "Exynos 1380": 7,
        "Exynos 850": 6,
        "Snapdragon 450": 5,
        "Exynos 7870": 4,
        "Snapdragon 425": 4,
        "Exynos 7570": 4,
        "Snapdragon 653": 6,        
        "Snapdragon 625": 5,        
        "Snapdragon 617": 5,        
        "Snapdragon 888": 9,        
        "Snapdragon 888": 9,        
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 2": 9,
        "Exynos 1380": 7,
        "Snapdragon 8 Gen 1": 9,
        "Snapdragon 8 Gen 1": 9,
        "Snapdragon 8 Gen 1": 9,
        "Snapdragon 695": 7,
        "MediaTek Helio G99": 7,
        "Unisoc T618": 6,
        "MediaTek Helio P22T": 4,
        "Exynos 1380": 7,
        "Snapdragon 778G": 8,
        "Exynos 9810": 7,
        "Spreadtrum SC8830": 3,
        "Qualcomm MSM8916": 4,
        "Snapdragon 8 Gen 3": 10,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 1": 9,
        "Snapdragon 8 Gen 1": 9,
        "MediaTek Dimensity 9000": 10,
        "Snapdragon 782G": 8,
        "Snapdragon 695": 7,
        "MediaTek Dimensity 6020": 7,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 1": 9,
        "Snapdragon 8+ Gen 1": 9,
        "Snapdragon 888": 9,
        "Snapdragon 888": 9,
        "Snapdragon 8 Gen 2": 9,
        "MediaTek Dimensity 1300": 8,
        "MediaTek Dimensity 1200-AI": 8,
        "Snapdragon 480": 5,
        "Qualcomm Snapdragon 460": 5,
        "Snapdragon 865": 8,
        "Snapdragon 888": 9,
        "Snapdragon 865": 8,
        "Snapdragon 8+ Gen 1": 9,
        "Snapdragon 870": 9,
        "Snapdragon 865": 8,
        "Snapdragon 865": 8,
        "MediaTek Dimensity 900": 8,
        "MediaTek Dimensity 1200": 8,
        "Snapdragon 765G": 7,
        "Snapdragon 750G": 7,
        "MediaTek Dimensity 1200-AI": 8,
        "Qualcomm Snapdragon 460": 5,
        "Qualcomm Snapdragon 690": 6,
        "Snapdragon 865": 8,
        "Snapdragon 855": 8,
        "Snapdragon 845": 8,
        "Snapdragon 835": 7,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 2": 9,
        "MediaTek Dimensity 8100": 9,
        "Snapdragon 855": 8,
        "Snapdragon 845": 8,
        "Snapdragon 835": 7,
        "Snapdragon 765G": 7,
        "Snapdragon 865": 8,
        "Snapdragon 865": 8,
        "Snapdragon 855": 8,
        "Snapdragon 8 Gen 3": 10,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Elite": 10,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8 Gen 2": 9,
        "MediaTek Dimensity 9000": 10,
        "MediaTek Dimensity 9000": 10,
        "Snapdragon 8 Gen 3": 10,
        "Dimensity 9400": 10,
        "Dimensity 9400": 10,
        "Dimensity 9400": 10,
        "Dimensity 9400": 10,
        "Dimensity 9400": 10,
        "Snapdragon 778G": 8,
        "Dimensity 1200": 8,
        "Snapdragon 870": 9,
        "Dimensity 900": 8,
        "Snapdragon 8 Gen 2": 9,
        "Dimensity 1100": 8,
        "Snapdragon 8 Gen 3": 10,
        "Snapdragon 710": 7,
        "Snapdragon 626": 5,
        "Snapdragon 653": 6,
        "MediaTek Helio P22": 4,
        "Snapdragon 615": 5,
        "Snapdragon 625": 5,
        "Snapdragon 439": 4,
        "Snapdragon 652": 5,
        "MediaTek MT6592": 4,
        "Snapdragon 430": 4,
        "Qualcomm Snapdragon 712": 7,
        "Qualcomm Snapdragon 712": 7,
        "Qualcomm Snapdragon 675": 6,
        "Qualcomm Snapdragon 675": 6,
        "MediaTek Helio P35": 5,
        "MediaTek Helio P35": 5,
        "MediaTek Helio P65": 6,
        "MediaTek Helio P65": 6,
        "Qualcomm Snapdragon 439": 4,
        "Qualcomm Snapdragon 439": 4,
        "MediaTek Helio P70": 6,
        "MediaTek Helio P70": 6,
        "Qualcomm Snapdragon 710": 7,
        "Qualcomm Snapdragon 710": 7,
        "MediaTek Helio P35": 5,
        "MediaTek Helio P35": 5,
        "Qualcomm Snapdragon 712": 7,
        "Qualcomm Snapdragon 712": 7,
        "Qualcomm Snapdragon 660": 6,
        "Qualcomm Snapdragon 660": 6,
        "MediaTek Helio G96": 6,
        "MediaTek Helio G96": 6,
        "MediaTek Helio G80": 6,
        "MediaTek Helio G80": 6,
        "Qualcomm Snapdragon 870": 9,
        "Qualcomm Snapdragon 870": 9,
        "Qualcomm Snapdragon 765G": 7,
        "Qualcomm Snapdragon 765G": 7,
        "MediaTek Dimensity 700": 7,
        "MediaTek Dimensity 700": 7,
        "Snapdragon 8 Gen 3": 10,
        "Dimensity 9300": 10,
        "Snapdragon 8 Gen 2": 9,
        "Dimensity 9200": 9,
        "Snapdragon 8+ Gen 1": 8.5,
        "Snapdragon 8 Gen 1": 8,
        "Dimensity 9000+": 8,
        "Dimensity 9000": 8,
        "Snapdragon 888": 7.5,
        "Snapdragon 870": 7.5,
        "Dimensity 8200": 7,
        "Dimensity 8100": 7,
        "Dimensity 1300": 6.5,
        "Dimensity 1200": 6.5,
        "Snapdragon 7 Gen 3": 6.5,
        "Snapdragon 778G": 6,
        "Snapdragon 855": 6,
        "Dimensity 8350": 6,
        "Dimensity 7300": 5.5,
        "Dimensity 7050": 5,
        "Snapdragon 750G": 5,
        "Snapdragon 695": 4.5,
        "Snapdragon 685": 4,
        "Snapdragon 680 4G": 4,
        "Dimensity 920": 4,
        "Dimensity 900": 4,
        "Dimensity 6300": 3.5,
        "Snapdragon 675": 3,
        "Snapdragon 6s 4G Gen 1": 3,
        "Helio G100": 3,
        "Helio P35": 2,
        "Snapdragon 8 Elite": 10,
        "Snapdragon 8s Gen 3": 9.5,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 870": 8,
        "Snapdragon 865": 8,
        "Dimensity 1000+": 8,
        "Dimensity 1000L": 7.5,
        "Dimensity 8100": 8,
        "Dimensity 8000-Max": 7.5,
        "Dimensity 1200": 7.5,
        "Snapdragon 782G": 7.5,
        "Snapdragon 7+ Gen 3": 7.5,
        "Snapdragon 7+ Gen 2": 7.5,
        "Dimensity 7200": 7,
        "Dimensity 7300 Energy": 7,
        "Snapdragon 7 Plus Gen 3": 7,
        "Snapdragon 768G": 6.5,
        "Snapdragon 765G": 6,
        "Snapdragon 7s Gen 3": 6,
        "Snapdragon 7s Gen 2": 6,
        "Snapdragon 7s Gen 1": 5.5,
        "Snapdragon 782G": 7,
        "Snapdragon 695": 5,
        "Snapdragon 680": 4.5,
        "Snapdragon 6s Gen 1": 4,
        "Snapdragon 480": 3.5,
        "Dimensity 810": 5,
        "Dimensity 8100": 8,
        "Dimensity 720": 4.5,
        "Dimensity 700": 4,
        "Dimensity 6020": 4,
        "Dimensity 6100+": 4,
        "Helio G99": 4,
        "Helio G88": 3.5,
        "Helio G85": 3.5,
        "Unisoc T612": 2.5,
        "Helio P35": 2,
        "Snapdragon 870": 9,
        "Snapdragon 765G": 6,
        "Dimensity 1000+": 8,
        "Dimensity 865": 8,
        "Dimensity 1000L": 7.5,
        "MediaTek Dimensity 6020": 4,
        "MediaTek Dimensity 700": 4,
        "MediaTek Dimensity 810": 5,
        "Qualcomm Snapdragon 480": 3.5,
        "MediaTek Dimensity 720": 4.5,
        "Qualcomm Snapdragon 6s Gen 1": 4,
        "Qualcomm Snapdragon 695": 5,
        "MediaTek Dimensity 8000-Max": 7.5,
        "MediaTek Dimensity 1200": 7.5,
        "Qualcomm Snapdragon 768G": 6.5,
        "Qualcomm Snapdragon 782G": 7.5,
        "Qualcomm Snapdragon 8 Elite": 10,
        "Qualcomm Snapdragon 8s Gen 3": 9.5,
        "Qualcomm Snapdragon 7 Plus Gen 3": 7,
        "Qualcomm Snapdragon 7s Gen 3": 6,
        "MediaTek Dimensity 7300 Energy": 7,
        "Qualcomm Snapdragon 7s Gen 2": 6,
        "MediaTek Dimensity 7200": 7,
        "MediaTek Dimensity 6100+": 4,
        "Qualcomm Snapdragon 7+ Gen 2": 7.5,
        "MediaTek Dimensity 8100": 8,
        "Qualcomm Snapdragon 7+ Gen 3": 7.5,
        "Qualcomm Snapdragon 7s Gen 1": 5.5,
        "MediaTek Helio G99": 4,
        "MediaTek Helio G88": 3.5,
        "MediaTek Helio G85": 3.5,
        "Unisoc T612": 2.5,
        "Qualcomm Snapdragon 680": 4.5,
        "Snapdragon 8 Elite": 10,
        "Snapdragon 8 Gen 3": 9.8,
        "Snapdragon 8 Gen 2": 9.5,
        "Snapdragon 8+ Gen 1": 9.2,
        "Snapdragon 8 Gen 1": 9.0,
        "Snapdragon 888+ 5G": 8.7,
        "Snapdragon 888 4G": 8.5,
        "Kirin 9010": 9.3,
        "Kirin 9000S": 9.1,
        "Kirin 9000 5G": 9.0,
        "Kirin 990E 5G": 8.0,
        "Snapdragon 855": 8.2,
        "Snapdragon 778G 4G": 7.8,
        "Snapdragon 7+ Gen 2": 7.7,
        "Snapdragon 7s Gen 2": 6.8,
        "Snapdragon 7s Gen 3": 6.5,
        "Snapdragon 695 5G": 5.5,
        "Snapdragon 680 4G": 4.5,
        "Snapdragon 670": 5.0,
        "Snapdragon 765G": 6.0,
        "Snapdragon 730G": 5.8,
        "Snapdragon 480+ 5G": 3.8,
        "Snapdragon 480": 3.5,
        "MediaTek Dimensity 7200": 7.0,
        "MediaTek Helio G99": 4.0,
        "MediaTek Helio G88": 3.7,
        "MediaTek Helio G85": 3.5,
        "MediaTek Helio G37": 2.5,
        "MediaTek G35": 2.5,
        "Unisoc T612": 2.5,
        "Unisoc T606": 2.3,
        "Unisoc SC9863A": 2.0,
        "Google Tensor": 6,
        "Google Tensor G2": 7.5,
        "Google Tensor G3": 8.5,
        "Google Tensor G4": 9.0,
        "MediaTek Helio A22": 1.8,
        "MediaTek Helio G99": 4.0,
        "Unisoc SC9863A": 2.0,
        "MediaTek Helio G80": 3.5,
        "MediaTek Dimensity 810": 5.0,
        "MediaTek Dimensity 6100+": 5.0,
        "MediaTek Dimensity 6020": 4.5,
        "Unisoc SC9832E": 1.8,
        "MediaTek Helio G85": 3.5,
        "MediaTek Dimensity 9200+": 9.0,
        "MediaTek Dimensity 8050": 7.0,
        "MediaTek Dimensity 8200": 8.0,
        "MediaTek Dimensity 8100": 8.0,
        "MediaTek Dimensity 900": 4.0,
        "Unisoc T606": 2.3,
        "MediaTek Dimensity 7200": 7.0,
        "MediaTek Dimensity 9000": 9.0,
        "MediaTek Dimensity 9200": 9.0,
        "MediaTek Helio G88": 3.5,
        "Qualcomm Snapdragon 778G": 6.5,
        "MediaTek Dimensity 8020": 6.5,
        "Unisoc T610": 2.5,
        "Unisoc T616": 2.6,
        "MediaTek Helio G37": 2.5,
        "MediaTek Helio G96": 3.5,
        "MediaTek Helio G25": 2.0,
        "MediaTek Helio G70": 3.0,
        "MediaTek Helio G35": 2.5,
        "MediaTek Helio A25": 1.7,
        "Qualcomm Snapdragon 680": 4.5,
        "MediaTek Helio A20": 2,
        "MediaTek Helio G80": 5,
        "MediaTek Helio A25": 2,
        "MediaTek Helio G90T": 6,
        "MediaTek Helio G70": 4,
        "Kirin 710F": 4,
        "Kirin 985 5G": 7,
        "Kirin 990 5G": 8,
        "Kirin 820 5G": 6,
        "MediaTek Dimensity 800": 6,
        "Kirin 710A": 4,
        "MediaTek Dimensity 1000+": 8,
        "Qualcomm Snapdragon 778G": 7,
        "MediaTek Dimensity 900": 6,
        "MediaTek Dimensity 700": 5,
        "MediaTek Dimensity 800U": 6,
        "Unisoc T610": 3,
        "Qualcomm Snapdragon 888": 9,
        "Qualcomm Snapdragon 888+": 9,
        "Qualcomm Snapdragon 778G+": 7,
        "Qualcomm Snapdragon 695": 6,
        "MediaTek Dimensity 810": 6,
        "MediaTek MT6762G Helio G25": 2,
        "Qualcomm Snapdragon 8 Gen 1": 9,
        "MediaTek Dimensity 8000": 8,
        "MediaTek Dimensity 9000": 9,
        "MediaTek Helio G37": 2,
        "MediaTek Dimensity 6020": 5,
        "Qualcomm Snapdragon 8 Gen 2": 10,
        "Qualcomm Snapdragon 8+ Gen 1": 9,
        "Qualcomm Snapdragon 782G": 8,
        "Qualcomm Snapdragon 6 Gen 1": 6,
        "MediaTek Helio G36": 2,
        "MediaTek Dimensity 6100+": 5,
        "Qualcomm Snapdragon 8 Gen 3": 10,
        "Qualcomm Snapdragon 7 Gen 1": 7,
        "Qualcomm Snapdragon 662": 4,
        "MediaTek MT8768T": 2,
        "MediaTek Dimensity 1300T": 8,
        "Qualcomm Snapdragon 680": 5,
        "MediaTek MT8786": 4,
        "MediaTek Dimensity 8020": 7,
        "MediaTek Dimensity 8100": 8,
        "Qualcomm Snapdragon 685": 5,
        "Qualcomm Snapdragon 7s Gen 2": 7,
        "Snapdragon 865": 8,
        "Snapdragon 720G": 6,
        "Snapdragon 732G": 5,
        "Snapdragon 662": 3,
        "Snapdragon 870": 8,
        "Snapdragon 860": 7,
        "MediaTek Dimensity 700": 4,
        "MediaTek Dimensity 1200": 7,
        "MediaTek Dimensity 1100": 6,
        "MediaTek Dimensity 810": 5,
        "Snapdragon 8 Gen 1": 8,
        "Snapdragon 695": 4,
        "MediaTek Helio G96": 4,
        "MediaTek Helio G99": 5,
        "MediaTek Helio G95": 4,
        "Snapdragon 7+ Gen 2": 8,
        "Snapdragon 8+ Gen 1": 9,
        "Snapdragon 778G": 6,
        "MediaTek Helio G88": 3,
        "Snapdragon 4 Gen 1": 3,
        "MediaTek Dimensity 8100": 8,
        "MediaTek Dimensity 8300": 9,
        "Snapdragon 8 Gen 2": 9,
        "Snapdragon 8+ Gen 2": 9,
        "MediaTek Helio G85": 3,
        "MediaTek Dimensity 8200": 8,
        "MediaTek Dimensity 8400": 9,
        "MediaTek Dimensity 7025": 6,
        "Snapdragon 7s Gen 2": 6,
        "Snapdragon 8 Gen 3": 10,
        "Snapdragon 8 Elite": 10,
        "Snapdragon 7s Gen 3": 7,
        "Snapdragon 8s Gen 3": 9,
        "Dimensity 7300": 6,
        "Dimensity 9400+": 10,
        "Tensor G4": 9,
        }


      proc_a = sr.loc[sr["Model Name"] == model_a, "Processor"].values[0]
      proc_b = sr.loc[sr["Model Name"] == model_b, "Processor"].values[0]


      rank_a = processor_rank.get(proc_a, 0)
      rank_b = processor_rank.get(proc_b, 0)


      fig, ax = plt.subplots(figsize=(3, 1))
      bars = ax.bar([model_a, model_b], [rank_a, rank_b], color=["skyblue", "lightgreen"])
      ax.set_ylabel("Processor Rank")
      ax.set_title("Processor Comparison")
      ax.tick_params(axis='x', labelsize=5)   
      ax.tick_params(axis='y', labelsize=6)   

    
      ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))


      for bar, proc in zip(bars, [proc_a, proc_b]):
          height = bar.get_height()
          ax.text(
              bar.get_x() + bar.get_width() / 2, 
              height + 0.1,
              proc,
              ha="center", va="bottom", fontsize=5, rotation=0
        )

      st.pyplot(fig)


      if rank_a == rank_b:
          result_text = f"📱 Both {model_a} and {model_b} have similar processor ranking."
      else:
          better = model_a if rank_a > rank_b else model_b
          result_text = f"📱 {better} has a better processor!"
      st.markdown(
          f"""
          <div style="border:2px solid white; padding:10px; border-radius:10px; 
                      text-align:center; color:white; font-weight:bold; font-size:18px;">
              {result_text}
          </div>
          """,
          unsafe_allow_html=True
        )
      st.markdown(f"<h2 style='color:white;'>➡️What the chart shows :</h2>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Compares processor “Rank” for two Phone models. </h3>", unsafe_allow_html=True)  
      st.markdown(f"<h2 style='color:white;'>➡️How to read it :</h2>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Xaxis: device and processor label (model + chip).</h3>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Yaxis: Processor Rank on a 0 to 10 scale. </h3>", unsafe_allow_html=True)  
      
    with t2:
     
      
     try:
        battery_a = sr.loc[sr['Model Name'] == model_a, 'Battery Capacity'].values[0]
        battery_b = sr.loc[sr['Model Name'] == model_b, 'Battery Capacity'].values[0]
        def clean_battery(val):
         if isinstance(val, str):
          val = re.sub(r'[^0-9]', '', val)  
          return int(val)

        battery_a = clean_battery(battery_a)
        battery_b = clean_battery(battery_b)
    
        fig, ax = plt.subplots(figsize=(3,1))
        ax.bar([model_a, model_b], [battery_a, battery_b], color=["#3DFF33", "#3DFF33"])
        ax.set_ylabel("Battery (mAh)")
        ax.set_ylim(0, max(battery_a, battery_b) + 500)  
        ax.tick_params(axis='x', labelsize=5)   
        ax.tick_params(axis='y', labelsize=5)   


        ax.set_title("Battery Capacity Comparison")
        ax.grid(axis="y", linestyle="--", alpha=0.6)

        
        for i, val in enumerate([battery_a, battery_b]):
            ax.text(i, val + 50, str(val), ha='center', fontsize=9, fontweight='bold')

        st.pyplot(fig)
        Bat = model_a if battery_a > battery_b else model_b
        st.markdown(
          f"""
          <div style="border:2px solid white; padding:10px; border-radius:10px; 
                      text-align:center; color:white; font-weight:bold; font-size:18px;">
         📱 {Bat} Phone have Better Battery.
         </div>
         """,unsafe_allow_html=True)

     except IndexError:
         st.error("Battery data not available for one of the selected models.")
     st.markdown(f"<h2 style='color:white;'>➡️What the chart shows : </h2>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Compares battery capacity (mAh) for two Phone models. </h3>", unsafe_allow_html=True)  
     st.markdown(f"<h2 style='color:white;'>➡️How to read it :</h2>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Xaxis: device models.</h3>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Yaxis:  Battery (mAh).</h3>", unsafe_allow_html=True) 
     
     
      
    with t3:
      st.title("📸 Back Camera Comparison")
      try:
    
        backcam_a = sr.loc[sr['Model Name'] == model_a, 'Back Camera'].values[0]
        backcam_b = sr.loc[sr['Model Name'] == model_b, 'Back Camera'].values[0]
        def clean_camera(val):
         if isinstance(val, str):
            
            nums = re.findall(r'\d+', val)
            return sum(map(int, nums)) if nums else 0
         return int(val) if isinstance(val, (int, float)) else 0
        backcam_a = clean_camera(backcam_a)
        backcam_b = clean_camera(backcam_b)

        fig, ax = plt.subplots(figsize=(3, 1))
        ax.bar([model_a, model_b], [backcam_a, backcam_b], color=['#8E44AD', '#27AE60'])
        ax.set_ylabel('Back Camera (MP)',fontsize=5)

        ax.set_ylim(0, max(backcam_a, backcam_b) + 10)
        ax.tick_params(axis='x', labelsize=5)   
        ax.tick_params(axis='y', labelsize=6)   


        for i, val in enumerate([backcam_a, backcam_b]):
         ax.text(i, val + 1, str(val) + " MP", ha='center', fontsize=9, fontweight='bold')

        st.pyplot(fig)
        og = model_a if backcam_a > backcam_b else model_b
        st.markdown(
          f"""
          <div style="border:2px solid white; padding:10px; border-radius:10px; 
                      text-align:center; color:white; font-weight:bold; font-size:18px;">
         📱 {og} Phone have Better Back Camera.
         </div>
         """,unsafe_allow_html=True)

      except KeyError:
       st.error("⚠️ Column 'Back Camera' not found in dataset.")
      except IndexError:
       st.error("⚠️ One of the selected models not found in dataset.")
      st.markdown(f"<h2 style='color:white;'>➡️What the chart shows :</h2>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Compares rear camera resolution (megapixels) for two Phone models. </h3>", unsafe_allow_html=True)  
      st.markdown(f"<h2 style='color:white;'>➡️How to read it :</h2>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Xaxis: device models.</h3>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Yaxis: Back Camera (MP).</h3>", unsafe_allow_html=True) 
    
    with t4:
     
     st.title("💾 RAM Comparison")
     try:
        RAM_a = sr.loc[sr['Model Name'] == model_a, 'RAM'].values[0]
        RAM_b = sr.loc[sr['Model Name'] == model_b, 'RAM'].values[0]

        def clean_ram(val):
         if isinstance(val, str):
            val = re.sub(r'[^0-9]', '', val)  
            return int(val)
         return int(val)

        ram_a = clean_ram(RAM_a)
        ram_b = clean_ram(RAM_b)

        fig, ax = plt.subplots(figsize=(3, 1))


        ax.bar([model_a, model_b],
           [ram_a, ram_b],
           color=['#3498DB', '#E67E22'],
           width=0.5)

        ax.set_xlabel("Phone Models", fontsize=6)   
        ax.set_ylabel("RAM (GB)", fontsize=8)       
        ax.set_ylim(0, 16)  
        ax.set_yticks(list(range(0, 18, 2)))  

    
        ax.tick_params(axis='x', labelsize=5)   
        ax.tick_params(axis='y', labelsize=5)   

        ax.set_title("RAM Comparison", fontsize=11)
    

        for i, val in enumerate([ram_a, ram_b]):
          ax.text(i, val + 0.5, f"{val} GB", ha='center', fontsize=8, fontweight='bold')

        st.pyplot(fig)
        rog = model_a if ram_a > ram_b else model_b
        st.markdown(
          f"""
          <div style="border:2px solid white; padding:10px; border-radius:10px; 
                      text-align:center; color:white; font-weight:bold; font-size:18px;">
         📱 {rog} Phone have Better Ram.
         </div>
         """,unsafe_allow_html=True)
     except KeyError:
      st.error("⚠️ Column 'RAM' not found in dataset.")
     except IndexError:
      st.error("⚠️ One of the selected models not found in dataset.")
     st.markdown(f"<h2 style='color:white;'>➡️What the chart shows : </h2>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Compares RAM for two Phone models. </h3>", unsafe_allow_html=True)  
     st.markdown(f"<h2 style='color:white;'>➡️How to read it :</h2>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Xaxis: Phone models.</h3>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Yaxis: RAM (GB).</h3>", unsafe_allow_html=True) 


    with t5:
     
     st.title("🤳 Front Camera Comparison")
     try:
        Frontcam_a = sr.loc[sr['Model Name'] == model_a, 'Front Camera'].values[0]
        Frontcam_b = sr.loc[sr['Model Name'] == model_b, 'Front Camera'].values[0]

        def clean_camera(val):
         if isinstance(val, str):
            nums = re.findall(r'\d+', val)
            return sum(map(int, nums)) if nums else 0
         return int(val) if isinstance(val, (int, float)) else 0

        Frontcam_a = clean_camera(Frontcam_a)
        Frontcam_b = clean_camera(Frontcam_b)

        fig, ax = plt.subplots(figsize=(3, 1))
        ax.bar([model_a, model_b],
           [Frontcam_a, Frontcam_b],
           color=["#AD4444", "#2739AE"])

        ax.set_ylabel('Front Camera (MP)',fontsize=5)
        ax.set_ylim(0, max(Frontcam_a, Frontcam_b) + 10)


        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=5)

    
        for i, val in enumerate([Frontcam_a, Frontcam_b]):
            ax.text(i, val + 1, str(val) + " MP",
                 ha='center', fontsize=8, fontweight='bold')

        st.pyplot(fig)
        Front = model_a if Frontcam_a > Frontcam_b else model_b
        st.markdown(
          f"""
          <div style="border:2px solid white; padding:10px; border-radius:10px; 
                      text-align:center; color:white; font-weight:bold; font-size:18px;">
        📱 {Front} has Better Front Camera.
        </div>
        """,
        unsafe_allow_html=True
        )
     except KeyError:
      st.error("⚠️ Column 'Back Camera' not found in dataset.")
     except IndexError:
      st.error("⚠️ One of the selected models not found in dataset.")
     st.markdown(f"<h2 style='color:white;'>➡️What the chart shows : </h2>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Compares front camera resolution (megapixels) for two Phone models. </h3>", unsafe_allow_html=True)  
     st.markdown(f"<h2 style='color:white;'>➡️How to read it :</h2>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Xaxis: Phone models.</h3>", unsafe_allow_html=True)  
     st.markdown(f"<h3 style='color:white;'>Yaxis:  Front Camera (MP).</h3>", unsafe_allow_html=True) 
    
    with t6:
      st.subheader("📅 Launch Year Comparison")
      try:
        year_a = sr.loc[sr['Model Name'] == model_a, 'Launch Year']
        year_b = sr.loc[sr['Model Name'] == model_b, 'Launch Year']

        if year_a.empty or year_b.empty:
           st.error("⚠️ One of the selected models was not found in the dataset.")
        else:
        
         launch_a = int(year_a.values[0])
         launch_b = int(year_b.values[0])

        fig, ax = plt.subplots(figsize=(3, 1))
        ax.bar([model_a, model_b],
               [launch_a, launch_b],
               color=['#2ECC71', '#9B59B6'],
               width=0.5)

        ax.set_xlabel("Phone Models", fontsize=5)
        ax.set_ylabel("Launch Year", fontsize=5)

        ymin = min(launch_a, launch_b) - 1
        ymax = max(launch_a, launch_b) + 1
        ax.set_ylim(ymin, ymax)
        ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        ax.tick_params(axis='x', labelsize=5, rotation=0)
        ax.tick_params(axis='y', labelsize=5)

        ax.set_title("Launch Year Comparison", fontsize=11)

        for i, val in enumerate([launch_a, launch_b]):
            ax.text(i, val + 0.1, str(val), ha='center', fontsize=7, fontweight='bold')

        st.pyplot(fig)
        diff = abs(launch_a - launch_b)
        newer = model_a if launch_a > launch_b else model_b

        st.markdown(
          f"""
          <div style="border:2px solid white; padding:10px; border-radius:10px; 
                      text-align:center; color:white; font-weight:bold; font-size:18px;">
        📱 {newer} is newer by {diff} years.
        </div>
        """,
        unsafe_allow_html=True
        )
 
      except Exception as e:
        st.error(f"⚠️ Error: {e}")
      st.markdown(f"<h2 style='color:white;'>➡️What the chart shows : </h2>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Compares release years for two Phone models.</h3>", unsafe_allow_html=True)  
      st.markdown(f"<h2 style='color:white;'>➡️How to read it :</h2>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Xaxis: Phone models.</h3>", unsafe_allow_html=True)  
      st.markdown(f"<h3 style='color:white;'>Yaxis: Launch Year.</h3>", unsafe_allow_html=True) 
    

elif selected =="Price Comparison":
    st.markdown("""
    <style>
    /* Change background color */
    .main {
        background-color: #0a0a0a;  /* dark background for better white contrast */
    }

    /* Change title and header text color to white */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    
    </style>
    """, unsafe_allow_html=True)


    st.title("📈 Price Comparison Page")
    st.header("📈 Graphical Comparison of Price:")
    sr.head(5)
    st.markdown("""
    <style>
    /* Style the entire tab container */
    [data-testid="stTabs"] div[role="tablist"] {
    background-color: #f5f5f5;
    padding: 8px;
    border-radius: 10px;
    gap: 10px;
    display: flex;
    justify-content: flex-start;
    }

    /* Style for active tab */
    [data-testid="stTab"][aria-selected="true"] {
    background-color: #004080 !important;  /* Deep blue */
    color: #ffffff !important;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 8px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    /* Style for inactive tabs */
    [data-testid="stTab"][aria-selected="false"] {
    background-color: #e0e0e0 !important;  /* light gray */
    color: #333333 !important;
    padding: 8px 16px;
    border-radius: 8px;
    transition: 0.3s ease;
    }

    /* Hover effect */
    [data-testid="stTab"]:hover {
    background-color: #cfcfcf !important;
    color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    conversion_rates = {
    "INR": 1,       
    "USD": 83.0,    
    "PKR": 0.30,    
    "AED": 22.6,    
    "CNY": 11.5     
    }


    phone1 = st.session_state.get("phone1")
    phone2 = st.session_state.get("phone2")

    if not phone1 or not phone2:
     st.warning("Please select two phones on the Comparison page first.")
     st.stop()


    df_selected = sr[sr['Model Name'].isin([phone1, phone2])]


    price_columns = [col for col in df_selected.columns if 'Price' in col]


    country_labels = []
    for col in price_columns:
       if "INR" in col:
        country_labels.append("India (₹)")
       elif "USD" in col:
        country_labels.append("USA ($)")
       elif "PKR" in col:
        country_labels.append("Pakistan (₨)")
       elif "AED" in col:
        country_labels.append("Dubai (د.إ)")
       elif "CNY" in col:
        country_labels.append("China (¥)")
       else:
        country_labels.append(col)


    def get_converted_prices(phone):
      prices_in_inr = []
      for col in price_columns:
        raw_value = df_selected[df_selected['Model Name'] == phone][col].values[0]

        if raw_value is None:
            prices_in_inr.append(0)
            continue

        
        value_str = str(raw_value)
        value_str = re.sub(r'[^\d.]', '', value_str)  

        if value_str == '':
            prices_in_inr.append(0)
            continue

        price_num = float(value_str)

        
        if "INR" in col:
            rate = conversion_rates["INR"]
        elif "USD" in col:
            rate = conversion_rates["USD"]
        elif "PKR" in col:
            rate = conversion_rates["PKR"]
        elif "AED" in col:
            rate = conversion_rates["AED"]
        elif "CNY" in col:
            rate = conversion_rates["CNY"]
        else:
            rate = 1

        prices_in_inr.append(price_num * rate)
      return prices_in_inr


    prices_phone1 = get_converted_prices(phone1)
    prices_phone2 = get_converted_prices(phone2)


    fig = go.Figure()

    fig.add_trace(go.Bar(
     x=country_labels,
     y=prices_phone1,
     name=phone1,
     marker=dict(color="#4CAF50", line=dict(width=1.5, color='black')),
     text=[f"{int(val):,}" for val in prices_phone1],                 
     textposition='outside' 
    ))
    fig.add_trace(go.Bar(
     x=country_labels,
     y=prices_phone2,
     name=phone2,
     marker=dict(color="#FF5733", line=dict(width=1.5, color='black')),  
     text=[f"{int(val):,}" for val in prices_phone2],                  
     textposition='outside'  
    ))

    fig.update_layout(
     title=f"Price Comparison in Different Currency (₹,$,₨,د.إ,¥): {phone1} vs {phone2}",
     xaxis_title="Country (Currency)",
     yaxis_title="Price in Different Currencies",
     barmode='group',
     xaxis=dict(
        ticktext=[f"<b>{label}</b>" for label in country_labels],
        tickvals=country_labels,
        tickfont=dict(
            color="black",
            size=14
        )
       ),
    
     
     yaxis=dict(
       tickvals=[0, 50000, 100000, 150000, 200000],
       ticktext=["<b>Cheap</b>", "<b>Mid Cheap</b>","<b>Mid Range</b>", "<b>Expensive</b>", "<b>Most Expensive</b>"],
       tickfont=dict(
          color="black", 
          size=14          
        ),
     range=[0, 210000] 
    )
    )
    st.plotly_chart(fig)
elif selected =="Tutorial":
    st.markdown("<h1 style='color: white;'>Tutorial Video For Project :</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: white;'>Battle Specs ⚔️📱</h2>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    .centered-button .stButton > button {
        width: 200px;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        background-color: #ff4b4b;
        color: white;
        border: none;
        border-radius: 8px;
        display: block;
        margin: 20px auto;
    }
    </style>
""", unsafe_allow_html=True)


    st.video("tutorial video.mp4")
    
        