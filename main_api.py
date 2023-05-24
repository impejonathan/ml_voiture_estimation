from pydantic import BaseModel
import sqlite3
import hashlib
import secrets
from fastapi import FastAPI, HTTPException,Header, Path , Depends
from CRUD import *

connexion = sqlite3.connect('voiture.db')
app = FastAPI(openapi_url="/openapi.json", docs_url="/")


# LES CLASS ---------------------------------------------------------------------------------------
class Utilisateur(BaseModel):

    nom: str
    email: str
    mdp: str
    
class Voiture(BaseModel):
    marque: str
    modele: str
    type_de_carburant: str
    aspiration: str
    nombre_de_portes: int
    carrosserie: str
    roues_motrices: str
    emplacement_moteur: str
    type_de_moteur: str
    nombre_de_cylindres: int
    taille_moteur_en_litres: float
    puissance: int
    rpm_max: int
    consommation_ville: float
    consommation_autoroute: float
    prix: float
    
    
class VoitureSupprimer(BaseModel):
    marque: str
    modele: str
    prix: float
    
# LES POST ---------------------------------------------------------------------------------------




# Define a dependency for verifying the token
async def verify_token(token: str = Header(...)):
    """
    Vérifie si le token fourni est valide en le recherchant dans la table `utilisateur` de la base de données.
    Si le token est invalide, lève une exception HTTP 401.
    Sinon, renvoie l'ID de l'utilisateur associé au token.

    :param token: Le token à vérifier.
    :type token: str
    :return: L'ID de l'utilisateur associé au token, ou None si le token est invalide.
    :rtype: Optional[int]
    """
    curseur = connexion.cursor()
    curseur.execute("""
        SELECT * FROM utilisateur WHERE token = ?
    """, (token,))
    res = curseur.fetchone()

    if not res:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Pass the user ID to the endpoint that depends on this function
    return res[0]

# Add the dependency to the /creer_voiture endpoint
@app.post("/creer_voiture")
async def creer_voiture(voiture : Voiture, user_id: int = Depends(verify_token)):
    """
    Crée une nouvelle voiture dans la base de données en utilisant les informations fournies dans l'objet `voiture`.
    Cette fonction dépend de la fonction `verify_token` pour vérifier si l'utilisateur est autorisé à créer une voiture.

    :param voiture: Les informations de la voiture à créer.
    :type voiture: Voiture
    :param user_id: L'ID de l'utilisateur qui crée la voiture (fourni par la fonction `verify_token`).
    :type user_id: int
    """
    create_voiture(voiture.marque, voiture.modele, voiture.type_de_carburant, voiture.aspiration, voiture.nombre_de_portes, voiture.carrosserie, voiture.roues_motrices, voiture.emplacement_moteur, voiture.type_de_moteur, voiture.nombre_de_cylindres, voiture.taille_moteur_en_litres, voiture.puissance, voiture.rpm_max, voiture.consommation_ville, voiture.consommation_autoroute, voiture.prix)


# @app.post("/creer_voiture")
# async def creer_voiture(voiture : Voiture):
#     create_voiture(voiture.marque, voiture.modele, voiture.type_de_carburant, voiture.aspiration, voiture.nombre_de_portes, voiture.carrosserie, voiture.roues_motrices, voiture.emplacement_moteur, voiture.type_de_moteur, voiture.nombre_de_cylindres, voiture.taille_moteur_en_litres, voiture.puissance, voiture.rpm_max, voiture.consommation_ville, voiture.consommation_autoroute, voiture.prix)

@app.post("/creer_utilisateur")
async def creer_utilisateur(utilisateur: Utilisateur):
    
    curseur = connexion.cursor()
    curseur.execute("""
        SELECT * FROM utilisateur WHERE email = ?
    """, (utilisateur.email,))
    res = curseur.fetchall()

    if res:
        raise HTTPException(status_code=400, detail="Un utilisateur avec cet email existe déjà")
    else:
        # Hash du mot de passe
        mdp_hash = hashlib.sha256(utilisateur.mdp.encode()).hexdigest()

        # Création de l'utilisateur avec un token unique
        token = secrets.token_hex(16)
        curseur.execute("""
            INSERT INTO utilisateur(nom, email, mdp, token)
            VALUES (?, ?, ?, ?)
        """, (utilisateur.nom, utilisateur.email, mdp_hash, token))
        connexion.commit()

        # Renvoi de l'utilisateur avec son token
        return {"id": curseur.lastrowid, "nom": utilisateur.nom, "email": utilisateur.email, "token": token}

# LES DELETE  ---------------------------------------------------------------------------------------


@app.delete("/supprimer_voiture/{id}")
async def supprimer_voiture(id: int = Path(..., description="L'ID de la voiture à supprimer")):
    """
    Supprime une voiture en utilisant son ID.

    Args:
        id (int): L'ID de la voiture à supprimer.

    Returns:
        None
    """
    delete_voiture(id)