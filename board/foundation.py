# Esta clase representa una foundation.
# Las foundations son las pilas finales
# donde se organizan las cartas por palo.
class FoundationPile:

    def __init__(self):

        # Cartas actuales de la foundation.
        self.cards = []

    def push_card(self, card):
        """
        Agrega una carta a la foundation.
        """

        self.cards.append(card)

    def pop_card(self):
        """
        Remueve la carta superior.
        """

        if self.cards:
            return self.cards.pop()

        return None

    def top_card(self):
        """
        Retorna la carta superior actual.
        """

        if self.cards:
            return self.cards[-1]

        return None

    def is_empty(self):
        """
        Verifica si la foundation está vacía.
        """

        return len(self.cards) == 0