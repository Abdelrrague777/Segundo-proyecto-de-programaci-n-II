import random
from core.cartas import Carta

class Deck:
    PALOS = ["corazones", "diamantes", "trebols", "espadas"]

    VALORES = [
        "A", "2", "3", "4", "5", "6",
        "7", "8", "9", "10", "J", "Q", "K"
    ]

    def __init__(self):
        self.cards = self.generar_mazo()

    def generar_mazo(self):
        return [
            Carta(palo, valor)
            for palo in self.PALOS
            for valor in self.VALORES
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def sacar_carta(self):
        if self.cards:
            return self.cards.pop()
        return None

    def reiniciar_mazo(self):
        self.cards = self.generar_mazo()
        self.shuffle()
