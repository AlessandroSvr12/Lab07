from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo: str, epoca: str):
            """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
            artefatti_filtrati = []
            artefatti = self._artefatto_dao.get_all_artefatti()
            musei = self._museo_dao.get_all_musei()

            # controlli
            #print("entrato in get_artefatti_filtrati")
            #print("museo:", museo)
            #print("mpoca:", epoca)

            # Caso: nessun filtro
            if museo == "nessun filtro" and epoca == "nessun filtro":
                return artefatti
            # Caso: solo epoca
            if museo == "nessun filtro" and epoca != "nessun filtro":
                for artefatto in artefatti:
                    if artefatto.epoca == epoca:
                        artefatti_filtrati.append(artefatto)
                return artefatti_filtrati
            # Caso: solo museo
            if museo != "nessun filtro" and epoca == "nessun filtro":
                for artefatto in artefatti:
                    if str(artefatto.id_museo) == museo:
                        artefatti_filtrati.append(artefatto)
                return artefatti_filtrati
                # Caso entrambi i filtri
            if museo != "nessun filtro" and epoca != "nessun filtro":
                for artefatto in artefatti:
                    if str(artefatto.id_museo) == museo and artefatto.epoca == epoca:
                        artefatti_filtrati.append(artefatto)
                return artefatti_filtrati

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        epoche = []
        artefatti = self._artefatto_dao.get_all_artefatti()
        for i in artefatti:
            epoca = i.epoca
            if epoca not in epoche:
                epoche.append(epoca)
                #semi-ordino le epoche
                epoche.sort(key=lambda s: (0 if 'a.C' in s else 1, s.split()[0][::-1] if 'a.C' in s else s.split()[0]))
        return epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        musei = self._museo_dao.get_all_musei()
        return musei

