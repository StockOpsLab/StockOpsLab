import streamlit as st

# Variable
VarTxt = "Hello Word"

# Affichage centré avec la nouvelle ligne
st.markdown(
    f"""
    <div style="text-align: center;">
        StockOpsLab<br>
        Application en construction<br>
        Bienvenue sur StockOpsLab !<br>
        {VarTxt}
    </div>
    """,
    unsafe_allow_html=True
)
