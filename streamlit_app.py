import streamlit as st

st.title("📈 StockOpsLab")
st.subheader("🚧 Application en construction 🚧")

st.write("Bienvenue sur **StockOpsLab** !")

col1, col2, col3 = st.columns([1,2,1])  # colonne centrale plus large
with col2:
    st.title("📈 StockOpsLab")
    st.subheader("🚧 Application en construction 🚧")
    st.write("Bienvenue sur **StockOpsLab** !")

