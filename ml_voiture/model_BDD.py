import sqlite3

connexion = sqlite3.connect("voiture.db")

curseur = connexion.cursor()




curseur.execute("""
                CREATE TABLE IF NOT EXISTS voiture(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    marque TEXT NOT NULL,
                    modele TEXT NOT NULL,
                    type_de_carburant TEXT NOT NULL,
                    aspiration TEXT NOT NULL,
                    nombre_de_portes INTEGER NOT NULL,
                    carrosserie TEXT NOT NULL,
                    roues_motrices TEXT NOT NULL,
                    emplacement_moteur TEXT NOT NULL,
                    type_de_moteur TEXT NOT NULL,
                    nombre_de_cylindres INTEGER NOT NULL,
                    taille_moteur_en_litres REAL NOT NULL,
                    puissance INTEGER NOT NULL,
                    rpm_max TEXT INTEGER NULL,
                    consommation_ville REAL NOT NULL,
                    consommation_autoroute REAL NOT NULL,
                    
                    prix REAL NOT NULL
                )
                
                """)


connexion.commit()

curseur.execute("""
                CREATE TABLE IF NOT EXISTS utilisateur(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    email TEXT NOT NULL,
                    mdp TEXT NOT NULL,
                    token TEXT NOT NULL
                )
                
                """)


connexion.commit()

# def supprimer_table_utilisateur():
#     connexion = sqlite3.connect('voiture.db')
#     curseur = connexion.cursor()
#     curseur.execute("DROP TABLE IF EXISTS utilisateur")
#     connexion.commit()
#     connexion.close()
    
# supprimer_table_utilisateur()
