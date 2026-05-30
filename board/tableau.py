# Columna del tableau: una de las siete pilas centrales del tablero
# donde se construyen secuencias descendentes de colores alternados.
class TableauPile:

    def __init__(self):

        # Secuencia de cartas de la columna, de base (índice 0) a cima.
        self.cards = []

    def add_cards(self, cards):
        """
        Apila una o varias cartas al tope de la columna.
        """

        self.cards.extend(cards)

    def remove_cards(self, start_index):
        """
        Extrae y retorna el segmento de cartas desde start_index hasta la cima.
        Permite mover secuencias completas entre columnas del tableau.
        """

        removed_cards = self.cards[start_index:]

        self.cards = self.cards[:start_index]

        return removed_cards

    def top_card(self):
        """
        Retorna la carta en la cima de la columna, o None si está vacía.
        """

        if self.cards:
            return self.cards[-1]

        return None

    def reveal_top_card(self):
        """
        Voltea la carta de la cima si está oculta.
        Se llama automáticamente tras mover o remover cartas de la columna.
        """

        if self.cards and not self.cards[-1].face_up:
            self.cards[-1].flip()

    def is_empty(self):
        """
        Retorna True si la columna no contiene cartas.
        """

        return len(self.cards) == 0
