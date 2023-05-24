import streamlit as st
import pandas as pd
import pickle
import sqlite3
from ajout_voiture import ajout



onglet = st.sidebar.selectbox("Choisissez un onglet", ["predict", "ajouter"])

if onglet == "predict":



    with open('voiture.pkl', 'rb') as file:
        pipe = pickle.load(file)




    connexion = sqlite3.connect("voiture.db")
    df = pd.read_sql_query("SELECT * FROM voiture", connexion)

    # Créer deux colonnes pour la marque et le modèle
    col1, col2, col3, col4 = st.columns(4)

    # Créer un sélecteur pour la marque dans la première colonne
    marques_uniques = list(df['marque'].unique())
    marques_uniques.sort()
    marque = col1.selectbox('Marque', marques_uniques)

    # Créer un sélecteur pour le modèle dans la deuxième colonne
    modele = col2.selectbox('Modèle', df.loc[df['marque'] == marque, 'modele'].unique())

    # Créer un sélecteur pour le type de carburant dans la troisième colonne
    type_de_carburant = col3.selectbox('Type de carburant', df['type_de_carburant'].unique())

    # Créer un sélecteur pour l'aspiration dans la quatrième colonne
    aspiration = col4.selectbox('Aspiration', df['aspiration'].unique())

    # Créer deux colonnes pour le nombre de portes et la carrosserie
    col5, col6, col7, col8 = st.columns(4)

    # Créer un sélecteur pour le nombre de portes dans la cinquième colonne
    nombre_de_portes = col5.selectbox('Nombre de portes', df['nombre_de_portes'].unique())

    # Créer un sélecteur pour la carrosserie dans la sixième colonne
    carrosserie = col6.selectbox('Carrosserie', df['carrosserie'].unique())

    # Créer un sélecteur pour les roues motrices dans la septième colonne
    roues_motrices = col7.selectbox('Roues motrices', df['roues_motrices'].unique())

    # Créer un sélecteur pour l'emplacement du moteur dans la huitième colonne
    emplacement_moteur = col8.selectbox('Emplacement du moteur', df['emplacement_moteur'].unique())

    # Créer quatre colonnes pour le type de moteur, le nombre de cylindres, la taille du moteur et la puissance
    col9, col10, col11, col12 = st.columns(4)

    # Créer un sélecteur pour le type de moteur dans la neuvième colonne
    type_de_moteur = col9.selectbox('Type de moteur', df['type_de_moteur'].unique())

    # Créer un sélecteur pour le nombre de cylindres dans la dixième colonne
    nombre_de_cylindres = col10.selectbox('Nombre de cylindres', df['nombre_de_cylindres'].unique())

    # Créer un champ pour saisir la taille du moteur dans la onzième colonne
    taille_moteur_en_litres = col11.number_input('Taille du moteur (en litres)')

    # Créer un champ pour saisir la puissance dans la douzième colonne
    puissance = col12.number_input('Puissance')

    # Créer quatre colonnes pour RPM max, consommation en ville et consommation sur autoroute
    col13, col14, col15 = st.columns(3)

    # Créer un champ pour saisir RPM max dans la treizième colonne
    rpm_max = col13.number_input('RPM max')

    # Créer un champ pour saisir la consommation en ville dans la quatorzième colonne
    consommation_ville = col14.number_input('Consommation en ville')

    # Créer un champ pour saisir la consommation sur autoroute dans la quinzième colonne
    consommation_autoroute = col15.number_input('Consommation sur autoroute')


    # Créer un DataFrame avec les valeurs saisies
    input_data = pd.DataFrame({
        'marque': [marque],
        "modele": [modele],
        'type_de_carburant': [type_de_carburant],
        'aspiration': [aspiration],
        'nombre_de_portes': [nombre_de_portes],
        'carrosserie': [carrosserie],
        'roues_motrices': [roues_motrices],
        'emplacement_moteur': [emplacement_moteur],
        'type_de_moteur': [type_de_moteur],
        'nombre_de_cylindres': [nombre_de_cylindres],
        'taille_moteur_en_litres': [taille_moteur_en_litres],
        'puissance': [puissance],
        'rpm_max': [rpm_max],
        'consommation_ville': [consommation_ville],
        'consommation_autoroute': [consommation_autoroute]
    })

    # Effectuer une prédiction avec le modèle entraîné
    prediction = pipe.predict(input_data)[0]

    # Afficher la prédiction
    st.markdown(f'<h2 style="text-align: center; color: green;">La prédiction du prix est de {prediction:.2f} $</h2>', unsafe_allow_html=True)



elif onglet == "ajouter":
    
    ajout()