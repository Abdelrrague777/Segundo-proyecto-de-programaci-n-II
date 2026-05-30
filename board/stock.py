# Gestiona el stock (mazo oculto) y el waste pile (cartas descartadas visibles).
class StockPile:

    def __init__(self, cards):

        # Mazo principal boca abajo; se roba de aquí durante el juego.
        self.stock = cards

        # Pila de descarte; contiene las cartas robadas boca arriba.
        self.waste = []

    def draw_from_stock(self):
        """
        Roba la carta superior del stock y la transfiere al waste pile.
        Retorna la carta robada, o None si el stock está vacío.
        """

        if self.stock:

            card = self.stock.pop()

            # Voltear la carta al pasarla al waste.
            card.face_up = True

            self.waste.append(card)

            return card

        return None

    def reset_stock(self):
        """
        Recicla el waste pile devolviéndolo al stock en orden inverso
        cuando el mazo principal se agota.
        """

        # Revertir el waste conserva el orden original de robo.
        self.stock = list(reversed(self.waste))

        # Las cartas regresan al stock boca abajo.
        for card in self.stock:
            card.face_up = False

        self.waste.clear()

    def top_waste_card(self):
        """
        Retorna la carta visible en la cima del waste pile,
        o None si el waste está vacío.
        """

        if self.waste:
            return self.waste[-1]

        return None