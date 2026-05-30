import flet as ft

from ui.styles import (
    CARD_WIDTH,
    CARD_HEIGHT,
    CARD_FRONT_COLOR,
    CARD_BACK_COLOR,
    CARD_BORDER_RADIUS,
)


# Componente visual de una carta individual, sin lógica de reglas.
# Renderiza el anverso con rango y palo, o el reverso con fondo azul y texto decorativo.
class CardView(ft.Container):

    def __init__(self, card):

        super().__init__()

        self.card = card

        # Dimensiones y forma base del contenedor de la carta.
        self.width = CARD_WIDTH
        self.height = CARD_HEIGHT

        self.border_radius = CARD_BORDER_RADIUS

        self.alignment = ft.alignment.center

        # Sombra sutil para simular profundidad sobre el tablero.
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLACK26,
        )

        # Renderizar la carta con su estado inicial.
        self.update_card_view()

    def update_card_view(self):
        """
        Redibuja la carta según su estado actual.
        Muestra el anverso si está boca arriba, o el reverso si está oculta.
        """

        # Anverso: fondo blanco con rango y palo en el color del palo correspondiente.
        if self.card.face_up:

            self.bgcolor = CARD_FRONT_COLOR

            # Palos rojos en rojo, palos negros en negro.
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

        # Reverso: fondo azul con texto decorativo que oculta el contenido.
        else:

            self.bgcolor = CARD_BACK_COLOR

            self.content = ft.Text(
                "SOL",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            )