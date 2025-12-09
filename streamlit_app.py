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
email = st.text_input("Email")
password = st.text_input("Mot de passe", type="password")
ok = st.button("OK")

if ok:
    # Vérification côté base : on utilise crypt() pour comparer
    query = f"""
        SELECT email
        FROM t_user
        WHERE email = %s
          AND password = crypt(%s, password);
    """
    # Exécution de la requête SQL via RPC
    result = supabase.rpc("exec_sql", {"sql": query, "params": [email, password]}).execute()

    if result.data:
        # Connexion réussie → redirection vers homepage
        st.success("Connexion réussie ✅")
        st.switch_page("pages/homepage.py")
    else:
        # Erreur de mot de passe
        st.error("Erreur de mot de passe ❌")





