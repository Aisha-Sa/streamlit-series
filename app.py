import streamlit as st
import pandas as pd 

# Titre principal de l'application (affiché en haut de la page)
st.title("Welcome to Aisha's website ")

# Charger le fichier CSV depuis l'URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)

# Extraire les arrondissements uniques
boroughs = df['pickup_borough'].unique()



# Menu déroulant pour choisir un arrondissement
selected_borough = st.selectbox("Indicate your recovery district", boroughs)

# Affichage du choix
st.write("___")
st.write(f"You have selected : **{selected_borough}**")


# Dictionnaire pour les images  
images = {
    "Bronx": "https://previews.123rf.com/images/melpomen/melpomen2003/melpomen200300083/141274538-vue-a%C3%A9rienne-du-bronx-new-york-city.jpg",
    "Manhattan": "https://www.new-york-city.fr/wp-content/uploads/2020/11/Manahttan_principale.jpg",
    "Brooklyn" : "https://trvlr.fr/wp-content/uploads/2020/08/brooklyn-bridge-conseils-village-trvlr-voyage-que-voir-que-faire-7-jours.jpg",
    "Queens" : "https://img-0.journaldunet.com/wyD16CX0gsH7HNq_arW4j-MRImA=/1240x/smart/bcf15ea4e4ee4b90ad12717f76fa29b9/ccmcms-jdn/10214805-13-fotolia-55605989-seanpavonephoto-fotoliacom.jpg"
    
}

# Afficher l'image du dictionnaire 
if selected_borough in images:
    st.image(images[selected_borough], caption=selected_borough, use_container_width=True)
