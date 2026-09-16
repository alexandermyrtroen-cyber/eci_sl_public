import streamlit as st

st.set_page_config(page_title="ECI Command Center", layout="wide")

# Read and render the true HTML layout
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()
    st.components.v1.html(html_data, width=None, height=1200, scrolling=True)
except FileNotFoundError:
    st.error("SYSTEM ERROR: index.html master layout not found in directory.")
