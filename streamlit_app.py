import streamlit as st
import requests

# Configuration Supabase
SUPABASE_URL = "https://ymjabtkhikeofdfyltra.supabase.co"   # remplace par ton URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InltamFidGtoaWtlb2ZkZnlsdHJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NzE2MjEsImV4cCI6MjA4MDI0NzYyMX0.2fdaFWK5oFz405ECG0qhXN3Z2KCjLS54kuA9XCuEfDM"                       # remplace par ta clé

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}
st.title("StockOpsLab WMS apps")
st.title("Open source project for training")
st.write("Test connexion Supabase")
st.write(" Under construction ")

# Lire tous les enregistrements de la table t_user
if st.button("Afficher les utilisateurs"):
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/t_user",
        headers=headers,
        params={"select": "*"}
    )
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Erreur {response.status_code}: {response.text}")

# Ajouter un utilisateur
name = st.text_input("Nom")
email = st.text_input("Email")

if st.button("Ajouter"):
    new_user = {"f_name": name, "email": email}
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/t_user",
        headers=headers,
        json=new_user
    )
    if response.status_code in (200, 201):
        st.success("Utilisateur ajouté !")
    else:
        st.error(f"Erreur {response.status_code}: {response.text}")



