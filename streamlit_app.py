import streamlit as st
import requests

# Configuration Supabase
SUPABASE_URL = "https://xyzcompany.supabase.co"   # remplace par ton URL
SUPABASE_KEY = "ta_cle_api"                       # remplace par ta clé

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

st.title("Test connexion Supabase")

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
    new_user = {"name": name, "email": email}
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/t_user",
        headers=headers,
        json=new_user
    )
    if response.status_code in (200, 201):
        st.success("Utilisateur ajouté !")
    else:
        st.error(f"Erreur {response.status_code}: {response.text}")



