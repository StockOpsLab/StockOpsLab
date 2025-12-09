import os
import json
import streamlit as st
import requests
from supabase import create_client

# Configuration Supabase
SUPABASE_URL = "https://ymjabtkhikeofdfyltra.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InltamFidGtoaWtlb2ZkZnlsdHJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NzE2MjEsImV4cCI6MjA4MDI0NzYyMX0.2fdaFWK5oFz405ECG0qhXN3Z2KCjLS54kuA9XCuEfDM"  
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


# Fonction pour appeler le RPC check_password
def check_password(email: str, password: str) -> bool:
    if not email or not password:
        st.warning("Veuillez renseigner email et mot de passe.")
        return False

    try:
        url = f"{SUPABASE_URL}/rest/v1/rpc/check_password"
        payload = {"p_email": email, "p_password": password}
        r = requests.post(url, headers=HEADERS, data=json.dumps(payload))
        r.raise_for_status()
        return bool(r.json())
    except Exception as e:
        st.error("Erreur de connexion au service d’authentification.")
        st.caption(f"Debug: {e}")
        return False

# Fonction sécurisée pour changer de page
def safe_switch_page(path: str):
    if not os.path.exists(path):
        st.error(f"Fichier introuvable : {path}")
        return
    try:
        st.switch_page(path)
    except Exception:
        st.error("Fichier introuvable")

# Interface Streamlit
st.title("Connexion")

with st.form("login_form"):
    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    submitted = st.form_submit_button("OK")

if submitted:
    is_valid = check_password(email, password)
    if is_valid:
        st.success("Connexion réussie ✅")
        safe_switch_page("pages/sol_homepage.py")  # adapte le nom du fichier
    else:
        st.error("Erreur de mot de passe ❌")

# Création du bouton
if st.button("SignUp"):
    # Redirection vers la page sol_signup.py
    st.switch_page("sol_signup.py")

