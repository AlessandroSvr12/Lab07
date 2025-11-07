from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    def get_all_artefatti(self):
        conn = ConnessioneDB.get_connection()
        cursor = conn.cursor()
        artefatti = []
        cursor.execute("SELECT * FROM artefatto")
        risultati = cursor.fetchall()
        for riga in risultati:
            artefatto = Artefatto(riga[0], riga[1], riga[2], riga[3], riga[4])
            artefatti.append(artefatto)
        cursor.close()
        conn.close()
        return artefatti if artefatti else None
