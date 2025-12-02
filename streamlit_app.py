import streamlit as st

#### CSS
st.markdown(
    """
    <style>
    .css-1y0tuds {  /* titre principal */
        text-align: center;
    }
    .css-1offfwp h2 {  /* subheader */
        text-align: center;
    }
    .css-1offfwp p {   /* st.write */
        text-align: center;
    }
    /* Ou plus simple : centrer tous les éléments de header */
    h1, h2, h3, h4 {
        text-align: center !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#### CSS
st.title("📈 StockOpsLab 2")
st.subheader("🚧 Under Construction 🚧")
st.write("Welcome on **StockOpsLab** !")

st.markdown(
    """
    <div style="text-align: center;">
        StockOpsLab<br>
        Application en construction<br>
        Bienvenue sur StockOpsLab !
    </div>
    """,
    unsafe_allow_html=True
)

# col1, col2, col3 = st.columns([1,2,1])  # colonne centrale plus large
# with col2:
#    st.title("📈 StockOpsLab")
#    st.subheader("🚧 Application en construction 🚧")
#    st.write("Bienvenue sur **StockOpsLab** !")

