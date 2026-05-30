import flet as ft


# Fábrica de animaciones reutilizables para toda la interfaz.
# Centralizar los parámetros aquí garantiza coherencia visual entre componentes.
class Animations:

    @staticmethod
    def card_move_animation():
        """
        Animación suave de 250ms para el desplazamiento de cartas entre pilas.
        """

        return ft.Animation(
            duration=250,
            curve=ft.AnimationCurve.EASE_IN_OUT,
        )

    @staticmethod
    def card_flip_animation():
        """
        Animación rápida de 180ms para voltear una carta boca arriba o abajo.
        """

        return ft.Animation(
            duration=180,
            curve=ft.AnimationCurve.EASE_IN,
        )

    @staticmethod
    def win_animation():
        """
        Animación de 500ms con rebote final para celebrar la victoria del jugador.
        """

        return ft.Animation(
            duration=500,
            curve=ft.AnimationCurve.BOUNCE_OUT,
        )