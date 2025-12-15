from supabase import create_client, Client

# Configuration Supabase
SUPABASE_URL = "https://ymjabtkhikeofdfyltra.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InltamFidGtoaWtlb2ZkZnlsdHJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ2NzE2MjEsImV4cCI6MjA4MDI0NzYyMX0.2fdaFWK5oFz405ECG0qhXN3Z2KCjLS54kuA9XCuEfDM"  
supabase: Client = create_client(url, key)

def afficher_utilisateurs():
    try:
        # Sélection de tous les enregistrements de la table t_user
        response = supabase.table("t_user").select("*").execute()
        
        if response.data:
            print("Liste des utilisateurs :")
            for user in response.data:
                print(user)
        else:
            print("Aucun utilisateur trouvé dans la table t_user.")
    except Exception as e:
        print("Erreur lors de la récupération :", e)

if __name__ == "__main__":
    afficher_utilisateurs()
