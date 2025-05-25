import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Mes Séries", layout="wide")

# Chargement et nettoyage du fichier CSV
users_df = pd.read_csv("users.csv")


# 🔧 S'assurer que les colonnes sont bien des chaînes et sans espaces
users_df['name'] = users_df['name'].apply(lambda x: str(x).strip())
users_df['password'] = users_df['password'].apply(lambda x: str(x).strip())



# Initialisation des variables de session
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

# Fonction de vérification des identifiants
def check_login(name, password):
    user_row = users_df[(users_df['name'] == name) & (users_df['password'] == password)]

    if not user_row.empty:
        return True
    return False

# Sidebar avec menu
with st.sidebar:
    if st.session_state.logged_in:
        st.markdown(f"Bienvenue *{st.session_state.username}*")
        page = st.radio("Navigation", ["🏠 Accueil", "📺 Mon Top Séries", "Déconnexion"])
    else:
        page = st.radio("Navigation", ["Login"])

# Si l'utilisateur n'est pas connecté
if not st.session_state.logged_in:
    if page == "Login":
        st.title("Page de connexion")
        name = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        if st.button("Se connecter"):
            if check_login(name, password):
                st.session_state.logged_in = True
                st.session_state.username = name
                st.success("Connexion réussie ✅")
                st.rerun()
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect ❌")

# Si l'utilisateur est connecté
else:
    if page == "🏠 Accueil":
        st.title("Welcome 🎬")
        st.write("Explore mon top séries ")
        st.image("https://media2.giphy.com/media/8Iv5lqKwKsZ2g/giphy.gif", width=700)

    elif page == "📺 Mon Top Séries":
        st.title("📺 My Top 3 TV Series")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://m.media-amazon.com/images/M/MV5BNzBiODQxZTUtNjc0MC00Yzc1LThmYTMtN2YwYTU3NjgxMmI4XkEyXkFqcGc@._V1_.jpg", width=200)
            st.subheader("Brooklyn Nine-Nine")
            st.caption("Comedy, Police — Une équipe de choc et de choc ! ")

        with col2:
            st.image("https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_A8EEAAE1-219E-457D-B1C1-7A2F8964DC96_2025-3-21-T14-26-29.jpg?s=260x371", width=200)
            st.subheader("Suits")
            st.caption("Legal, Drama — Avocats stylés et stratégies brillantes !")

        with col3:
            st.image("https://image.tmdb.org/t/p/original/Jfq6EpTxFeCX9vi3dKDgZDUZTy.jpg", width=200)
            st.subheader("Mindhunter")
            st.caption("Crime, Thriller — Profilage psychologique captivant !")

    elif page == "Déconnexion":
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.success("Déconnecté avec succès.")
        st.rerun()
