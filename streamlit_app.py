import requests

# Remplace par ton URL et ta clé
url = "https://stockopslab.streamlit.app/"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InltamFidGtoaWtlb2ZkZnlsdHJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NzE2MjEsImV4cCI6MjA4MDI0NzYyMX0.2fdaFWK5oFz405ECG0qhXN3Z2KCjLS54kuA9XCuEfDM"
table = "t_user"

# Construire l’URL REST
endpoint = f"{url}/rest/v1/{table}"

# Headers nécessaires
headers = {
    "apikey": key,
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# Faire une requête GET simple
response = requests.get(endpoint, headers=headers, params={"limit": 1})

if response.status_code == 200:
    print("Connexion réussie ✅")
    print(response.json())
else:
    print("Erreur ❌", response.status_code, response.text)




import streamlit as st
from supabase import create_client, Client

# Clés Supabase (trouvées dans Project Settings → API)
url = "https://ymjabtkhikeofdfyltra.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InltamFidGtoaWtlb2ZkZnlsdHJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NzE2MjEsImV4cCI6MjA4MDI0NzYyMX0.2fdaFWK5oFz405ECG0qhXN3Z2KCjLS54kuA9XCuEfDM"
# Variable
VarTxt = "Hello Word"
supabase: Client = create_client(url, key)
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
with st.form("user_form"):
    f_name = st.text_input("Prénom")
    l_name = st.text_input("Nom")
    email = st.text_input("Email (obligatoire)")
    job_title = st.text_input("Titre du poste")
    company = st.text_input("Entreprise")

    submit = st.form_submit_button("Créer user")

if submit:
    if email.strip() == "":
        st.error("Email est obligatoire !")
    else:
        data = {
            "f_name": f_name,
            "l_name": l_name,
            "job_title": job_title,
            "company": company,
            "email": email
        }
        try:
            supabase.table("t_user").insert(data).execute()
            st.success(f"Utilisateur {f_name} {l_name} créé avec succès !")
        except Exception as e:
            st.error(f"Erreur : {e}")
