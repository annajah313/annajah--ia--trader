import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ANNAJAH AI TRADER",
    page_icon="📈",
    layout="wide"
)

st.title("📈 ANNAJAH AI TRADER")
st.caption("Indonesia Stock Market")

st.warning("MODE DEMO - Data belum live")

st.metric("Modal Trading", "Rp50.000.000")
st.metric("Risiko per transaksi", "Rp250.000")
st.metric("Batas rugi harian", "Rp500.000")

st.subheader("Stock Scanner")

data = pd.DataFrame({
    "Saham": ["BBRI", "BMRI", "BBCA", "ANTM"],
    "Sinyal": ["WAIT", "WAIT", "WAIT", "WAIT"],
    "Status": ["DEMO", "DEMO", "DEMO", "DEMO"]
})

st.dataframe(data, use_container_width=True)

st.success("Annajah AI Trader berhasil dijalankan!")
