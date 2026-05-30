# Pila de destino final del solitario.
# Agrupa cartas de un mismo palo en orden ascendente (A → K).
# El juego se gana cuando las cuatro foundations están completas.
class FoundationPile:

    def __init__(self):

        # Secuencia de cartas del palo, de As (índice 0) a Rey (cima).
        self.cards = []

    def push_card(self, card):
        """
        Coloca una carta en la cima de la foundation.
        """

        self.cards.append(card)

    def pop_card(self):
        """
        Retira y retorna la carta de la cima, o None si la foundation está vacía.
        """

        if self.cards:
            return self.cards.pop()

        return None

    def top_card(self):
        """
        Retorna la carta en la cima de la foundation, o None si está vacía.
        """

        if self.cards:
            return self.cards[-1]

        return None

    def is_empty(self):
        """
        Retorna True si la foundation no contiene cartas aún.
        """

        return len(self.cards) == 0
