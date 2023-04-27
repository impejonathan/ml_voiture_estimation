import sqlite3
from typing import NoReturn

def delete_string_brand() -> NoReturn:
    """
    Supprime toutes les entrées de la table `voiture` dans la base de données `voiture`
    où la colonne `marque` est égale à `"string"`.
    """
    # Connect to the database
    conn = sqlite3.connect('voiture.db')
    c = conn.cursor()

    # Execute the DELETE statement
    c.execute("DELETE FROM voiture WHERE marque = 'string'")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()



delete_string_brand()