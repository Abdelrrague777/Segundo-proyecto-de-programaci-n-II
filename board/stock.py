# Esta clase administra el stock principal
# y también el waste pile.
class StockPile:

    def __init__(self, cards):

        # Cartas restantes del mazo.
        self.stock = cards

        # Cartas reveladas.
        self.waste = []

    def draw_from_stock(self):
        """
        Toma una carta del stock
        y la mueve al waste.
        """

        if self.stock:

            card = self.stock.pop()

            # La carta debe mostrarse boca arriba.
            card.face_up = True

            self.waste.append(card)

            return card

        return None

    def reset_stock(self):
        """
        Cuando el stock se vacía,
        reutilizamos las cartas del waste.
        """

        # Invertimos las cartas para conservar
        # el orden correcto del juego.
        self.stock = list(reversed(self.waste))

        # Todas vuelven boca abajo.
        for card in self.stock:
            card.face_up = False

        self.waste.clear()

    def top_waste_card(self):
        """
        Retorna la carta superior del waste.
        """

        if self.waste:
            return self.waste[-1]

        return None