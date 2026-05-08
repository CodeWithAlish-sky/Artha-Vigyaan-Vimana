import streamlit as st
import ccxt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import time

# --- ARTHA-VIGYAN VIMANA CONFIG ---
st.set_page_config(page_title="Artha-Vigyan Vimana", layout="wide")

# --- ANCIENT-MODERN INTERFACE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@300;600&display=swap');
    .stApp { background: radial-gradient(circle at center, #080C14 0%, #010205 100%); color: #F4E4C1; }
    .shakti-btn {
        background: linear-gradient(135deg, #FF9933 0%, #8B4513 100%);
        color: #FFFFFF !important; padding: 24px; text-align: center; border-radius: 4px;
        text-decoration: none; font-weight: bold; display: block; border: 1px solid #D4AF37;
        box-shadow: 0 0 45px rgba(255, 153, 51, 0.4); font-family: 'Cinzel', serif;
        letter-spacing: 4px; transition: 0.5s; margin: 20px 0;
    }
    .shakti-btn:hover { box-shadow: 0 0 80px rgba(255, 153, 51, 0.8); transform: translateY(-3px); }
    div[data-testid="stMetricValue"] { font-family: 'Cinzel', serif; color: #D4AF37 !important; text-shadow: 0 0 20px rgba(212, 175, 55, 0.6); }
    h1 { font-family: 'Cinzel', serif; color: #FF9933; text-align: center; font-size: 3.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- BUDDHI ENGINES (AI & ML) ---
def dharmic_ai(gap):
    if gap > 0.15: return "🔱 DHARMA SIGNAL: High Artha-Siddhi detected. Balance is skewed for wealth."
    return "☸️ DHYANA: Market in Shunya state. Observe the flow with stillness."

def artha_prediction(history):
    if len(history) < 5: return "Reading Akasha..."
    model = LinearRegression().fit(np.array(range(len(history))).reshape(-1, 1), np.array(history))
    pred = model.predict([[len(history)+1]])
    return "VARDHANA (Rising)" if pred > history[-1] else "KSHAYA (Falling)"

# --- MAIN VIMANA INTERFACE ---
st.markdown("<h1>ᴀʀᴛʜᴀ-ᴠɪɢʏᴀɴ ᴠɪᴍᴀɴᴀ</h1>", unsafe_allow_html=True)

if 'stream' not in st.session_state: st.session_state.stream = []

asset = st.sidebar.selectbox("Asset Orbit", ["BTC/USDT", "ETH/USDT", "SOL/USDT"])
st.sidebar.markdown('<a href="#" class="shakti-btn">🔱 SHAKTI-SADHAN 🔱</a>', unsafe_allow_html=True)

placeholder = st.empty()

while True:
    with placeholder.container():
        try:
            p1 = ccxt.binance().fetch_ticker(asset)['last']
            p2 = ccxt.bybit().fetch_ticker(asset)['last']
        except: p1, p2 = 82500.0, 82560.0

        gap = abs(p1 - p2)
        st.session_state.stream.append(gap)
        if len(st.session_state.stream) > 20: st.session_state.stream.pop(0)

        c1, c2, c3 = st.columns(3)
        c1.metric("Binance Gyaan", f"${p1:,.2f}")
        c2.metric("Bybit Gyaan", f"${p2:,.2f}")
        c3.metric("Ansh (Gap)", f"${gap:,.2f}")

        st.write("---")
        col_ai, col_ml = st.columns(2)
        col_ai.info(f"🤖 AI Advisor: {dharmic_ai(gap/p1)}")
        col_ml.success(f"📈 ML Trend: {artha_prediction(st.session_state.stream)}")
        
        st.line_chart(st.session_state.stream)
        st.markdown('<a href="#" class="shakti-btn">🔱 VIGYAN-STHAAN PORTAL 🔱</a>', unsafe_allow_html=True)

        time.sleep(10)
        st.rerun()
