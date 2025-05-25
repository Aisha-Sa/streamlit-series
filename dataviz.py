import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib as plt

st.title("Manipulation de données et création de graphique")


# chargement du dataset 
dataset = sns.get_dataset_names()


# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
names = st.selectbox("Quels dataset veux-tu utliser :", dataset ) 
st.write('___')


# Chargement du dataset sélectionné
df = sns.load_dataset(names)


st.subheader(f"Dataset : {names}")
st.dataframe(df)


# Sélection des colonnes 
columns = df.columns.tolist()

x_col = st.selectbox("Sélectionner la colonne X :", columns)
y_col = st.selectbox("Sélectionner la colonne Y :", columns)

# Choix du type de graphique
graph = st.radio("Choisir un type de graphique :", ("scatter_chart", "bar_chart", "line_chart"))

# Affichage du graphique
st.subheader("Graphique")


if graph == "scatter_chart":
        st.scatter_chart(df[[x_col, y_col]])
elif graph == "bar_chart":
        st.bar_chart(df[[x_col, y_col]])
elif graph == "line_chart":
        st.line_chart(df[[x_col, y_col]])


# Affichage de la matrice de corrélation
if st.checkbox("Afficher la matrice de corrélation (colonnes numériques uniquement)"):
    st.subheader("Matrice de corrélation")
    numerique = df.select_dtypes(include='number')
    if not numerique.empty:
        corr = numerique.corr()
        st.dataframe(corr.style.background_gradient(cmap= "BuPu").format("{:.2f}"))
    else:
        st.info("Aucune colonne numérique disponible dans ce dataset.")