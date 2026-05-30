import flet as ft

from ui.styles import (
    CARD_WIDTH,
    CARD_HEIGHT,
    CARD_FRONT_COLOR,
    CARD_BACK_COLOR,
    CARD_BORDER_RADIUS,
)


# Este componente representa visualmente una carta.
# Aquí NO manejamos reglas del juego,
# solamente apariencia y renderizado(Diseño de cartas y como luce de frente y de espaldas).
class CardView(ft.Container):

    def __init__(self, card):

        super().__init__()

        self.card = card

        # Configuración visual base.
        self.width = CARD_WIDTH
        self.height = CARD_HEIGHT

        self.border_radius = CARD_BORDER_RADIUS

        self.alignment = ft.alignment.center

        # Pequeña sombra para dar profundidad visual.
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLACK26,
        )

        # Construimos el contenido inicial.
        self.update_card_view()

    def update_card_view(self):
        """
        Actualiza la apariencia de la carta
        dependiendo de si está boca arriba o abajo.
        """

        # Carta visible.
        if self.card.face_up:

            self.bgcolor = CARD_FRONT_COLOR

            # Elegimos color del texto según el palo.
            text_color = (
                ft.Colors.RED
                if self.card.color == "red"
                else ft.Colors.BLACK
            )

            self.content = ft.Column(
                controls=[
                    ft.Text(
                        self.card.rank,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=text_color,
                    ),

                    ft.Text(
                        self.card.suit,
                        size=18,
                        color=text_color,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )

        # Carta boca abajo.
        else:

            self.bgcolor = CARD_BACK_COLOR

            self.content = ft.Text(
                "SOL",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            )