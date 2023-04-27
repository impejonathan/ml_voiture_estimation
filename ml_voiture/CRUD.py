import sqlite3
import csv
from typing import Union


def create_voiture(marque: str, modele: str, type_de_carburant: str, aspiration: str, nombre_de_portes: int, carrosserie: str, roues_motrices: str, emplacement_moteur: str, type_de_moteur: str, nombre_de_cylindres: int, taille_moteur_en_litres: float, puissance: Union[int,float], rpm_max: int, consommation_ville: Union[int,float], consommation_autoroute: Union[int,float], prix: Union[int,float]) -> None:
    """
    Crée une nouvelle voiture dans la base de données.

    Args:
        marque (str): La marque de la voiture.
        modele (str): Le modèle de la voiture.
        type_de_carburant (str): Le type de carburant utilisé par la voiture.
        aspiration (str): L'aspiration de la voiture.
        nombre_de_portes (int): Le nombre de portes de la voiture.
        carrosserie (str): La carrosserie de la voiture.
        roues_motrices (str): Les roues motrices de la voiture.
        emplacement_moteur (str): L'emplacement du moteur de la voiture.
        type_de_moteur (str): Le type de moteur de la voiture.
        nombre_de_cylindres (int): Le nombre de cylindres du moteur de la voiture.
        taille_moteur_en_litres (float): La taille du moteur en litres.
        puissance (Union[int,float]): La puissance du moteur en chevaux-vapeur ou en kilowatts.
        rpm_max (int): Le régime maximal du moteur en tours par minute.
        consommation_ville (Union[int,float]): La consommation en ville en litres aux 100 km ou en miles par gallon.
        consommation_autoroute (Union[int,float]): La consommation sur autoroute en litres aux 100 km ou en miles par gallon.
        prix (Union[int,float]): Le prix de la voiture.

    Returns:
        None
    """
    connexion = sqlite3.connect("voiture.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO voiture (marque, modele, type_de_carburant, aspiration, nombre_de_portes, carrosserie, roues_motrices, emplacement_moteur,type_de_moteur,nombre_de_cylindres,taille_moteur_en_litres,puissance,rpm_max,consommation_ville,consommation_autoroute,prix) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (marque, modele,type_de_carburant ,aspiration ,nombre_de_portes ,carrosserie ,roues_motrices ,emplacement_moteur ,type_de_moteur ,nombre_de_cylindres ,taille_moteur_en_litres ,puissance ,rpm_max ,consommation_ville ,consommation_autoroute ,prix))
    connexion.commit()
    connexion.close()

# def read_voitures():
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     curseur.execute("SELECT * FROM voiture")
#     rows = curseur.fetchall()
#     for row in rows:
#         print(row)
#     connexion.close()
    
    
    
# def recuperer_voitures_par_marque(marque):
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     curseur.execute("SELECT * FROM voiture WHERE marque = ?", (marque,))
#     rows = curseur.fetchall()
#     for row in rows:
#         print(row)
#     connexion.close()
    

# def recuperer_voitures_par_nombre_de_cylindres(nombre_de_cylindres):
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     curseur.execute("SELECT * FROM voiture WHERE nombre_de_cylindres = ?", (nombre_de_cylindres,))
#     rows = curseur.fetchall()
#     for row in rows:
#         print(row)
#     connexion.close()

# def recuperer_voitures_par_prix(min_prix, max_prix):
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     curseur.execute("SELECT * FROM voiture WHERE prix BETWEEN ? AND ?", (min_prix, max_prix))
#     rows = curseur.fetchall()
#     for row in rows:
#         print(row)
#     connexion.close()


# def update_voiture(id_, marque):
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     curseur.execute("UPDATE voiture SET marque = ? WHERE id = ?", (marque,id_))
#     connexion.commit()
#     connexion.close()


def delete_voiture(id_: int) -> None:
    """
    Supprime une voiture de la base de données en utilisant son ID.

    Args:
        id_ (int): L'ID de la voiture à supprimer.

    Returns:
        None
    """
    connexion = sqlite3.connect("voiture.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM voiture WHERE id = ?", (id_,))
    connexion.commit()
    connexion.close()


def create_utilisateur(nom: str, email: str, mdp: str) -> None:
    """
    Crée un nouvel utilisateur dans la base de données.

    Args:
        nom (str): Le nom de l'utilisateur.
        email (str): L'adresse e-mail de l'utilisateur.
        mdp (str): Le mot de passe de l'utilisateur.

    Returns:
        None
    """
    connexion = sqlite3.connect("voiture.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO utilisateur (nom,email,mdp) VALUES (?,?,?)", (nom,email,mdp))
    connexion.commit()
    connexion.close()

# def read_utilisateurs():
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     curseur.execute("SELECT * FROM utilisateur")
#     rows = curseur.fetchall()
#     for row in rows:
#         print(row)
#     connexion.close()

# def update_utilisateur(id_, nom):
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     curseur.execute("UPDATE utilisateur SET nom = ? WHERE id = ?", (nom,id_))
#     connexion.commit()
#     connexion.close()

# def delete_utilisateur(id_):
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     curseur.execute("DELETE FROM utilisateur WHERE id = ?", (id_,))
#     connexion.commit()




##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
## -----------------------------   FONCTION QUI VA RECHERCHER LES INFO DU CSV POUR LES REMPLIRE -------------------------------------------
##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def remplir_voiture_depuis_csv(fichier_csv):
#     connexion = sqlite3.connect("voiture.db")
#     curseur = connexion.cursor()
#     with open(fichier_csv, 'r') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             marque = row['marque']
#             modele = row['modele']
#             type_de_carburant = row['type_de_carburant']
#             aspiration = row['aspiration']
#             nombre_de_portes = row['nombre_de_portes']
#             carrosserie = row['carrosserie']
#             roues_motrices = row['roues_motrices']
#             emplacement_moteur = row['emplacement_moteur']
#             type_de_moteur = row['type_de_moteur']
#             nombre_de_cylindres = row['nombre_de_cylindres']
#             taille_moteur_en_litres = row['taille_moteur_en_litres']
#             puissance = row['puissance']
#             rpm_max = row['rpm_max']
#             consommation_ville = row['consommation_ville']
#             consommation_autoroute = row['consommation_autoroute']
#             prix = row['prix']

#             curseur.execute("INSERT INTO voiture (marque, modele, type_de_carburant, aspiration, nombre_de_portes, carrosserie, roues_motrices, emplacement_moteur,type_de_moteur,nombre_de_cylindres,taille_moteur_en_litres,puissance,rpm_max,consommation_ville,consommation_autoroute,prix) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (marque, modele,type_de_carburant ,aspiration ,nombre_de_portes ,carrosserie ,roues_motrices ,emplacement_moteur ,type_de_moteur ,nombre_de_cylindres ,taille_moteur_en_litres ,puissance ,rpm_max ,consommation_ville ,consommation_autoroute ,prix))
#     connexion.commit()
#     connexion.close()


# remplir_voiture_depuis_csv("donnees_propre.csv")