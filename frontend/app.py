import streamlit as st

# Page Config
st.set_page_config(page_title="PayFast", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .header {
        background-color: #5f259f;
        padding: 15px;
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .offer {
        background-color: #ffe6ff;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">💜 PayFast</div>', unsafe_allow_html=True)

st.write("")

# Wallet Section
st.subheader("Wallet Balance")
st.markdown("## ₹10,250")
st.button("Add Money")

st.write("---")

# Services Grid
st.subheader("Services")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card">📱<br>Mobile Recharge</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">💡<br>Electricity Bill</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">💰<br>Send Money</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card">🏦<br>Bank Transfer</div>', unsafe_allow_html=True)

st.write("---")

# Offers Section
st.subheader("Offers")
st.markdown('<div class="offer">🎁 Get ₹50 Cashback on first payment!</div>', unsafe_allow_html=True)