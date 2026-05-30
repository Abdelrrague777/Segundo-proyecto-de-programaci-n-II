import flet as ft

from ui.styles import TABLE_COLOR


# Vista principal del tablero, construida como columna vertical de dos filas.
# La fila superior contiene stock, waste y foundations; la inferior el tableau.
class GameView(ft.Column):

    def __init__(self):

        super().__init__()

        # Propiedades base del contenedor principal.
        self.expand = True

        self.spacing = 20

        self.bgcolor = TABLE_COLOR

        # Fila superior que aloja el stock, el waste y las cuatro foundations.
        self.top_row = ft.Row(
            spacing=20,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # Fila inferior que aloja las siete columnas del tableau con scroll horizontal.
        self.tableau_row = ft.Row(
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        )

        # Estructura vertical del tablero: fila superior seguida del tableau.
        self.controls = [
            self.top_row,
            self.tableau_row,
        ]

    def add_tableau_pile(self, pile_view):
        """
        Registra una columna del tableau en la fila inferior del tablero.
        """

        self.tableau_row.controls.append(pile_view)

    def add_foundation_pile(self, pile_view):
        """
        Registra una foundation en la fila superior del tablero.
        """

        self.top_row.controls.append(pile_view)

    def refresh_board(self):
        """
        Solicita a Flet que redibuje el tablero tras cualquier cambio de estado.
        """

        self.update()