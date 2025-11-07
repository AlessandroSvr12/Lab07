import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_musei(self):
        musei = self._model.get_musei()

        self._view.campo_museo.options = [
            ft.dropdown.Option(str(m.id), text=m.nome) for m in musei
        ]
        self._view.campo_museo.options.insert(0, ft.dropdown.Option("nessun filtro", text="nessun filtro"))
    def popola_epoche(self):
        epoche = self._model.get_epoche()

        self._view.campo_epoca.options = [
            ft.dropdown.Option(e) for e in epoche
        ]
        self._view.campo_epoca.options.insert(0, ft.dropdown.Option("nessun filtro", text="nessun filtro"))

    # CALLBACKS DROPDOWN
    #scegliendo un'opzione aggirona la selezione attuale
    def museo_dropdown(self,e):
        self.museo_selezionato=e.control.value
    def epoche_dropdown(self,e):
        self.epoca_selezionata=e.control.value
    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):
        self._view.lista_artefatti.controls.clear()
        artefatti_filtrati = self._model.get_artefatti_filtrati(
            self.museo_selezionato,
            self.epoca_selezionata
        )

        if not artefatti_filtrati:
            self._view.show_alert("Nessun artefatto trovato")
        else:
            for artefatto in artefatti_filtrati:
                self._view.lista_artefatti.controls.append(
                    ft.Text(f"{artefatto.nome} ({artefatto.epoca})")
                )

        self._view.lista_artefatti.update()
        self._view.update()
