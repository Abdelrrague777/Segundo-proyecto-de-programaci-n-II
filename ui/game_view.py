import flet as ft
from ui.styles import TABLE_COLOR

class GameView(ft.Column):

    def __init__(self):

        super().__init__()

        self.expand = True
        self.spacing = 20
        self.bgcolor = TABLE_COLOR

        self.top_row = ft.Row(
            spacing=20,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        self.tableau_row = ft.Row(
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        )

        self.controls = [
            self.top_row,
            self.tableau_row,
        ]

    def add_tableau_pile(self, pile_view):

        self.tableau_row.controls.append(pile_view)

    def add_foundation_pile(self, pile_view):

        self.top_row.controls.append(pile_view)

    def refresh_board(self):

        self.update()
