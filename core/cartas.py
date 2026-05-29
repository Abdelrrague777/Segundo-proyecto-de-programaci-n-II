import random
from core.cartas import Carta


class Mazo:

    PALOS = [
        "corazones",
        "diamantes",
        "treboles",
        "espadas"
    ]

    VALORES = [
        "A", "2", "3", "4", "5", "6",
        "7", "8", "9", "10", "J", "Q", "K"
    ]

    def __init__(self):
        self.cartas = self.generar_mazo()

    def generar_mazo(self):
        return [
            Carta(palo, valor)
            for palo in self.PALOS
            for valor in self.VALORES
        ]

    def mezclar(self):
        random.shuffle(self.cartas)

    def sacar_carta(self):

        if self.cartas:
            return self.cartas.pop()

        return None

    def reiniciar_mazo(self):
        self.cartas = self.generar_mazo()
        self.mezclar()