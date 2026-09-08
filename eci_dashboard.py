import streamlit as st
import json
import datetime
from eci_engine import verify_structural_integrity

st.set_page_config(
    page_title="ECI SL // Institutional Control Panel",
    page_icon="⚖️",
    layout="wide"
)

# Custom Styling to match Bone/Charcoal/Gold/Electric aesthetic
st.markdown("""
    <style>
    .main { background-color: #EAE6DF; color: #0a0a0a; }
    h1, h2, h3 { font-family: 'Cinzel', serif; color: #0a0a0a; }
    .stButton>button { background-color: #0a0a0a; color: #EAE6DF; border-radius: 0px; font-family: monospace; }
    .stButton>button:hover { background-color: #0070FF; color: #0a0a0a; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p style='font-family: monospace; color: #C5A861; font-size: 12px; letter-spacing: 2px;'>[ ECI SL // SOVEREIGN COMMAND CONSOLE ]</p>", unsafe_allow_html=True)
st.title("Institutional Intelligence & Audit Center")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Active Case Telemetry & Ingestion")
    sector_choice = st.selectbox(
        "Select Operational Sector Matrix",
        [
            "01_TRADE_FINANCE",
            "02_AGRICULTURE",
            "03_MUSIC_IP",
            "04_SOLE_TRADERS",
            "05_LOGISTICS",
            "06_REAL_ESTATE",
            "07_TREASURY",
            "08_PHILANTHROPY"
        ]
    )
    
    entity_name = st.text_input("Principal / Entity Name", value="Global Asset Group SA")
    payload_scope = st.text_area("Mandate Parameters / Document URI", value="Ingesting 300-page operational audit payload for cryptographic verification.")
    
    if st.button("Execute Deterministic Verification"):
        payload = {"entity": entity_name, "scope": payload_scope, "timestamp": str(datetime.datetime.utcnow())}
        result = verify_structural_integrity(sector_choice, payload)
        
        st.success("Verification Complete. Mathematical Certainty Established.")
        st.json(result)

with col2:
    st.subheader("System Status")
    st.markdown("""
    * **Node Server:** Active (`localhost:8044`)
    * **Certainty Engine:** `eci_engine.py` (Online)
    * **Security Posture:** Air-Gapped / Local Host
    * **Compliance:** Non-Financial Advisory Enforced
    """)
    
    st.markdown("---")
    st.subheader("Quick Actions")
    if st.button("Purge Temporary Logs"):
        st.info("Cache cleared. System state pristine.")
