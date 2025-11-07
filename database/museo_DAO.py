from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def get_all_musei(self):
        conn = ConnessioneDB.get_connection()
        cursor = conn.cursor()
        musei = []
        cursor.execute("SELECT * FROM museo ")
        risultati = cursor.fetchall()
        for riga in risultati:
            museo = Museo(riga[0], riga[1], riga[2])
            musei.append(museo)
        cursor.close()
        conn.close()
        return musei if musei else None