import flet as ft

from ui.styles import TABLE_COLOR


# Esta vista representa el tablero completo del juego.
# Aquí organizamos visualmente todas las pilas.
class GameView(ft.Column):

    def __init__(self):

        super().__init__()

        # Configuración principal del layout.
        self.expand = True

        self.spacing = 20

        self.bgcolor = TABLE_COLOR

        # Fila superior:
        # stock + waste + foundations.
        self.top_row = ft.Row(
            spacing=20,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # Fila principal:
        # columnas tableau.
        self.tableau_row = ft.Row(
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        )

        # Agregamos todo al layout principal.
        self.controls = [
            self.top_row,
            self.tableau_row,
        ]

    def add_tableau_pile(self, pile_view):
        """
        Agrega una columna visual al tableau.
        """

        self.tableau_row.controls.append(pile_view)

    def add_foundation_pile(self, pile_view):
        """
        Agrega una foundation visual.
        """

        self.top_row.controls.append(pile_view)

    def refresh_board(self):
        """
        Fuerza actualización visual del tablero.
        """

        self.update()