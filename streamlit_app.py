import streamlit as st
import requests

# Configuration Supabase
SUPABASE_URL = "https://ymjabtkhikeofdfyltra.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InltamFidGtoaWtlb2ZkZnlsdHJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NzE2MjEsImV4cCI6MjA4MDI0NzYyMX0.2fdaFWK5oFz405ECG0qhXN3Z2KCjLS54kuA9XCuEfDM"  
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}
st.title("StockOpsLab WMS apps")
st.title("Open source project for training")
st.write("Test connexion Supabase")
st.write(" Under construction ")

# Formulaire de saisie
with st.form("login_form"):
    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    submitted = st.form_submit_button("OK")

if submitted:
    # Appel RPC à la fonction SQL
    result = supabase.rpc("check_password", {"p_email": email, "p_password": password}).execute()
    is_valid = bool(result.data)  # True si mot de passe correct

    if is_valid:
        st.success("Connexion réussie ✅")
        # Redirection vers la page pages/homepage.py
        st.switch_page("pages/homepage.py")
    else:
        st.error("Erreur de mot de passe")





