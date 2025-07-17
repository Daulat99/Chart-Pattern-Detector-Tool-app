
import streamlit as st
import pandas as pd
from patterns import (
    detect_double_top,
    detect_double_bottom,
    detect_head_and_shoulders,
    detect_inverse_head_and_shoulders,
    detect_bullish_flag,
    detect_bearish_flag
)

st.set_page_config(page_title="Chart Pattern Detector", layout="wide")
st.title("🧠 Chart Pattern Detection Tool")

uploaded_file = st.file_uploader("Upload your CSV file (Open-High-Low-Close)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Chart Preview")
    st.dataframe(df.tail(30))

    with st.expander("🔍 Detected Patterns"):
        dt_msg, *_ = detect_double_top(df)
        db_msg, *_ = detect_double_bottom(df)
        hs_msg, *_ = detect_head_and_shoulders(df)
        ihs_msg, *_ = detect_inverse_head_and_shoulders(df)
        bf_msg, *_ = detect_bullish_flag(df)
        brf_msg, *_ = detect_bearish_flag(df)

        for msg in [dt_msg, db_msg, hs_msg, ihs_msg, bf_msg, brf_msg]:
            if msg:
                st.success(msg)
            else:
                st.warning("No pattern found.")
