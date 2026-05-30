import flet as ft

from ui.styles import (
    CARD_WIDTH,
    CARD_HEIGHT,
    CARD_FRONT_COLOR,
    CARD_BACK_COLOR,
    CARD_BORDER_RADIUS,
)

class CardView(ft.Container):

    def __init__(self, card):

        super().__init__()

        self.card = card

        self.width = CARD_WIDTH
        self.height = CARD_HEIGHT
        self.border_radius = CARD_BORDER_RADIUS

        # Alineación del contenedor usando la clase compatible
        self.alignment = ft.Alignment(0, 0)

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLACK26,
        )

        self.update_card_view()

    def update_card_view(self):

        if self.card.face_up:

            self.bgcolor = CARD_FRONT_COLOR

            # Color del texto basado en el palo de la carta
            text_color = (
                ft.Colors.RED
                if self.card.palo in ["corazones", "diamantes"]
                else ft.Colors.BLACK
            )


            self.content = ft.Column(
                controls=[
                    ft.Text(
                        self.card.valor,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=text_color,
                    ),

                    ft.Text(
                        self.card.palo,
                        size=18,
                        color=text_color,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )

        else:

            self.bgcolor = CARD_BACK_COLOR

            self.content = ft.Text(
                "SOL",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            )