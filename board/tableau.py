# Esta clase representa una columna del tableau.
# Aquí se almacenan las cartas principales del juego.
class TableauPile:

    def __init__(self):

        # Lista de cartas dentro de la columna.
        self.cards = []

    def add_cards(self, cards):
        """
        Agrega una o varias cartas al final de la columna.
        """

        self.cards.extend(cards)

    def remove_cards(self, start_index):
        """
        Remueve un grupo de cartas desde cierto índice.

        Esto es importante porque en Solitaire
        pueden moverse varias cartas juntas.
        """

        removed_cards = self.cards[start_index:]

        self.cards = self.cards[:start_index]

        return removed_cards

    def top_card(self):
        """
        Retorna la carta superior de la columna.
        """

        if self.cards:
            return self.cards[-1]

        return None

    def reveal_top_card(self):
        """
        Si la carta superior está oculta,
        la voltea automáticamente.
        """

        if self.cards and not self.cards[-1].face_up:
            self.cards[-1].flip()

    def is_empty(self):
        """
        Verifica si la columna está vacía.
        """

        return len(self.cards) == 0