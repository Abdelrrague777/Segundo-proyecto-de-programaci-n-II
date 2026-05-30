import flet as ft


# Aquí centralizamos las animaciones del proyecto.
# Esto ayuda a mantener consistencia visual.
class Animations:

    @staticmethod
    def card_move_animation():
        """
        Animación estándar para movimiento de cartas.
        """

        return ft.Animation(
            duration=250,
            curve=ft.AnimationCurve.EASE_IN_OUT,
        )

    @staticmethod
    def card_flip_animation():
        """
        Animación utilizada al voltear cartas.
        """

        return ft.Animation(
            duration=180,
            curve=ft.AnimationCurve.EASE_IN,
        )

    @staticmethod
    def win_animation():
        """
        Animación especial para victoria.
        """

        return ft.Animation(
            duration=500,
            curve=ft.AnimationCurve.BOUNCE_OUT,
        )