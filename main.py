from core.deck import Deck
from board.tableau import TableauPile
from board.foundation import FoundationPile
from board.stock import StockPile
from board.move_manager import MoveManager
from ui.game_view import GameView
from ui.card_view import CardView
from core.game_rules import GameRules


# Esta clase coordina todo el flujo principal del juego.
# Aquí conectamos lógica, tablero y UI.
class GameController:

    def __init__(self, page):

        self.page = page

        # Inicializamos el mazo principal.
        self.deck = Deck()

        self.deck.shuffle()

        # Administrador de movimientos.
        self.move_manager = MoveManager()

        # Creamos las columnas del tableau.
        self.tableau_piles = [
            TableauPile() for _ in range(7)
        ]

        # Creamos las foundations.
        self.foundation_piles = [
            FoundationPile() for _ in range(4)
        ]

        # Creamos stock y waste.
        self.stock_pile = StockPile(self.deck.cards)

        # Vista principal del tablero.
        self.game_view = GameView()

    def setup_tableau(self):
        """
        Reparte las cartas iniciales
        en las columnas del tableau.
        """

        for column_index in range(7):

            for row_index in range(column_index + 1):

                card = self.stock_pile.stock.pop()

                # La última carta debe quedar visible.
                if row_index == column_index:
                    card.face_up = True

                self.tableau_piles[column_index].add_cards([card])

    def build_ui(self):
        """
        Construye visualmente todas las columnas.
        """

        for pile in self.tableau_piles:

            pile_column = self.create_tableau_column(pile)

            self.game_view.add_tableau_pile(
                pile_column
            )

    def create_tableau_column(self, pile):
        """
        Convierte una columna lógica
        en una columna visual de Flet.
        """

        controls = []

        for card in pile.cards:

            card_view = CardView(card)

            controls.append(card_view)

        return controls

    def start_game(self):
        """
        Inicia completamente la partida.
        """

        self.setup_tableau()

        self.build_ui()

        self.page.add(self.game_view)

    def check_victory(self):
        """
        Verifica si el jugador ganó.
        """

        if GameRules.is_game_won(
            self.foundation_piles
        ):

            self.page.snack_bar = SnackBar(
                Text("Ganaste la partida")
            )

            self.page.snack_bar.open = True

            self.page.update()
Archivo: controller/drag_drop_handler.py
# Esta clase manejará toda la lógica
# de arrastrar y soltar cartas.
# Por ahora dejamos preparada
# la estructura principal para integrar después.
class DragDropHandler:

    def __init__(self, controller):

        self.controller = controller

    def handle_drag_start(self, event):
        """
        Se ejecuta cuando el usuario
        comienza a arrastrar una carta.
        """

        print("Inicio de drag")

    def handle_drag_end(self, event):
        """
        Se ejecuta cuando termina el drag.
        """

        print("Fin de drag")

    def handle_drop(self, event):
        """
        Aquí se validará el movimiento
        al soltar una carta.
        """

        print("Carta soltada")
Archivo: controller/event_manager.py
# Esta clase centraliza eventos generales
# del juego.
class EventManager:

    def __init__(self, controller):

        self.controller = controller

    def restart_game(self, event):
        """
        Reinicia completamente la partida.
        """

        print("Reiniciando juego")

    def undo_move(self, event):
        """
        Recupera el último movimiento.
        """

        print("Deshaciendo movimiento")

    def on_card_click(self, event):
        """
        Evento de click sobre carta.
        """

        print("Carta seleccionada")
Archivo: main.py
import flet as ft

from controller.game_controller import GameController


# Punto de entrada principal del proyecto.
# Aquí inicializamos Flet y lanzamos el juego.
def main(page: ft.Page):

    # Configuración general de ventana.
    page.title = "Solitario Klondike"

    page.window_width = 1400
    page.window_height = 900

    page.padding = 20

    # Color principal del fondo.
    page.bgcolor = "#0B6623"

    # Creamos el controlador principal.
    controller = GameController(page)

    # Iniciamos el juego.
    controller.start_game()


# Lanzamos la aplicación.
ft.app(target=main)
