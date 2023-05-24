import streamlit as st
import pandas as pd
import pickle
import sqlite3
import hashlib
from typing import Union
from CRUD import create_voiture

def verifier_utilisateur(email: str, mdp: str) -> bool:
    """
    Vérifie si l'utilisateur est valide en interrogeant la base de données pour trouver l'utilisateur correspondant.

    Args:
        email (str): L'email de l'utilisateur à vérifier.
        mdp (str): Le mot de passe de l'utilisateur à vérifier.

    Returns:
        bool: True si l'utilisateur est valide, False sinon.
    """
    connexion = sqlite3.connect("voiture.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM utilisateur WHERE email=? AND mdp=?", (email, hashlib.sha256(mdp.encode()).hexdigest()))
    resultat = curseur.fetchone()
    connexion.close()

    if resultat:
        return True
    else:
        return False


def ajout():
    # Demander l'email et le mot de passe à l'utilisateur
    email = st.text_input("Entrez votre email")
    mdp = st.text_input("Entrez votre mot de passe", type="password")

    # Vérifier si l'utilisateur est valide
    if verifier_utilisateur(email, mdp):

        st.title("Ajouter une voiture")

        # Create four columns
        col1, col2, col3, col4 = st.columns(4)

        # Place widgets in the first column
        marque = col1.text_input("Marque :")
        type_de_carburant = col1.selectbox("Type de carburant :", ["Essence", "Diesel", "Électrique","GPL", "E85"])
        nombre_de_portes = col1.number_input("Nombre de portes :", min_value=2, max_value=5, value=4)
        roues_motrices = col1.selectbox("Roues motrices :", [ 'propulsion',   'traction',   'quatre roues motrices'])
        
        # Place widgets in the second column
        modele = col2.text_input("Modèle :")
        aspiration = col2.selectbox("Aspiration :", ["std", "Turbo"])
        carrosserie = col2.selectbox("Carrosserie :", ['cabriolet','hayon',   'berline',   'break', 'coupe'])
        type_de_moteur = col2.selectbox("Type de moteur :", ['dohc' ,'ohcv', 'ohc' ,'l', 'rotor'])


        # Place widgets in the third column
        puissance = col4.number_input("Puissance en chevaux-vapeur :", min_value=50, max_value=1000, value=100, step=10)
        consommation_ville = col4.number_input("Consommation en ville en litres aux 100 km :", min_value=2.0, max_value=30.0, value=7.0, step=0.1)
        consommation_autoroute = col4.number_input("Consommation sur autoroute en litres aux 100 km :", min_value=2.0, max_value=30.0, value=5.0, step=0.1)
        prix = col4.number_input("Prix :", min_value=1000, max_value=1000000, value=20000, step=1000)
        
        # Place widgets in the 4 column
        taille_moteur_en_litres = col3.number_input("Taille du moteur en litres :", min_value=0.5, max_value=8.0, value=1.6, step=0.1)
        rpm_max = col3.number_input("Régime maximal en tours par minute :", min_value=5000, max_value=15000, value=7000)
        emplacement_moteur = col3.selectbox("Emplacement du moteur :", ["avant", "arriere"])
        nombre_de_cylindres = col3.number_input("Nombre de cylindres :", min_value=2, max_value=16, value=4)

        button_html = """
        <style>
            .big-red-button {
                background-color: green;
                color: white;
                font-size: 20px;
                padding: 10px 20px;
                cursor: pointer;
                display: block;
                margin: 0 auto;
            }
        </style>
        <button class="big-red-button" onclick="location.href='/';">Ajouter</button>
    """

        if st.button("Ajouter"):
            create_voiture(marque, modele, type_de_carburant, aspiration, nombre_de_portes, carrosserie, roues_motrices, emplacement_moteur, type_de_moteur, nombre_de_cylindres, taille_moteur_en_litres, puissance, rpm_max, consommation_ville, consommation_autoroute, prix)
            st.success("La voiture a été ajoutée avec succès à la base de données !")



    else:
        st.write("L'utilisateur n'est pas valide.")
